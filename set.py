
"""

s={1,2,34,56};
print(s);

inf ={"carla",True,34,908};
print(inf);

for value in inf:
    print(value);

"""
# Set Methods

# Union() method
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}

# print(cities.union(cities2));

# Update() Method
cities3 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities4 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# cities3.update(cities4);
# print(cities3);


# Intersection() Method
cities5 = {"Tokyo", "Madrid", "Berlin", "Delhi"};
cities6 = {"Tokyo", "Seoul", "Kabul", "Madrid"};

# print(cities5.intersection(cities6));

# Intersection_update() Method
cities5 = {"Tokyo", "Madrid", "Berlin", "Delhi"};
cities6 = {"Tokyo", "Seoul", "Kabul", "Madrid"};
# cities5.intersection_update(cities6);
# print(cities5);



# symmetric_difference() Method
cities7 = {"Tokyo", "Madrid", "Berlin", "Delhi"};
cities8 = {"Tokyo", "Seoul", "Kabul", "Madrid"};
# print(cities7.symmetric_difference(cities8));

# symmetric-differece_update()
cities9 = {"Tokyo", "Madrid", "Berlin", "Delhi"};
cities10 = {"Tokyo", "Seoul", "Kabul", "Madrid"};
# cities9.symmetric_difference_update(cities10);
# print(cities9);


# Difference() Method
cities11 = {"Tokyo", "Madrid", "Berlin", "Delhi"};
cities12 = {"Tokyo", "Seoul", "Kabul", "Madrid"};
# print(cities11.difference(cities12));

# Differece_update() Method
cities13 = {"Tokyo", "Madrid", "Berlin", "Delhi"};
cities14 = {"Tokyo", "Seoul", "Kabul", "Madrid"};
# cities13.difference_update(cities14);
# print(cities13);


# isdisjoint() Method
cities15 = {"Tokyo", "Madrid"}
cities16 = {"ght"}
# print(cities15.isdisjoint(cities16));


# Issuperset() Method
cities17 = {"Tokyo", "Madrid", "Berlin", "Delhi"};
cities18 = {"Tokyo", "Madrid"};
# print(cities17.issuperset(cities18));
# print(cities13);

# IsSubset() Method
cities19 = {"Tokyo", "Madrid", "Berlin", "Delhi"};
cities20 = {"Tokyo", "Madrid"};
# print(cities20.issubset(cities19));
# print(cities13);


# add() Method
cities21 = {"Tokyo", "Madrid", "Berlin", "Delhi"};
cities21.add("Tokyo1");
# print(cities21);


# update() Method
cities22 = {"Tokyo", "Madrid", "Berlin", "Delhi"};
cities23 = {"Tokyo1", "Madrid1"};
cities22.update(cities23);
# print(cities22);

# remove() and discard() Method
cities24 = {"Tokyo", "Madrid", "Berlin", "Delhi"};
# cities24.remove("Tokyo");
cities24.discard("Tokyo");
# print(cities24);

# cities25 = {"Tokyo", "Madrid", "Berlin", "Delhi"};
# # print(cities25.pop());

# try:
#  del cities25;
# #  print(cities25);
# except:
#     # print("Throw an Error");

# clear() is for empty set.
cities26 = {"Tokyo", "Madrid", "Berlin", "Delhi"};
cities26.clear();
# print(cities26);


