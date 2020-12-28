def get_reversed(list_of_number):
  if len(list_of_number) ==0:
    return []
  else:
    return list_of_number[-1] + get_reversed[:-1]