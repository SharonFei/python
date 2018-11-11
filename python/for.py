numBlocks=int(input('How many blocks of stars do you want?'))
numLines=int(input('How many lines of stars do you want?'))
numStars=int(input('How many stars do you want?'))
for block in range(0,numBlocks):
    for line in range(0,numLines):
        for star in range(0,numStars):
            print ('*',end=" ")
        print()
    print()
          
