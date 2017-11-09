import MySQLdb

class base_datos(object):
	def insertar_matricula(self,cedula_alumno,id_asignatura,nota):
		try:

			bd = MySQLdb.connect("localhost","root","123","academia")
			cursor = bd.cursor()
			sql ="INSERT INTO matricula values(%s,%s,%s) " %(cedula_alumno,id_asignatura,nota)

		except:
			print "error de conexcion"
			return
		
		try:
			cursor.execute(sql)
			bd.commit()
			print "datos guardados con exito!"
			
		except:
			print "error al insertar los datos"
		bd.close()

	def insertar_asignatura(self,nombre,cedula_profesor):
		try:

			bd = MySQLdb.connect("localhost","root","123","academia")
			cursor = bd.cursor()
			sql ="INSERT INTO asignatura(nombre,cedula_profesor) VALUES('%s','%s') " %(nombre,cedula_profesor)
			

		except:
			print "error de conexcion"
			return
		
		
		try:
			cursor.execute(sql)
			bd.commit()
			print "datos guardados con exito!"
			
		except:
			print "error al insertar los datos"

		bd.close()
	def insertar_alumnos(self,cedula,nombre):
		try:

			bd = MySQLdb.connect("localhost","root","123","academia")
			cursor = bd.cursor()
			sql ="INSERT INTO alumno (cedula,nombre)VALUES('%s','%s') " %(cedula,nombre)
			

		except:
			print "error de conexcion"
			return
		
		
		try:
			cursor.execute(sql)
			bd.commit()
			print "datos guardados con exito!"
		
		except:
			print "error al insertar los datos"
		bd.close()


bd = base_datos()
bd.insertar_alumnos("Orlando")








		
	
		