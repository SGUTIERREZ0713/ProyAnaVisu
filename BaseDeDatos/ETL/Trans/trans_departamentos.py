import traceback
import pandas as pd
from datetime import datetime

def transformar_departamentos (departamentos):

    try: 
        
        departamentos['now'] = datetime.now()

        return departamentos

    except:
        traceback.print_exc()
    finally:
        pass
