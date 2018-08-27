#this .py is used to check the carton_type_code
import json
import pandas as pd
def check_carton_type_code(json_file):
    #read and decompose the carton_info
    f=open(json_file)
    carton_number=json.load(f)
    # carton_owner=carton_number['carton_owner']
    # carton_code=carton_number['carton_code']
    # verification=carton_number['verification']
    carton_type_code=carton_number['carton_type_code']
    # print(type(carton_owner))
    # print(carton_code)
    # print(verification)
    # print(carton_type_code)
    carton_type_code_file = 'carton_type_code.csv'
    carton_owner_code_list=pd.read_csv(carton_type_code_file)
    carton_owner_code_list=list(carton_owner_code_list['TOR_IYC_ISOCD'])
    if carton_type_code in carton_owner_code_list:
        return 0 #carton_type_code is right
    else:
        return 1 #carton_type_code is wrong
# print(check_carton_type_code('carton_info.json'))