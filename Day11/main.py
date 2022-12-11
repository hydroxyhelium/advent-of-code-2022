from typing import List

class Monkey():
    ## starting_items is an array of worry levels of each item. 
    ## operation is function that takes in (worry level)=>(new worry level)
    ## Monkey_List is the list of monkeys that would be supplied later
    def __init__(self, starting_items, operation, condition,items_inspected, Monkey_List) -> None:
        self.starting_items = starting_items 
        self.operation = operation 
        self.condition = condition
        self.items_inspected = items_inspected
        self.Monkey_List = Monkey_List

    def move(self) ->None:
        while(self.starting_items):
            worry_level = self.starting_items[0]
            worry_level_modified = self.operation(worry_level)
            self.items_inspected += 1 
            monkey_index_to_send = self.condition(worry_level_modified)
            self.starting_items.pop(0)
            self.Monkey_List[monkey_index_to_send].push_back(worry_level_modified)
        
    def set_monkey_list(self, Monkey_List):
        self.Monkey_List = Monkey_List

    def push_back(self, worry):
        self.starting_items.append(worry)

    def print_inspected(self):
        print(self.items_inspected)


op1 = lambda x: ((x*17)//3)
op2 = lambda x: ((x+7)//3)
op3 = lambda x: ((x*x)//3)
op4 = lambda x: ((x+1)//3)
op5 = lambda x: x
op6 = lambda x: ((x+4)//3)
op7 = lambda x: ((x+8)//3)
op8 = lambda x: ((x+6)//3)


con1 = lambda x: 2 if (x%11==0) else 3 
con2 = lambda x: 6 if (x%3==0) else 5 
con3=  lambda x: 1 if (x%5==0) else 7 
con4 = lambda x: 2 if (x%7==0) else 7 
con5 = lambda x: 0 if (x%19==0) else 3
con6 = lambda x: 6 if (x%2==0) else 4
con7 = lambda x: 4 if (x%13==0) else 0
con8 = lambda x: 1 if (x%17==0) else 5

list1 = [56, 52, 58, 96, 70, 75, 72]
list2 = [75, 58, 86, 80, 55, 81]
list3 = [73, 68, 73, 90]
list4 = [72, 89, 55, 51, 59]
list5 = [76, 76, 91]
list6 = [88]
list7 = [64, 63, 56, 50, 77, 55, 55, 86]
list8 = [79, 58]



monkey1 = Monkey(list1, op1, con1, 0, [])
monkey2 = Monkey(list2, op2, con2, 0, [])
monkey3 = Monkey(list3, op3, con3, 0, [])
monkey4 = Monkey(list4, op4, con4, 0, [])
monkey5 = Monkey(list5, op5, con5, 0, [])
monkey6 = Monkey(list6, op6, con6, 0, [])
monkey7 = Monkey(list7, op7, con7, 0, [])
monkey8 = Monkey(list8, op8, con8, 0, [])

Monkey_List = [monkey1,monkey2, monkey3, monkey4, monkey5, monkey6, monkey7, monkey8]

for i in Monkey_List:
    i.set_monkey_list(Monkey_List)

for i in range(20):
    for j in Monkey_List:
        j.move()

for i in Monkey_List:
    i.print_inspected()

 



    