
user_email_adress = (input("Enter your email_adress : ")).lower().split("@")

first_part = user_email_adress[0].replace(".","")

if first_part == "ceng113" and user_email_adress[1] =="example.com":
  print(True)
else:
  print(False)



