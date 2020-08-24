def HDL_input():
    print("Enter HDL Value: ")
    ret = int(input())
    return ret
def HDL_check(x):
    if x >= 60:
        return "Normal"
    elif x >= 40 and x < 60:
        return "Borderline Low"
    else:
        return "Low"
def HDL_out(msg):
    print(msg, "\n")


def HDL_driver():
    # Get input
    a = HDL_input()
    # Check if HDL is normal 60 or more normal, 40 - 60 borderline low, < 40 is low
    b = HDL_check(a)
    # Output
    HDL_out(b)

def interface():
    print("My Program")
    while True:
        print("Options")
        print("1 - HDL")
        print("9 - Quit")
        choice = input("Enter your choice: ")
        if choice == "9":
            return
        elif choice == "1":
            HDL_driver()

interface()
