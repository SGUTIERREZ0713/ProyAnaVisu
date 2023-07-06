import traceback
import pandas as pd

def extraer_departamentos ():

    try: 
        
        filename = '/home/proyecto/BaseDeDatos/departamentos.csv'

        departamentos = pd.read_csv(filename)

        return departamentos

    except:
        traceback.print_exc()
    finally:
        pass
