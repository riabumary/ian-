my_list = []
my_list.extend = ([10,20,30,40])
my_list.insert = (1, 15)
my_list.extend = ([50,60,70])
my_list.remove(-1)
# sort my_list in ascending order
my_list.sort()
index_30 = my_list.index(30)
print("index of 30in my_list:",index_30)

# print final list
print("final list:", my_list)
