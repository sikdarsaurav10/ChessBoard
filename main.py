# x and y are the co-ordinates of the opposite pawn
# the output should produce a series of tuples of the path taken by our pawn
'''
The time complexity for the below program for the best case if no pawn encountered is -> O(n)
and the worst case if we encounter a opp_pawn on our path is -> O(n^3)
The space complexity for the program can be stated to have a constant space complexity

So, should i try another approach for the below program and try to see if i can reduce the time
complexity of the program!!
'''





x, y = [int(x) for x in input("Enter co-ordinates of pawn with space(expect(0,0) and (7,7)): ").split()]
opp_pawn = (x,y)

#i and j are the initial position of our pawn
i = 0
j = 0

flag = False
while i<=8 and j<=8:
    pawn = (i,j)
    if i==x and j==y:
        flag = True
        print('Pawn encountered taking alternate route!!')
        i = 0
        j = 0
    if flag == False:
        print(pawn)
        i+=1
        j+=1
        if i==8 and j==8:
            print('Shortest Route, no pawn encountered!!')
            break

    elif flag == True:
        while i<=x-1 and j<=y-1:
            pawn = (i, j)
            if i == x - 1 and j == y - 1:
                while i <= 8 and j <= 8:
                    if i < x + 2 and j == y - 1:
                        pawn = (i,j)
                        print(pawn)
                        i += 1
                    if j < y + 2 and i == x + 1:
                        pawn = (i, j)
                        j += 1
                        print(pawn)
                    if i == j and i<=7 and y<=7:
                        pawn = (i, j)
                        print(pawn)
                        i+=1
                        j+=1
                        if i==8 and j==8:
                            print('Shortest route!!')
            elif i<x-1 and j<y-1:
                print(pawn)
                i+=1
                j+=1







