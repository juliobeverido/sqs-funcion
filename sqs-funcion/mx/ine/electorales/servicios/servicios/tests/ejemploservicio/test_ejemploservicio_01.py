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
from ...ejemploservicio.ejemploservicio import EjemploServicio
"""
	TODO [Agregar documentacion de la clase]
	nombre= 
	funcion_principal= 
	author= Beverido Castellanos Julio Andrés (julio.beverido@ine.mx)
	version= 1.0.0
	tags=
"""
class TestEjemploServicio01:
	"""
		TODO [Agregar documentacion al método]
		nombre= 
		funcion_principal=
		parámetros= 
		retorno= 
		author= Beverido Castellanos Julio Andrés (julio.beverido@ine.mx)
		tags=
	"""
	def test_ejecuta_algoritmo(self):
		ejemplo_1 = EjemploServicio()
		assert ejemplo_1.ejecuta_algoritmo() == "Este test va a fallar"