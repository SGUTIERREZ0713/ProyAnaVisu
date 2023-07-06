  GNU nano 6.2                     ext_refugiados.py                               
import traceback
from sqlalchemy import create_engine
import pandas as pd

def extraer_servicios():
    try:
        host = 'localhost'
        port = '3306'
        user = 'root'
        pwd = 'password'
        db = 'NRC'

        # Crear el objeto de conexión utilizando SQLAlchemy
        conn_str = f'mysql+mysqlconnector://{user}:{pwd}@{host}:{port}/{db}'
        engine = create_engine(conn_str)

        # Leer los datos de la tabla 'country'
        servicios = pd.read_sql('SELECT * FROM servicios', con=engine)
        return servicios

    except:
        traceback.print_exc()

    finally:
        pass


