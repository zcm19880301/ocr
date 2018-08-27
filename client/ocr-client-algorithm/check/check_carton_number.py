#this .py is used to check the carton_number
import json
def check_carton_number(json_file):
    #read and decompose the carton_info
    f=open(json_file)
    carton_number=json.load(f)
    # carton_owner=carton_number['carton_owner']
    carton_code=carton_number['carton_code']
    # verification=carton_number['verification']
    # carton_type_code=carton_number['carton_type_code']
    # print(type(carton_owner))
    # print(carton_code)
    # print(verification)
    # print(carton_type_code)
    if isinstance(carton_code,int):
        carton_code=str(carton_code)
        # print(carton_code)
        carton_code_list = [int(carton_code[item: item + 1]) for item in range(0, len(carton_code), 1)]
        if len(carton_code_list)==6:
            return 0
        else:
            return 2#if length of carton_code is not 6
    else:#if carton_code is not int
        return 1
# print(check_carton_number('carton_info.json'))