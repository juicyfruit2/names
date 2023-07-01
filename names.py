# Require the user to enter the names of all pupils in a class. 

# ask user to enter the names of puplis 
names = input("Enter names pupils('stop' when done):")

# line 8-12  used while loop and if statements 
total_names = 0
while names!='stop':
    names = input("Enter name of pupils('stop'when done):")
    total_names = total_names + 1
    if names =='stop':
        break 
print(total_names)






