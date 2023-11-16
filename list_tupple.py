list =[3,5,7,"Aht",True,456,90.9];


"""

print(list);
print(type(list));
print(list[1]);
print(list[-4]);

if 7 in list:
    print("Yes");
else:
    print("No");

if "Ha" in "Harry":
    print("Yes");

print(list[0:4]);



lst = [i*i for i in range(10)]
print(lst)



lst = [i*i for i in range(10) if i%2==0]
print(lst)



# Methods of Lists

l = [11, 45, 1, 2, 4, 6, 1, 1];
print(l);




l.append(7);
print(l);
l.sort()
print(l);
l.sort(reverse=True);
print(l);

print(l.index(1));

print(l.count(2));

m = l.copy();
m.append(2);
print(m);

m.insert(3,789);
print(m);

# for concatenation

j=m+l;
print(j);

j.pop(2);
print(j);

"""

"""
# *********************************************  Tuple  ******************************************************

'''
Tuples are ordered collection of data items. They store multiple items in a single variable.
 Tuple items are separated by commas and enclosed within round brackets (). 
Tuples are unchangeable meaning we can not alter them after creation.
'''

# tuple1 = (1,2,3,4,5,6);
# print(tuple1);
# details = ("Abhijeet", 18, "FYBScIT", 9.8)
# print(details)

tup =(1,2,3,76,342,32,"green",True);

print(tup[0]);
print(tup[7]);

if 342 in tup:
    print("yes");

tuple1 = (0, 1, 2, 3, 2, 31, 1, 3, 2, 3);
# res = tuple1.count(3);
# res = tuple1.index(3);
# res = tuple1.index(311);
# res = tuple1.index(3, 4, 8);
res = len(tuple1);
print('Count of 3 in tuple1 is:', res);

"""


import random

# List of names of potential crorepati
names = ["John", "Jane", "Alice", "Bob", "Emma", "Michael", "Olivia", "David", "Sophia", "William"]

# Randomly select a crorepati from the list
crorepati = random.choice(names)

# Print the selected crorepati
print(f"The crorepati is: {crorepati}")

