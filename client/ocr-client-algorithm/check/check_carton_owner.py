#this .py is used to check the carton_owner
import json
import pandas as pd
def check_carton_owner(json_file):
    #read and decompose the carton_info
    f=open(json_file)
    carton_number=json.load(f)
    carton_owner=carton_number['carton_owner']
    # carton_code=carton_number['carton_code']
    # verification=carton_number['verification']
    # carton_type_code=carton_number['carton_type_code']
    # print(type(carton_owner))
    # print(carton_code)
    # print(verification)
    # print(carton_type_code)
    carton_owner_code_file = 'chixiangrendaima.csv'
    carton_owner_code=pd.read_csv(carton_owner_code_file)
    carton_owner_code=list(carton_owner_code['OWNER_CODE'])
    if carton_owner in carton_owner_code:
        return 0 #carton_owner is right
    else:
        return 1 #carton_owner is wrong
# print(check_carton_owner('carton_info.json'))