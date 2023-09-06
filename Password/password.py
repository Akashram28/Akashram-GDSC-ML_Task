import random
import string


upper_case = list(string.ascii_uppercase)
lower_case = list(string.ascii_lowercase)
nums = [str(i) for i in range(10)]
special = ['.', ',' , ':' , ';' ,'[' ,']' ,'`' , '~' ,'}' ,'{','+', '_' ,'=','-','|' ,'(' ,')','!','@','#','$','%','^','&','*','<' ,'>']

password = random.sample(upper_case,4) + random.sample(lower_case,4) + random.sample(nums,4) + random.sample(special,4)
random.shuffle(password)

print("New password : " + "".join(password))