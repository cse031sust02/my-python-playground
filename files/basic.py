fhand = open('demo.txt')

counter = 0
for line in fhand:
    counter = counter + 1
    # ToDo : Add explanation for rstrip()
    line = line.rstrip()
    print(counter, line)
