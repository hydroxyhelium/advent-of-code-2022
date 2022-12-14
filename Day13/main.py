import ast


## this is a function that evaluates left and right list 
def compare_list(left, right):

    if(left == [] and right == []):
        return None
    elif(left == []):
        return True 
    elif(right == []):
        return False 
    else:
        first_elemet = left[0]
        second_element = right[0]

        if(isinstance(first_elemet, int) and isinstance(second_element, int)):
            if(first_elemet<second_element):
                return True
            elif(second_element<first_elemet):
                return False
            else:
                return compare_list(left[1:], right[1:])
        else:
            if(isinstance(first_elemet, list) and isinstance(second_element, list)):

                if(compare_list(first_elemet, second_element) is None):
                    return compare_list(left[1:], right[1:])

                if(compare_list(first_elemet, second_element)):
                    return True 
                
                else:
                    return False
            else:
                ## this would be the case if the first element is an int and the second is a list 
                if(isinstance(first_elemet, int)):
                    modified_first_element = [first_elemet]

                    res = compare_list(modified_first_element, second_element)

                    if(res is None):
                        return compare_list(left[1:], right[1:])

                    elif(res):
                        return True
                    
                    else: 
                        return False 


                else:
                    modified_second_element = [second_element]

                    res = compare_list(first_elemet, modified_second_element)

                    if(res is None):
                        return compare_list(left[1:], right[1:])
                    
                    elif(res):
                        return True

                    else: 
                        return False 

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
                if(compare_list(temp_array[0], temp_array[1])):
                    index_array.append(cur_index)
            else: 
                temp_array.append(line)
    
    return sum(index_array)

print(load_data('input.in'))
#print(compare_list(first_list, second_list))
print(compare_list([7,7,7],[[6]]))

        
        










