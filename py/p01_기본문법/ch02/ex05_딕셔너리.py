my_dict = {
    "name":"Harry",
    "age": 27,
    "height": 190,
    "weight" : 99.9
}

print(my_dict)
print(my_dict.keys())
print(my_dict.values())
print(my_dict['age'])
my_dict['age']=55
print(my_dict['age'])
my_dict.update({'weight':100})
print(my_dict)
my_dict.update({'address':'Busan'})
print(my_dict)
my_dict['address'] = 'Seoul'
print(my_dict)
my_dict['hobby'] = 'fishing'
print(my_dict)
# print(my_dict.pop('address', None))
# print(my_dict)
# _,a = my_dict.popitem()
# print(my_dict)
# print(a)

for key in my_dict.keys():
    print(f'{key}: {my_dict[key]}')

print(list(my_dict.keys())[3])

print(my_dict.items())

for key, value in my_dict.items():
    print(f'{key}: {value}')
