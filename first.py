string = str(input("pls enter the word: "))
char = str(input("pls enter your own charecter: "))
i = 0
count = 0

while(i < len(string)):

    if(string[i] == char):
        count = count + 1
    i = i+1

print("the total number of times",char,"has occures=",count)        