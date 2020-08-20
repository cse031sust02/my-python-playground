num1 = input("Enter First Number : ")
num2 = input("Enter Second Number : ")
try:
    result = int(num1)/ int(num2)
    print("The result is : ", result)
except:
    print("Sorry! Can not divide")
    # ToDo : Add explanation
    quit()

print("Successfully Done!")