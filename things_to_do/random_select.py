import random

input_file = "things.txt"
f = open(input_file, 'r')

choices = [] 
for choice in f:
    #print(choice)
    choices.append(choice)

f.close()

#print("all choices ")
#print(choices)

num = len(choices)
select = random.randint(0, num-1)
print("select", select, choices[select])
