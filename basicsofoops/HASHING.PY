'''
my_dict={'dave':'001','ava':'002',1:'003'}
print(my_dict)
new_dict=dict(dave='001',ava='002',a='swami')
print(new_dict)

#nested dictionary
emp_details={'employee':{'dev':{'id':'002','salary':'2000','Designation':'teamlead'},
                        'Ava':{'id':'002','salary':'1000','Designation':'manager'} }}
print(emp_details)
#performing operations on hash tables
print(my_dict['dave'])
print(my_dict.keys())
print(my_dict.values())
print(my_dict.get('ava'))
for x in my_dict:
    print(x)
for x in my_dict.values():
    print(x)
for x,y in my_dict.items():
    print(x,y)
#update value in dict
my_dict['dave']='004'
my_dict['chris']='003'
print(my_dict)
#delete
my_dict.pop('ava')
print(my_dict)
my_dict.popitem()
print(my_dict)
del my_dict['dave']
print(my_dict)
#data frame dict to df
import pandas as pd
df=pd.DataFrame(emp_details['employee'])
print(df)

'''

'''print(ord("a"))
print(ord("o"))
print(ord("b"))'''
'''def hash_function(value):
    sum_of_chars = 0
    for char in value:
        sum_of_chars += ord(char)

    return sum_of_chars % 10
my_array = ['Pete', 'Jones', 'Lisa', 'Bob', 'Siri']
print("'Bob' has hash code:",hash_function('Bob'))'''
value=['a','b','c']
a=sum(ord(char) for char in value) % 10
print(a)

print(ord("a"))























