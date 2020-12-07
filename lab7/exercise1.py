my_list_of_tuple = [("Jon",15), ("Ned",45), ("Arya",9), ("Catelyn",44), ("Bran",10)]

index = 0
while index<len(my_list_of_tuple):
  if my_list_of_tuple[index][1] >18:
    print (my_list_of_tuple[index][0])
  index += 1
