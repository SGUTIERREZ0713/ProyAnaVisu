import traceback
import pandas as pd
from datetime import datetime

def transformar_servicios (servicios):

    try: 
        
        servicios['now'] = datetime.now()

        return servicios

    except:
        traceback.print_exc()
    finally:
        pass
