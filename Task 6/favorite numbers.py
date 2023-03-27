fav_num = {
    'Duaa': '13',
    'Noor': '16',
    'Mahnoor': '20000000',
    'Mahrukh': '0',
    'Fatima': '-8'
    }
for name, number in fav_num.items():    #key value pair
    print(name+'\'s favorite number is', number + '.')
print(fav_num.keys())   #returns keys
new_fav = fav_num.copy()    #copy of dictionary
print(new_fav.items())  #key value pair
new_fav.popitem()   #removes last pair
print(new_fav)