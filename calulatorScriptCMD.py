#control functions

def add(x,y):
    return x + y
def minus(x,y):
	return x - y
def multiply(x,y):
	return x * y
def divide (x,y):
	if y == 0:
		return "Math ERROR"
	else:
		return x/y
def power (x,y):
	return x ** y
def root (x,y):
	return x ** (1/y)

#whileloop with menu
while True:
    print("\nSimple Calculator")
    print("***YOU CAN ONLY ENTER 2 VALUES PER FUNCTION")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print ("6.Root")
    print("7.Close/Quit")
	
    choice = input("\nSelect a Function (1-7): ")
    
    if choice == "7":
        print("Exiting calculator...")
        break
        
    
    #if choice in ["1","2","3","4","5","6"]:
        #num1=float(input("Enter the first Number:"))
        #num2=float(input("Enter the second Number:"))
	
    elif choice == "1":
        num1=float(input("Enter the first Number:"))
        num2=float(input("Enter the second Number:"))
        print("Result of ", num1 ," + ", num2, "=",add(num1,num2))
	
	
    elif choice == "2":
        num1=float(input("Enter the first Number:"))
        num2=float(input("Enter the second Number:"))
        print("Result of ", num1 ," - ", num2, "=",minus(num1,num2))
	
	
    elif choice == "3":
        num1=float(input("Enter the first Number:"))
        num2=float(input("Enter the second Number:"))
        print("Result of multiplying ", num1 ," with ", num2, "=",multiply(num1,num2))
	
	
    elif choice == "4":
        num1=float(input("Enter the first Number:"))
        num2=float(input("Enter the second Number:"))
        print("Result of dividing ", num1 ," with ", num2, "=",divide(num1,num2))
	
	
    elif choice == "5":
        num1=float(input("Enter the first Number:"))
        num2=float(input("Enter the second Number:"))
        print("Result of ", num1 ,"as the power of ",num2, "=",power(num1,num2))
	
	
    elif choice == "6":
        num1 = float(input("Enter the number you want the root of: "))
        num2 = float(input("Enter the degree of the root: "))
        print("Result:", num2, "th root of", num1, "=", root(num1, num2))
        
    else:
        print("Invalid choice! Please select a number 1-7.")
		
input("Press Enter to exit...")
	