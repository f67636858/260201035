password = "abc123"
while True:

  input_password = input("Enter password : ")
  if input_password == password :
    print("Welcome")
    break
  elif input_password.lower() == "help":
    print(password[0])
  else:
    print("Wrong") 
