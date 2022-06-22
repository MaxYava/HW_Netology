import os
from pprint import pprint
from re import A
LOG_CATALOG_NAME = "files"
LOG_FILE_NAME = "File_Menu.txt"
BASE_PATH = os.getcwd()
full_path = os.path.join(BASE_PATH, LOG_CATALOG_NAME, LOG_FILE_NAME)
#print(full_path)


def cook_book_dict(file=full_path):
    cook_book = {}
    
    with open(full_path) as data:
        for line in data:
            dish = line.strip()
            nums = data.readline()
            ingr_list = []
            fin_list = []
            for item in range(int(nums)):
                ingr = data.readline()
                new_ingr = ingr.split('|')
                sub_dict = {}
                sub_dict['ingridient_name'] = new_ingr[0]
                sub_dict['quantity'] = new_ingr[1]
                sub_dict['measure'] = new_ingr[2].strip()

              
                fin_list.append(sub_dict)
                cook_book[dish] = fin_list
                data.readline()
        return cook_book
    

pprint(cook_book_dict())