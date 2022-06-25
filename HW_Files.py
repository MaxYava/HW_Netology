import os
from pprint import pprint


LOG_CATALOG_NAME = "files"
LOG_FILE_NAME = "File_Menu.txt"
BASE_PATH = os.getcwd()
full_path = os.path.join(BASE_PATH, LOG_CATALOG_NAME, LOG_FILE_NAME)


cook_book = {}
def cook_book_dict(file=full_path):
    cook_book = {}
    with open(full_path) as data:
        for line in data:
            dish = line.strip()
            nums = data.readline()
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
    

#pprint(cook_book_dict())

def get_shop_list_by_dishes(dishes, person_count):
    shop_dict = {}
    for el in dishes:
        if el in cook_book_dict().keys():
            step = cook_book_dict().get(el)
            for ingrs in step:
                ingr_1 = ingrs.get('ingridient_name')
                ingr_2 = ingrs.get('measure')
                ingr_3 = ingrs.get('quantity')
                sub_ingr = int(ingr_3)
                if person_count == 1:
                    fin_ingr = sub_ingr * len(dishes)
                else:
                    fin_ingr = sub_ingr * person_count
                sub_dict = {}
                sub_dict['measure'] = ingr_2
                sub_dict['quantity'] = fin_ingr
                shop_dict[ingr_1] = sub_dict
    return shop_dict

            
#pprint(get_shop_list_by_dishes(['Фахитос'], 2))



def fin_files():
    file_1 = "file_1.txt"
    file_2 = "file_2.txt"
    file_3 = "file_3.txt"
    result = "new_file.txt"
    files =  [file_1, file_2, file_3]
    file_dict = {}
    for id_file, file in enumerate(files, start=1):
        with open(file) as data_txt:
            text = data_txt.read()
        with open(file) as data:
            for id, line in enumerate(data, start=1):
                pass
            file_dict[id] = [file, str(id), text]  
    with open(result, 'a') as fin_file:
        for el in sorted(file_dict.keys()):
            fin_data = file_dict.get(el)
            for item in fin_data:
                fin_file.write(item)
                fin_file.write('\n')

        

#fin_files()            

