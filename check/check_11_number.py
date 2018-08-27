#this .py this used to check the 11 number
import json
import check_carton_number
import check_carton_owner
import check_carton_type_code
import change_carton_char_to_number
import check_verification
def check_11_number(json_file):
    carton_owner_result=check_carton_owner.check_carton_owner(json_file)
    carton_number_result=check_carton_number.check_carton_number(json_file)
    verification_result=check_verification.check_verification(json_file)
    carton_type_code_result=check_carton_type_code.check_carton_type_code(json_file)
    return [carton_owner_result,carton_number_result,verification_result,carton_type_code_result]

print(check_11_number('carton_info.json'))