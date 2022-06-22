some_list = []
fin_list = []
cook = {}
cook_fin = {}
cook_book = {'Омлет': ['Яйцо | 2 | шт', 'Молоко | 100 | мл', 'Помидор | 2 | шт']}
for di in (cook_book.values()):
    for id, el in di:
        ind = str(id)
        a = ''.join(el)
        b = a.replace('|', '')
        c = b.split()

        cook['ingridient_name'] = c[0]
        cook['quantity'] = c[1]
        cook['measure'] = c[2]
        some_list.append(cook)
       
       

print(some_list)













#cook_book = {'Омлет': ['Яйцо | 2 | шт', 'Молоко | 100 | мл', 'Помидор | 2 | шт']}

#for ol in cook_book.values():
 #   for ingr_name, qua, meas in ol:
  #      print(ingr_name, qua, meas)