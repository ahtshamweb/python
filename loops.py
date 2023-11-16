'''


a = "Hello";
for e in a :
    print(e)

list = ["apple","banana","saeb","orange"];
for lis in list:
    print(lis);
    for a in lis:
        print(a);

for i in range(5):
    print(i);



wh = 0;
while(wh<=5):
  print(wh);
  wh = wh +1 ;

# i = input()

for i in range(1,12):
    if(i==5):
        print("This is 5");
        break;
    print("5 X" , i ,"=" , 5*i)



def adition(a,b):
    print(a+b/a-b);

adition(2,5);


'''

# if_else in Loop

user_input = input("Please enter a number: ")
i = int(user_input)
while i<7:
    print(i) ;
    i = i + 1 ;
    if(i==4):
        break;
    else:
        continue;    















