import re
inp_str = "Hey readers, we all are here be 45the time 1!"


print("Original string : " + inp_str)

num = re.findall(r'\d+', inp_str)

print(num)
