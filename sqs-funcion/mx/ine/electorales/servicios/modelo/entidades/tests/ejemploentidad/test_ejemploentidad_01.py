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
import pytest
from ...ejemploentidad.ejemploentidad import EjemploEntidad
"""
	TODO [Agregar documentacion de la clase]
	nombre= 
	funcion_principal= 
	author= Beverido Castellanos Julio Andrés (julio.beverido@ine.mx)
	version= 1.0.0
	tags=
"""
class TestEjemploEntidad01:
	"""
		TODO [Agregar documentacion al método]
		nombre= 
		funcion_principal=
		parámetros= 
		retorno= 
		author= Beverido Castellanos Julio Andrés (julio.beverido@ine.mx)
		tags=
	"""
	def test_realiza_mapeo(self):
		ejemplo_1 = EjemploEntidad()
		assert ejemplo_1.realiza_mapeo() == "<br>EjemploEntidad: Mapeo de entidad realizado"