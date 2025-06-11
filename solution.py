lineOfStar=""
userInput=int(input("Enter a number to see a tree: ")) 
counter=1
starCounter=1

while(counter<=userInput):
    while(starCounter<=counter):
        lineOfStar=lineOfStar+"*"
        starCounter=starCounter + 1
    print(lineOfStar)
    counter=counter+1