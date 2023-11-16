import dictionaries;

'''

a = int(input("enter your age: "))
print("Please enter your age" , a)

if(a>18):
    print("yes its greater than 18");
elif(a<18):
     if(a==10):
        print("it is equal to: ",a)
     elif(a==5):
        print("it is equal to:",a)  
     else:
        print("it is just less than ",18);   

else:
    print("No,its not right")


print("This Is Separate")



x =int(input("please enter the number: "))

match x:

    case 0:
        print("x is zero");
    case 4:
        print("x is 4");

    case _ if x!=90:
        print("itis not equal to 90")        
    case _ if x!=80:    
        print("it is not  equal to 80");

'''

# Short hand if else

a=90;
b=59;
print("A") if (a>b) else print("=") if (a==b) else print("B");

c = 9 if a>b else 0;
print(c);