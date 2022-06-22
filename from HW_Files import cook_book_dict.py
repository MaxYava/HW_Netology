some_list = []
fin_list = []
cook = {}
cook_fin = {}
cook_book = {'Омлет': ['Яйцо | 2 | шт', 'Молоко | 100 | мл', 'Помидор | 2 | шт']}
for di in (cook_book.values()):
    for el in di:
        ind = str(id)
        a = ''.join(el)
        b = a.replace('|', '')
        c = b.split()

        cook['ingridient_name'] = c[0]
        cook['quantity'] = c[1]
        cook['measure'] = c[2]
        some_list.append(cook)
       
       

print(some_list)
dop_cook_dict = {}
                dish_list = []
                for line in cook_book.values():
      
                    for name in line:
                        ingr = name[0]
                        qua = name[1]
                        meas = name[2]
                        dop_cook_dict['ingridient_name'] = ingr
                        dop_cook_dict['quantity'] = qua
                        dop_cook_dict['measure'] = meas.strip()
                        fin_cook[dish] = dop_cook_dict
                    data.readline()
       
    dop_cook_dict = {}
    dish_list = []
    for line in cook_book.values():
      
        for name in line:
            ingr = name[0]
            qua = name[1]
            meas = name[2]
            dop_cook_dict['ingridient_name'] = ingr
            dop_cook_dict['quantity'] = qua
            dop_cook_dict['measure'] = meas.strip()
            
            dish_list.append(dop_cook_dict)
            print(dop_cook_dict)
            














#cook_book = {'Омлет': ['Яйцо | 2 | шт', 'Молоко | 100 | мл', 'Помидор | 2 | шт']}

#for ol in cook_book.values():
 #   for ingr_name, qua, meas in ol:
  #      print(ingr_name, qua, meas)