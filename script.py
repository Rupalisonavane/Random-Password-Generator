import random

upper_char= ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
 
lower_char = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

num_list =['1','2','3','4','4','6','7','8','9','0']



passw = random.choice(upper_char)+random.choice(lower_char)+random.choice(lower_char)+random.choice(num_list)+ random.choice(upper_char)

print(passw)