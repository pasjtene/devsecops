import math

my_list = [i for i in range(1,10)]
print (my_list)

print("Test 2")

for i in my_list:
    if i == 5:
        pass
    else:
        print(i)
        
print("test 3")

for i in my_list:
    if i == 6:
        break
    else:
        print(i)
        
print("Test 4")

for i in my_list:
    if i == 7:
        continue
    else:
        print(i)
        
my_num = 23.345

print("test 5")
print(math.floor(my_num))
print(math.ceil(my_num))

print("test 6 dictionary comprehension")

my_dict = {i:i+7 for i in range(1,10)}
print(my_dict)

del my_list

print("test 6")
print(my_list)