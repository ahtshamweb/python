'''

dic = {
    'name':'karan',
    'age':19,
    'Roll_No':2597
};

print(dic);


# Access Single Value
print(dic['name']);
print(dic.get('eligible'));

#  Accessing Multiple Values
print(dic.values());

# Accessing Keys
print(dic.keys());

# Accesssing key-values pairs:
print(dic.items());


'''
# ***************************** Dictionary Method **********************

ep1 = {122: 45, 123: 89, 567: 69, 670: 69};
ep2 = {222: 67, 566: 90};

ep1.update(ep2);
# print(ep1);


info = {'name':'Karan', 'age':19, 'eligible':True};
# print(info);
info.update({'age':20});
info.update({'DOB':2001});
# print(info);


# Removing Items From Dictionary:


info1 = {'name':'Karan', 'age':19, 'eligible':True};
# info1.clear();
# info1.pop('eligible');
# info1.popitem();
del info1['age'];
# del info1;
print(info1);


