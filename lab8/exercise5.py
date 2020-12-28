def password_checker(password):
  if " " in password or len(password) < 8:
    return "Level 0"
  elif password.isalpha() or password.isnumeric():
    return "Level 1"
  else:
    is_special_char = False
    is_alpha = False
    is_numeric = False
    for letter in password:
      if letter.is_alpha():
        is_alpha = True
      elif letter.is_numeric():
        is_numeric = True
      else:
        is_special_char = True
    #All of them are bollean expression
    list_of_condition = [is_alpha,is_numeric,is_special_char]
    if is_numeric and is_alpha and is_special_char:
      return "Level 3"
    elif False in list_of_condition:
      return "Level 2"

def main():
  result = ""
  while result != "Level 3" :
    password = input("Enter the Password : ")
    result = password_checker(password)
    print(result)

main()