import pandas as pd
from database import Database
data = pd.HDFStore('/Users/fakram/Downloads/results_dvrpc_run_335_run_results.h5',mode = 'r')

type(data)
#load dataframe into postgreSQL using Database.py 


db = Database()
#db.import...