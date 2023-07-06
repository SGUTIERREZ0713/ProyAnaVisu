import traceback
import pandas as pd
from datetime import datetime

def transformar_donantes (donantes):

    try: 
        
        donantes['pais'] = ('EEUU')

        return donantes

    except:
        traceback.print_exc()
    finally:
        pass
