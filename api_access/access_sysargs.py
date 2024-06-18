import sys # this gives us access to the current operating system

# python ALWAYS receives system argument variables
print(sys.argv[0]) # sys.argv[0] is ALWAYS the name of the current module

for _ in sys.argv:
    print(_) # print each system argument variable