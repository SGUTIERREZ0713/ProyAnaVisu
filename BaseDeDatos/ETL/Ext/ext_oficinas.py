import traceback
import pandas as pd

def extraer_oficinas ():

    try: 

        filename = '/home/proyecto/BaseDeDatos/oficinas.csv'

        oficinas = pd.read_csv(filename)

        return oficinas

    except:
        traceback.print_exc()
    finally:
        pass





