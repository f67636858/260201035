import random
def get_rand_list(b,e,n):  
  random_list= list(random.sample(range(b,e+1),n))
  return random_list

def get_overlap(b,e,N):
  random_set_01 = set(get_rand_list(b,e,N))
  random_set_02 = set(get_rand_list(b,e,N))

  return random_set_01.intersection(random_set_02)

print(get_overlap(0,10,5))
