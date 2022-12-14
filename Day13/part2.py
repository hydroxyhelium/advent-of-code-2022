import ast 
from functools import cmp_to_key

## to make this is a comparison function we will reuturn 
## 1 if right order 
## -1 if not right order 
## 0 if tie
def compare_list(left, right):

    if(left == [] and right == []):
        return 0
    elif(left == []):
        return 1 
    elif(right == []):
        return -1 
    else:
        first_elemet = left[0]
        second_element = right[0]

        if(isinstance(first_elemet, int) and isinstance(second_element, int)):
            if(first_elemet<second_element):
                return 1
            elif(second_element<first_elemet):
                return -1
            else:
                return compare_list(left[1:], right[1:])
        else:
            if(isinstance(first_elemet, list) and isinstance(second_element, list)):

                if(compare_list(first_elemet, second_element)==0):
                    return compare_list(left[1:], right[1:])

                if(compare_list(first_elemet, second_element)==1):
                    return 1
                
                else:
                    return -1
            else:
                ## this would be the case if the first element is an int and the second is a list 
                if(isinstance(first_elemet, int)):
                    modified_first_element = [first_elemet]

                    res = compare_list(modified_first_element, second_element)

                    if(res==0):
                        return compare_list(left[1:], right[1:])

                    elif(res==1):
                        return 1
                    
                    else: 
                        return -1


                else:
                    modified_second_element = [second_element]

                    res = compare_list(first_elemet, modified_second_element)

                    if(res==0):
                        return compare_list(left[1:], right[1:])
                    
                    elif(res==1):
                        return 1

                    else: 
                        return -1

#print(compare_list([7,7,7],[[6]]))


def load_data(f_name):
    cur_index = 1 
    index_array = []
    temp_array = []
    with open(f_name) as f:
        for line in f:
            if(line=="\n"):
                temp_array = []
                cur_index += 1
                continue
            line = ast.literal_eval(line)
            if(len(temp_array)==1):
                temp_array.append(line)
                if(compare_list(temp_array[0], temp_array[1])==1):
                    index_array.append(cur_index)
            else: 
                temp_array.append(line)
    
    return sum(index_array)

def sort_data(fname):
    unsorted_array = [[[2]], [[6]]]
    with open(fname) as f:
        for line in f:
            if(line == "\n"):
                continue
            else:
                line = ast.literal_eval(line)
                unsorted_array.append(line)
    
    return sorted(unsorted_array, key=cmp_to_key(lambda item1, item2: compare_list(item1, item2)))[::-1]

def track_index(array):
    index_1 = array.index([[2]])+1
    index_2 = array.index([[6]])+1

    return index_1*index_2

fname="input.in"

print(track_index(sort_data(fname)))


