import traceback

from ext_departamentos import  extraer_departamentos
from ext_donantes import extraer_donantes
from ext_empleados import extraer_empleados
from ext_oficinas import extraer_oficinas
from ext_proyectos import extraer_proyectos
from ext_refugiados import extraer_beneficiarios
from ext_servicios import extraer_servicios
from trans_departamentos import transformar_departamentos
from trans_donantes.py import transformar_donantes
from trans_servicios.py import transformar_donantes
from carg_departamentos import cargar_departamentos


try:
    print('Extraccion de Datos iniciadia')
    departamentos = extraer_departamentos
    donantes = extraer_donantes
    empleados = extraer_empleados
    oficinas = extraer_oficinas
    proyectos = extraer_proyectos
    beneficiarios = extraer_beneficiarios
    servicios = extraer_servicios
    print('TRansformacion de DAtos Iniciada')
    tdepartamentos = transformar_departamentos
    tdonantes = transformar_donantes
    tservicios = transformar_servicios
    print('Carga de Datos')
    cdepartamentos = cargar_departamentos

except:
    traceback.print_exc()
finally:
    pass
