import random
from faker import Faker
import mysql.connector
import datetime
from faker.providers import barcode

# Configuración de la conexión a la base de datos
config = {
    'user': 'root',
    'password': 'password',
    'host': 'localhost',
    'database': 'NRC',
    'raise_on_warnings': True
}

# Crear una conexión a la base de datos
conn = mysql.connector.connect(**config)
cursor = conn.cursor()

# Crear registros de ejemplo utilizando Faker y agregarlos a la tabla
fake = Faker()
fake.add_provider(barcode)

# CREACION TABLA DONANTES
#cursor.execute("CREATE TABLE IF NOT EXISTS donantes (id_donantes INT AUTO_INCREMENT PRIMARY KEY, nombre VARCHAR(50))")
#cursor.execute("DROP TABLE IF EXISTS donantes")
cursor.execute("CREATE TABLE IF NOT EXISTS donantes (id_donantes INT AUTO_INCREMENT PRIMARY KEY, nombre VARCHAR(50))")

# Crear registros de ejemplo utilizando Faker y agregarlos a la tabla
def donantes():
    # Aquí puedes definir tu lógica para generar el dato personalizado
    donante = ['ACNUR', 'FMSA', 'HILTON', 'NRC', 'GOBIERNO']
    return donante
    
for _ in range (5):
    donante = donantes()
    nombre = fake.random_element(donante)
    cursor.execute("INSERT INTO donantes (nombre) VALUES (%s)", (nombre,))


#CREACION TABLA PROYECTOS
#cursor.execute("CREATE TABLE  proyectos (id INT AUTO_INCREMENT PRIMARY KEY, servicio VARCHAR(50), localidad VARCHAR(50), donante  VARCHAR(10))")
#cursor.execute("DROP TABLE IF EXISTS proyectos")
cursor.execute("CREATE TABLE  proyectos (id_proyectos INT AUTO_INCREMENT PRIMARY KEY, servicio VARCHAR(50), localidad VARCHAR(50), donante  VARCHAR(10), meses char(2))")

def localidades():
    localidad = ['Quito', 'San Lorenzo', 'Ibarra', 'Ambato', 'Guayaquil', 'Tulcan', 'Esmeraldas', 'Huaquillas', 'El coca', 'Cuenca', 'Manta', 'Sto Domingo' ]
    return localidad

# Crear registros de ejemplo utilizando Faker y agregarlos a la tabla
def servicios():
    # Aquí puedes definir tu lógica para generar el dato personalizado
    servicio = ['Educacion', 'FSL', 'ICLA', 'Vivienda', 'Asistencia']
    return servicio

for _ in range(50):
    servicio = servicios()
    servicio = fake.random_element(servicio)
    localidad = localidades()
    localidad = fake.random_element(localidad)
    donante = donantes()
    donante = fake.random_element(donante)
    meses = fake.random_int(min=1, max=48)
    cursor.execute("INSERT INTO proyectos (servicio, localidad, donante, meses) VALUES (%s, %s, %s, %s)", (servicio, localidad, donante, meses))

#CREACION TABLA EMPLEADOS
#cursor.execute("DROP TABLE IF EXISTS empleados")
cursor.execute("CREATE TABLE IF NOT EXISTS empleados (id_empleados INT AUTO_INCREMENT PRIMARY KEY, nombre VARCHAR(50), localidad VARCHAR(50), departamento VARCHAR(50), CODIGO VARCHAR(10), donante VARCHAR(10))")

def departamentos():
    departamento = ['RRHH', 'ICLA', 'MONITOREO', 'LOGISTICA', 'SOPORTE', 'EDUCACION']
    return departamento

for _ in range(50):
    random_number = random.randint(0, 1)
    if random_number == 0:
        # Si el número es 0, generar un nombre masculino
        nombre = fake.first_name_male()
        sexo = 'Masculino'
    else:
        # Si el número es 1, generar un nombre femenino
        nombre = fake.first_name_female()
        sexo = 'Femenino' 
    localidad = localidades()
    localidad = fake.random_element(localidad)
    departamento = departamentos()
    departamento = fake.random_element(departamento)
    codigo = fake.ean(length=8)
    donante = donantes()
    donante = fake.random_element(donante)
    cursor.execute("INSERT INTO empleados (nombre, localidad, departamento, codigo, donante) VALUES (%s, %s, %s, %s, %s)", (nombre, localidad, departamento, codigo, donante))

#CREACION TABLA SERVICIOS
#cursor.execute("CREATE TABLE servicios (id_servicios INT AUTO_INCREMENT PRIMARY KEY)")
#cursor.execute("DROP TABLE IF EXISTS servicios")
#cursor.execute("CREATE TABLE servicios (id_servicios INT AUTO_INCREMENT PRIMARY KEY, nombre VARCHAR(50), fechaInicio DATE, id_proyectos INT, FOREIGN KEY (id_proyectos REFERENCES proyectos (id_proyectos), id_donantes INT, FOREIGN KEY (id_donantes) REFERENCES donantes (id_donantes))")
cursor.execute("CREATE TABLE servicios (id_servicios INT AUTO_INCREMENT PRIMARY KEY, nombre VARCHAR(50), fechaInicio DATE, id_proyectos INT, FOREIGN KEY (id_proyectos) REFERENCES proyectos(id_proyectos), id_donantes INT, FOREIGN KEY (id_donantes) REFERENCES donantes (id_donantes))")

# Definir una función para generar datos personalizados
def servicios():
    # Aquí puedes definir tu lógica para generar el dato personalizado
    servicio = ['Educacion', 'FSL', 'ICLA', 'Vivienda', 'Asistencia']
    return servicio

for _ in range(5):
    servicio = servicios()
    nombre = fake.random_element(servicio)
    # Obtener la fecha actual
    fecha_actual = datetime.date.today()
    # Generar una fecha aleatoria en los últimos 5 años
    fechaInicio = fecha_actual - datetime.timedelta(days=365 * 5)
    cursor.execute("INSERT INTO servicios (nombre, fechaInicio) VALUES (%s, %s)", (nombre, fechaInicio))

#CREACION TABLA BENEFICIARIOS
#cursor.execute("DROP TABLE IF EXISTS beneficiarios")
#cursor.execute("CREATE TABLE beneficiarios (id_beneficiarios INT AUTO_INCREMENT PRIMARY KEY, nombre VARCHAR(50), sexo VARCHAR(10), edad CHAR(2), nacionalidad VARCHAR(50), fechaIngreso DATE, identificacion CHAR(10), id_servicio INT, FOREIGN KEY (id_servicio) REFERENCES (servicios(id_servicios))")
cursor.execute("CREATE TABLE beneficiarios (id_beneficiarios INT AUTO_INCREMENT PRIMARY KEY, nombre VARCHAR(50), sexo VARCHAR(10), edad CHAR(2), nacionalidad VARCHAR(100), fechaIngreso DATE, identificacion CHAR(10), id_servicio INT, FOREIGN KEY (id_servicio) REFERENCES servicios(id_servicios))")

for _ in range(50):
    random_number = random.randint(0, 1)
    if random_number == 0:
        # Si el número es 0, generar un nombre masculino
        nombre = fake.first_name_male()
        sexo = 'Masculino'
    else:
        # Si el número es 1, generar un nombre femenino
        nombre = fake.first_name_female()
        sexo = 'Femenino'
    # Generar una fecha de nacimiento aleatoria en los últimos 80 años
    fecha_nacimiento = fake.date_of_birth(minimum_age=1, maximum_age=80)
    # Calcular la edad en base a la fecha de nacimiento
    hoy = datetime.date.today()
    edad = hoy.year - fecha_nacimiento.year
    nacionalidad = fake.country()
    # Obtener la fecha actual
    fecha_actual = datetime.date.today()
    # Generar una fecha aleatoria en los últimos 20 años
    fecha_inicio = fecha_actual - datetime.timedelta(days=365 * 20)
    # Restar 20 años a la fecha actual
    fechaIngreso = fake.date_between(start_date=fecha_inicio, end_date=fecha_actual)
    # Generar un número de 10 dígitos
    identificacion = fake.random_number(digits=10)
    cursor.execute("INSERT INTO beneficiarios (nombre, sexo, edad, nacionalidad, fechaIngreso, identificacion) VALUES (%s, %s, %s, %s, %s, %s)", (nombre, sexo, edad, nacionalidad, fechaIngreso, identificacion)) 



# Guardar los cambios en la base de datos
conn.commit()

# Mostrar los registros agregados
#cursor.execute("SELECT * FROM beneficiarios")
#print("Registros en la tabla beneficiarios:")
#for (id, nombre, nacionalidad, fechaIngreso, identificacion) in cursor:
#    print(f"ID: {id}, Nombre: {nombre}, Nacionalidad: {nacionalidad}, Fecha Ingreso: {fechaIngreso}, Identificacion: {identificacion}")

#cursor.execute("SELECT * FROM proyectos")
#print("Registros en la tabla proyectos:")
#for (id, servicio, localidad, donante) in cursor:
#    print(f"ID: {id}, Localidad: {localidad}, Servicio: {servicio}, Donante: {donante}")


# Cerrar la conexión a la base de datos
cursor.close()
conn.close()
