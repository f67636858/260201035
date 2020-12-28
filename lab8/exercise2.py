def is_prime(number):
  is_prime_number = True
  if number <2 :
    return False
  elif number == 2:
    return True
  else:
    for x in range(2,number):
      if number % x == 0:
        is_prime_number = False
        break
  return is_prime_number


def print_primes_between(num_01,num_02):
  for x in range(num_01,num_02+1):
    if is_prime(x):
      print(x)


print(is_prime(10))
print_primes_between(1,25)

