def add():

    a= int(input('Enter the value of a:'))

    b= int(input('Enter the value of b:'))

    c=a+b

    print("Addittion of a and b is :",c)
   
    



def sub():

    a= int(input('Enter the value of a:'))

    b= int(input('Enter the value of b:'))

    c=a-b

    print("Substraction of a and b is :",c)

   # print(c)
    




def mul():

    a= int(input('Enter the value of a:'))

    b= int(input('Enter the value of b:'))

    c=a*b

    print("multiplication of a and b is :",c)

def div():

    a= int(input('Enter the value of a:'))

    b= int(input('Enter the value of b:'))

    if a==0 or b==0:

        print("DIvision is not possible")
    

    else:

        print("DIvision is not")

    print("Divistion of a and b is :",c) 
    

while True:

    print("Addition = 1 ")
    print("Subtraction = 2")
    print("Multiplication = 3")
    print("Division = 4")


    if (int(input("Seclect your program : ")))==1:
        add()
    elif (int(input("Seclect your program : ")))==2:
        sub()
    elif (int(input("Seclect your program : ")))==3:

        mul()
    elif (int(input("Seclect your program : ")))==4:
        div()
    else:

        print("you select wrong type")



4