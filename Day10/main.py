def part_one_solutions():
    
    ## this is the input text replace this by text being given to you 
    text = "addx 1 addx 4 noop noop noop addx 5 addx 3 noop addx 2 noop noop noop noop addx 3 addx 5 addx 2 addx 1 noop addx 5 addx -1 addx 5 noop addx 3 noop addx -40 noop addx 38 addx -31 addx 3 noop addx 2 addx -7 addx 8 addx 2 addx 5 addx 2 addx 3 addx -2 noop noop noop addx 5 addx 2 noop addx 3 addx 2 noop addx 3 addx -36 noop noop addx 5 noop noop addx 8 addx -5 addx 5 addx 2 addx -15 addx 16 addx 4 noop addx 1 noop noop addx 4 addx 5 addx -30 addx 35 addx -1 addx 2 addx -36 addx 5 noop noop addx -2 addx 5 addx 2 addx 3 noop addx 2 noop noop addx 5 noop addx 14 addx -13 addx 5 addx -14 addx 18 addx 3 addx 2 addx -2 addx 5 addx -40 noop addx 32 addx -25 addx 3 noop addx 2 addx 3 addx -2 addx 2 addx 2 noop addx 3 addx 5 addx 2 addx 9 addx -36 addx 30 addx 5 addx 2 addx -25 addx 26 addx -38 addx 10 addx -3 noop noop addx 22 addx -16 addx -1 addx 5 addx 3 noop addx 2 addx -20 addx 21 addx 3 addx 2 addx -24 addx 28 noop addx 5 addx 3 noop addx -24 noop"
    ## the text is then split into array
    arr = text.split(" ")
    ## this array would be filled with the intensity of CRT and added up on returning 
    values = []
    ## cycle starts at one
    cycle_start = 1
    ## the target values where we measure the intensity
    target_values = [20, 60, 100, 140, 180, 220]
    ## value of X in the CPU 
    X = 1 

    ## We loop through the array and maintain track of cycle being executed 
    for i in range(len(arr)):

        ## First type of instruction
        if(arr[i]=="noop"):
            # Execution has begun
            begin_cycle = cycle_start
            print("cycle"+ " "+ str(cycle_start)+ " " + str(X))
            if(cycle_start in target_values):
                values.append(cycle_start*X)

            # begin_cycle being executing 
            # X remains unchanged 
            cycle_start+=1
            # execution of the noop instruction has ended
            pass
        
        ## second type of instruction
        elif(arr[i]=="addx"):
            num = arr[i+1]
            # at start of cycle X remains unchanged 
            begin_cycle = cycle_start
            #begin_cycle begin executed
            
            if(cycle_start in target_values):
                values.append(cycle_start*X)  
            
            print("cycle"+ " "+ str(cycle_start)+ " " + str(X))
            
            cycle_start +=1 # One cycle finished X remains unchanged 
            
            if(cycle_start in target_values):
                values.append(cycle_start*X)
            print("cycle"+ " "+ str(cycle_start)+ " " + str(X))
            # cycle_start+1 cycle being executed
            cycle_start += 1 # 2nd cycle is finished
            X += int(num)
            #cylce_start += 1 being executed

        ## we pass when we see numbers
        else:
            pass

    ## At the end of the for loop we sum up all the intensities and return the answer
    print(sum(values)) 

# a function to convert back cathode ray tube implementation of the function
 
def print_string(output_string):
    ## we just append new line characters where required and return the answer
    for i in [40, 81, 122, 163, 204, 246]:
        output_string.insert(i, "\n")
    print("".join(output_string))


def part_two_solutions():
    text = "addx 1 addx 4 noop noop noop addx 5 addx 3 noop addx 2 noop noop noop noop addx 3 addx 5 addx 2 addx 1 noop addx 5 addx -1 addx 5 noop addx 3 noop addx -40 noop addx 38 addx -31 addx 3 noop addx 2 addx -7 addx 8 addx 2 addx 5 addx 2 addx 3 addx -2 noop noop noop addx 5 addx 2 noop addx 3 addx 2 noop addx 3 addx -36 noop noop addx 5 noop noop addx 8 addx -5 addx 5 addx 2 addx -15 addx 16 addx 4 noop addx 1 noop noop addx 4 addx 5 addx -30 addx 35 addx -1 addx 2 addx -36 addx 5 noop noop addx -2 addx 5 addx 2 addx 3 noop addx 2 noop noop addx 5 noop addx 14 addx -13 addx 5 addx -14 addx 18 addx 3 addx 2 addx -2 addx 5 addx -40 noop addx 32 addx -25 addx 3 noop addx 2 addx 3 addx -2 addx 2 addx 2 noop addx 3 addx 5 addx 2 addx 9 addx -36 addx 30 addx 5 addx 2 addx -25 addx 26 addx -38 addx 10 addx -3 noop noop addx 22 addx -16 addx -1 addx 5 addx 3 noop addx 2 addx -20 addx 21 addx 3 addx 2 addx -24 addx 28 noop addx 5 addx 3 noop addx -24 noop"
    arr = text.split(" ")
    cycle_start = 1

    ## this time we maintain output string that is being printed on CRT
    output_string = ["." for i in range(240)]

    ## only thing take care to left is that during execution of cycle n index n-1 is begin changed  

    #target_values = [20, 60, 100, 140, 180, 220]
    X = 1  
    ## this time it also represents middle of the sprite position
    for i in range(len(arr)):
        if(arr[i]=="noop"):
            # Execution has begun
            begin_cycle = cycle_start
            ## right now cycle_start is being executed.
            index_being_changed = cycle_start-1

            ## It's ALWAYS the case that CRT is working on index that is one less that actual value
            if(index_being_changed%40 in [X-1, X, X+1]):
                output_string[index_being_changed]="#"

            print("cycle"+ " "+ str(cycle_start)+ " " + str(X))

            # begin_cycle being executing 
            # X remains unchanged 
            cycle_start+=1
            # execution of the noop instruction has ended
            pass
        
        elif(arr[i]=="addx"):
            num = arr[i+1]
            # at start of cycle X remains unchanged 
            begin_cycle = cycle_start
            #begin_cycle begin executed
            
            index_being_changed = cycle_start-1

            if(index_being_changed%40 in [X-1, X, X+1]):
                output_string[index_being_changed]="#"
            
            print("cycle"+ " "+ str(cycle_start)+ " " + str(X))


            cycle_start +=1 # One cycle finished X remains unchanged 

            index_being_changed = cycle_start-1

            if(index_being_changed%40 in [X-1, X, X+1]):
                output_string[index_being_changed]="#"
            
            print("cycle"+ " "+ str(cycle_start)+ " " + str(X))
            # cycle_start+1 cycle being executed
            cycle_start += 1 # 2nd cycle is finished
            X += int(num)
            #cylce_start += 1 being executed
        else:
            pass

    print_string(output_string)




## initially X's position is controled by the spire 
