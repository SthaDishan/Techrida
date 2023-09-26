
# try, except


# x= int(input("Enter the value of x: "))
# print(f"x is: {x}")




def main():
    x = get_int()
        print(f"x is {x}")

def get_int():
    while True:
        try:
            x= int(input("Enter the value of x: "))     
            return x 
        except ValueError:
            print("x is not an integer")

main()