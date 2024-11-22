def addition(x,y):
    return(x+y)

def subtraction(x,y):
    return(x-y)

def multiplication(x,y):
    return(x*y)

def divition(x,y):
    return(x/y)
def modulas(x,y):
    return(x%y)

no1=eval(input("enter the first number:"))
no2=eval(input("enter the second number:"))

print("select the option:")
print("1.addition")
print("2.subtraction")
print("3.multiplicati")
print("4.divition")
print("5.modulas")

print("6.exit")


while(True):
    choice=int(input("enter the choice from(1/2/3/4/5/6)-->"))
    if choice in (1,2,3,4,5):
        if choice==1:
            print("Addition of two numbers",no1,"and",no2,"is->",addition(no1,no2))
        elif choice==2:
            print("subtraction of two numbers",no1,"and",no2,"is->",subtraction(no1,no2))
        elif choice==3:
            print("multiplication of two numbers",no1,"and",no2,"is->",multiplication(no1,no2))
        elif choice==4:
            print("divition of two numbers",no1,"and",no2,"is->",divition(no1,no2))

        elif choice==5:
            print("modulas of two numbers",no1,"and",no2,"is->",modulas(no1,no2))
 
        elif choice==6:
            print("Thank you :)")
            exit()
    else:
        print("invalid choice try again")