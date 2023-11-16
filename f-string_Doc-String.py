# ********************************************  f-String  *********************************************
"""
fomat_String = "Hey, My Name is {}"
Name="Ahtsham";

print(fomat_String.format(Name));



Name1="Ahtsham";
tem_literal = f"My Name is {Name1}";
print(tem_literal);


Name2="Ahtsham";
tem_literal = f"My Name is {{Name1}}";
print(tem_literal);

float_var = 34.890890;

print(f"My Float Variable{float_var:.2f}")

"""

# ************************************************  Doc String  ************************************


def square(n):
    '''Here we have to take square root of n '''
    if(n==1):
        print(n*2);
    else:
        print(n**4);
square(4);

print(square.__doc__);








