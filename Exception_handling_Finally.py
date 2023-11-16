# a =input("Enter a number:");
# try:
#   for i in range(1,11):
#    print(f"{int(a)} X {i} = {int(a)*i}");
# except:
#    print("Invalid  Input!");   
# finally:
#   print("Finally")
# print("success is a key to success");


a= int(input("Enter the Number b/t 5 & 9:: "));
if(a>5 or a<8):
 raise ValueError("Raise Error Please");
else:
 print("else");
print("end it");