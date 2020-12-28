def binary_to_dec(binary):
  decimal = 0
  exponential = 0
  binary = binary[::-1]
  for digit in binary:
    decimal += int(digit) * (2** exponential)
    exponential += 1
  return decimal

def dec_to_binary(decimal):
  list_of_binary = []
  while decimal != 0 :
    remain = decimal % 2
    decimal = decimal // 2
    list_of_binary.append(remain)
  list_of_binary.reverse()
  list_of_binary = list(map(str,list_of_binary))
  return "".join(list_of_binary)

print(binary_to_dec("101001"))
print(dec_to_binary(17))

