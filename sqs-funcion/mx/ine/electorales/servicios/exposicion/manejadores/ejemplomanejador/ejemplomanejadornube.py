"""
	Copyright (c)  INE, UNICOM, México.
	Todos los derechos reservados.

	nombre_archivo=
	fecha_creacion= date, time

	Este software es información confidencial, propiedad del
	INE (Instituto Nacional Electoral). Esta información 
	no deberá ser divulgada y solo se podrá utilizar con base
	a los términos que el propio Instituto determine.
"""

"""
	TODO [Agregar importaciones requeridas de la clase]
"""

import json
import boto3
import sys
import os
import logging
import base64
import mysql.connector
from botocore.exceptions import ClientError

logging.basicConfig(format='[%(asctime)s] %(levelname)s: %(message)s', level=logging.DEBUG)

sqs = boto3.client('sqs')

queue_url = 'https://sqs.us-west-1.amazonaws.com/432132817178/sqs-demo'
queue_deadletter = 'https://sqs.us-west-1.amazonaws.com/432132817178/sqs-demo-error'
queue_url_destino_estructura = 'https://sqs.us-west-1.amazonaws.com/432132817178/'

secreto_bd = os.environ['secretobd']

session = boto3.session.Session()
client = session.client(
    service_name='secretsmanager',
    region_name='us-west-1'
)

destinos_dict = {
    "inicial": 'sqs-destino-1',
    "movil": 'sqs-destino-2',
    "mcad": 'sqs-destino-3'
}

valor_secreto = {}

def lambda_handler(event, context):
    mensajes = json.loads(json.dumps(event))
    for mensaje in mensajes['Records']:
        info_destino = procesa_mensaje(mensaje['body'])
        encola_mensaje(info_destino)
        valor_secreto = obtiene_secreto()
        conecta_base()
        elimina_mensaje(mensaje)
    print(valor_secreto)
        
#Para efectos demostrativos
def procesa_mensaje(mensaje):
    queue_destino = ""
    resultado_origen = busca_en_json(json.loads(mensaje), "iniciador")
    for i,j  in destinos_dict.items():
        if resultado_origen == i:
            queue_destino = j
            return [resultado_origen, queue_destino]
    return ["Error", "Destino no encontrado"]
    
def encola_mensaje(info_destino):
    if info_destino[0] != "Error":
        sqs.send_message(
            QueueUrl=queue_url_destino_estructura + info_destino[1],
            DelaySeconds=10,
            MessageBody=(
                info_destino[0]
            )
        )
    else:
        sqs.send_message(
            QueueUrl=queue_deadletter,
            DelaySeconds=10,
            MessageBody=(
                info_destino[1]
            )
        )

def elimina_mensaje(mensaje):
    sqs.delete_message(
        QueueUrl=queue_url,
        ReceiptHandle=mensaje['receiptHandle']
    )

def busca_en_json(diccionario, parametro):
    k = None
    if diccionario.get(parametro) != None:
        k = diccionario.get(parametro)
        return k
    else:
        for i, j in diccionario.items():
            if type(j) == dict:
                k = busca_en_json(j, parametro)
                if k != None:
                    break
    return k

def obtiene_secreto():
    secret = ""
    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secreto_bd
        )
    except ClientError as e:
        print(e.response['Error']['Code'])
    else:
        if 'SecretString' in get_secret_value_response:
            secret = get_secret_value_response['SecretString']
        else:
            secret = base64.b64decode(get_secret_value_response['SecretBinary'])
    return json.loads(secret)
    
def conecta_base():
    try:
        conn = pymysql.connect(valor_secreto.get("host"), user=valor_secreto.get("username"), passwd=valor_secreto.get("password"), db="actas", connect_timeout=5)
        print(conn)
    except pymysql.MySQLError as e:
        logging.error("ERROR: Unexpected error: Could not connect to MySQL instance.")
        logging.error(e)
        sys.exit()
    
    logging.info("SUCCESS: Connection to RDS MySQL instance succeeded")



    