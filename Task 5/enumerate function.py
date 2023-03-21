num_list = [23,34,56,41,67,88,99]
for index,element in enumerate(num_list):
    print(index,element)
    
names = ["Fatima", "Noor", "Mahjabeen", "Menahil"]
indexed_names = []
for i, name in enumerate(names):
    index_name = (i,name)
    indexed_names.append(index_name)
print(indexed_names)

indexed_names_friends = [(i,name) for i,name in enumerate(names)]
print(indexed_names_friends)
