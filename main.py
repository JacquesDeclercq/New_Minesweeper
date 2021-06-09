inp = ["+------+",
        "| *  * |",
        "|  *   |",
        "|    * |",
        "|   * *|",
        "| *  * |",
        "|      |",
        "+------+"]




def board(inp):
    # COACHES' NOTE: inp? Don't use abbreviations for variable names.
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
    # COACHES' NOTE: this could have been a separate function.
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
    # COACHES' NOTE: it's okay to separate checks into multiple line or checks for readability
    if(row < len(grid) and col < len(grid[0]) and row >= 0 and col >= 0 and grid[row][col] == "*"):
        return 1
    return 0


board(inp)



#def board():
    #pass


#create_output_board(inp)

#if __name__ == '__main__':

# COACHES' NOTE: general feedback, take things one step at a time. Identify what the smallest action is within the problem and start writing a function. I feel you wrote a lot more code than I see here, but erased it because it didn't fit into the rest. 
