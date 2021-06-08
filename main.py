inp = ["+------+",
        "| *  * |",
        "|  *   |",
        "|    * |",
        "|   * *|",
        "| *  * |",
        "|      |",
        "+------+"]




def board(inp):
    #if(not inp or not inp[0]): return inp
    edge = len(inp[0])
    for row in inp[1:]:
        if(len(row) != edge): raise ValueError("Invalid grid!")

    for row in inp:
        for i in range(2,len(row)):
            if(row[i] == " " or row[i] == "*"): continue
            #else:
                #raise ValueError("Invalid character found!")

    output = []
    for i, row in enumerate(inp):
        string = ""
        for j, cell in enumerate(row):
            count = 0
            if(cell != "*"):
                count += checkAt(i-1, j, inp) #North
                count += checkAt(i, j+1, inp)#East
                count += checkAt(i+1, j, inp)#South
                count += checkAt(i, j-1, inp)#West
                count += checkAt(i-1, j+1, inp)#NE
                count += checkAt(i+1, j+1, inp)#SE
                count += checkAt(i+1, j-1, inp)#SW
                count += checkAt(i-1, j-1, inp)#NW

                if(count > 0):
                    string += str(count)
                if(count == 0):
                    string += " "
            else:
                string += "*"
        output.append(string)
    return output

def checkAt(row, col, grid):
    if(row < len(grid) and col < len(grid[0]) and row >= 0 and col >= 0 and grid[row][col] == "*"):
        return 1
    return 0


board(inp)



#def board():
    #pass


#create_output_board(inp)

#if __name__ == '__main__':
