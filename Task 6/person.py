mahrukh = {
    'first name':'Mahrukh',
    'last name' : 'Muzammil',
    'age' : '20',
    'city' : 'Multan'
    }
print(mahrukh)
mahrukh['city'] = 'Lahore'  #Changing Item
print('The city Mahrukh lives in now is', mahrukh['city'])
mahrukh['birthday'] = '19/03/2003'  #Adding Item
print('Her birthday is on', mahrukh['birthday'])
del mahrukh['last name']   #Removing Item
print(mahrukh)

