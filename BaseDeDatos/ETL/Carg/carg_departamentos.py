import traceback
from util.db_conn import Db_Connection
import psycopg2
import pandas as pd
from sqlalchemy import teimport traceback
from sqlalchemy import create_engine
import pandas as pd

def cargar_beneficiarios():
    try:
        host = 'localhost'
        port = '3306'
        user = 'root'
        pwd = 'password'
        db = 'NRC'

        # Crear el objeto de conexión utilizando SQLAlchemy
        conn_str = f'mysql+mysqlconnector://{user}:{pwd}@{host}:{port}/{db}'
        engine = create_engine(conn_str)
    
        # Leer los datos de la tabla ext_category en un dataframe
        data = pd.read_sql("SELECT id_beneficiarios, name FROM ext_beneficiarios", ses_db_stg)

        # Renombrar las columnas del DataFrame para que coincidan con los nombres de columna de la tabla en la base de datos de destino
        data = data.rename(columns={"id_beneficiarios": "cat_bus_id", "name": "nombre"})

        # Crear TABLA temporAL en sor_dvdrental
        sql_temp = text("""
        CREATE TABLE IF NOT EXISTS temp_beneficiarios (
            CAT_BUS_ID INTEGER NOT NULL,
            NOMBRE VARCHAR(100) NOT NULL
        )
    """)
        with ses_db_sor.begin() as conn:
            conn.execute(sql_temp)

        #Caraga de datos al la tabla temporal
        data.to_sql('temp_categoria', ses_db_sor, schema='public', if_exists='replace', index=False, method='multi', chunksize=1000)

        sql_sentence = text("MERGE INTO public.dim_categoria car_ca USING (SELECT cat_bus_id, nombre FROM public.temp_categoria) AS ext_ca ON car_ca.cat_bus_id = ext_ca.cat_bus_id WHEN MATCHED THEN UPDATE SET nombre = ext_ca.nombre WHEN NOT MATCHED THEN INSERT (cat_bus_id, nombre) VALUES (ext_ca.cat_bus_id, ext_ca.nombre)")
        with ses_db_sor.begin() as conn:
            conn.execute(sql_sentence)

        #Borrar tabla temporal
        sql_drop_temp = text("DROP TABLE IF EXISTS temp_categoria;")
        with ses_db_sor.begin() as conn:
            conn.execute(sql_drop_temp)

    except:
        traceback.print_exc()
    finally:
        con_db_stg.stop()
        con_db_sor.stop()
