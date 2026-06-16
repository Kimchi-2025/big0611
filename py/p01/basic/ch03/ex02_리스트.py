import random

fruit_list = ['apple', 'banana', 'orange']

print(fruit_list[0])

fruit_list[0] = 'strawberry'
fruit_list.insert(1, 'water melon')
fruit_list.append('kiwi')
print(fruit_list)
print(len(fruit_list))

fruit_list.insert(3, 'durian')
print(fruit_list)
print(len(fruit_list))

vegetable_list = ['carrot', 'tomato', 'onion']
print(fruit_list + vegetable_list)
print(fruit_list)
print(vegetable_list)

list1 = [1,2,3,4,5]
list2 = ['가', '나', '다', '라', '마']
list3 = [list(x) for x in zip(list1, list2)]
list4 = list(zip(list1, list2))
list5 = list(map(list, zip(list1, list2)))
print(f'list3: {list3}')
print(f'list4: {list4}')
print(f'list5: {list5}')
print([x+10 for x in list1])
print(list(map(lambda x: x+10, list1)))


for item1, item2 in list3:
    print(f'item1: {item1} {type(item1)} / item2: {item2} {type(item2)}')

print(list4)
unzip1, unzip2 = zip(*list4)
print(list(unzip1))
print(list(unzip2))

# print(vegetable_list)
# fruit_list.extend(vegetable_list)
# print(fruit_list)

list2 = ['나', '라', '다', '가', '마']
print(list2)

list2.sort(reverse=True)
print(list2)

random.shuffle(list2)
print(list2)
