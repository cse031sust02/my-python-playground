# This will take input from the user
# If user types anything other that '#' and 'goodbye', It will print
# If user types '#', It will not print anything
# If user types 'goodbye', It will exit

while True:
    input_text = input("Type anything : ")
    if input_text == '#':
        continue
    if input_text == 'goodbye':
        break
    print(input_text)
