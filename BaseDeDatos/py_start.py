import traceback

from ext_departamentos import  extraer_departamentos
from ext_donantes import extraer_donantes
from ext_empleados import extraer_empleados
from ext_oficinas import extraer_oficinas
from ext_proyectos import extraer_proyectos
from ext_refugiados import extraer_beneficiarios
from ext_servicios import extraer_servicios

try:
    print('Extraccion de Datos iniciadia')
    departamentos = extraer_departamentos
    donantes = extraer_donantes
    empleados = extraer_empleados
    oficinas = extraer_oficinas
    proyectos = extraer_proyectos
    beneficiarios = extraer_beneficiarios
    servicios = extraer_servicios
    

except:
    traceback.print_exc()
finally:
    pass
