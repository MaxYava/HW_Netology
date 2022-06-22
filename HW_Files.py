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
            for item in range(int(nums)):
                ingr = data.readline()
                ingr_list.append(ingr.strip())
                
            cook_book[dish] = ingr_list
            data.readline()
        return cook_book
        #return cook_book
    #for dish, ingr in cook_book.items():
     #   a = ' '.join(ingr)
        
        
      #  print(dish, a.replace("|", ''))

    #pprint(cook_book)


pprint(cook_book_dict())

##def fin_dict(file=full_path):
    #ith open(full_path) as menu:
        