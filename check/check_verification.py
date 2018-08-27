#this .py is used to check the verification
import json
import check_carton_number
import check_carton_owner
import change_carton_char_to_number
def check_verification(json_file):
    #first to finish the check of carton_number, carton_owner
    carton_number_result=check_carton_number.check_carton_number(json_file)
    carton_owner_result=check_carton_owner.check_carton_owner(json_file)
    if carton_number_result==0 and carton_owner_result==0:#if carton_number and carton_owner are both right
        f = open(json_file)
        carton_number = json.load(f)
        carton_owner = carton_number['carton_owner']
        carton_code = carton_number['carton_code']
        verification = carton_number['verification']
        # carton_type_code=carton_number['carton_type_code']
        #decompose the carton_owner and carton_code
        carton_owner_list=[x for x in carton_owner]
        carton_code_list = str(carton_code)
        #sum the results of changing item from carton_owner_list and carton_code_list according to their orders
        # print(carton_owner_list)
        # print(carton_code_list)
        # print(sum_of_carton_owner_list_and_carton_code_list(carton_owner_list,carton_code_list))
        if sum_of_carton_owner_list_and_carton_code_list(carton_owner_list,carton_code_list)==verification:
            return 0#verification is right
        else:
            return 2#verification is wrong
        # change_carton_char_to_number
    else:
        return 1#carton_number or carton_owner is wrong, the verification is wrong
    #read and decompose the carton_info
def sum_of_carton_owner_list_and_carton_code_list(carton_owner_list,carton_code_list):
    information_of_changed_carton_owner_list=[change_carton_char_to_number.change_carton_char_to_number(carton_owner_list[item])*(2**item) for item in range(0,len(carton_owner_list))]
    information_of_changed_carton_code_list=[change_carton_char_to_number.change_carton_char_to_number(carton_code_list[item]) * (2 ** (item+len(carton_owner_list))) for item in range(0, len(carton_code_list))]
    # print(information_of_changed_carton_owner_list)
    # print(information_of_changed_carton_code_list)
    # print(sum(information_of_changed_carton_owner_list)+sum(information_of_changed_carton_code_list))
    return (sum(information_of_changed_carton_owner_list)+sum(information_of_changed_carton_code_list))% 11

print(check_verification('carton_info.json'))