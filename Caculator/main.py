
def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def devide(x,y):
    if y ==0 :
        return "Lỗi y = 0"
    return x / y
def main():
    print("__SIMPLE CACULATOR__")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Devide")
    choice = input("Enter your choice: ")
    x = int(input("Enter your number x: "))
    y = int(input("Enter your number y: "))
    if choice == "1":
        print("Result", add(x,y))
    elif choice == "2":
        print("Result", subtract(x,y))
    elif choice == "3":
        print("Result", multiply(x,y))
    elif choice == "4":
        print("Result:", devide(x,y))
    else:
        print(" Invalid choice ")
if __name__ == "__main__":
    main()