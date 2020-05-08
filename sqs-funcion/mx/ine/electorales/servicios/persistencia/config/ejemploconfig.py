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

import mysql.connector
"""
	TODO [Agregar documentacion de la clase]
	nombre= 
	funcion_principal= 
	author= Beverido Castellanos Julio Andrés (julio.beverido@ine.mx)
	version= 1.0.0
	tags=
"""
class EjemploConfig:
	"""
		TODO [Agregar documentacion al método]
		nombre= 
		funcion_principal=
		parámetros= 
		retorno= 
		author= Beverido Castellanos Julio Andrés (julio.beverido@ine.mx)
		tags=
	"""
	def obtiene_conexion(self):
		mydb = mysql.connector.connect(
			host = 'localhost', 
			user = 'root', 
			passwd = 'admin', 
			database = 'dbtest')
		return mydb