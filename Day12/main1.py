class Node():
    # Every node in the graph can be represented by it's name, (weather it's lowercase or not), 
    # and the number of connections, and a list of places_visited in the graph
    def __init__(self, name, capital, connections, places_visited) -> None:
        self.name = name 
        self.capital = capital
        self.connections = [x for x in connections]
        self.places_visited = [x for x in places_visited]

    def append_connections(self, node)-> None:
        self.connections.append(node)

    def set_connections(self, connections) -> None:
        self.connections = connections
        pass

    def set_places_visited(self, places_visited) -> None:
        self.places_visited = places_visited
        pass

    def get_name(self) -> str:
        return self.name

    def count_places(self)->int:
        
        if(self.name=="end"):
            print(list(map(lambda x: x.get_name(),self.places_visited)))
            return 1 
        
        else:
            count = 0 

            for index, i in enumerate(self.connections):
                if i.get_name() in list(map(lambda x: x.get_name(),self.places_visited)):
                    continue

                else:
                    if(self.capital):
                        temp_node = i
                        places_visited = [x for x in self.places_visited]
                        temp_node.set_places_visited(places_visited)
                        #print(list(map(lambda x: x.get_name(),places_visited)))
                        count += temp_node.count_places()
                    else:
                        temp_node = i 
                        places_visited = [x for x in self.places_visited]
                        places_visited.append(self)
                        temp_node.set_places_visited(places_visited)
                        #print(list(map(lambda x: x.get_name(),places_visited)))
                        count += temp_node.count_places()

            return count

temp = "start-A start-b A-c A-b b-d A-end b-end"
example = "start-A start-b A-end A-b"


def create_hashmap(text):
    hashmap = {}
    for index, i in enumerate(text.split(' ')):
        pos_A, pos_B = i.split('-')

        if(pos_A in hashmap.keys()):
            hashmap[pos_A].append(pos_B)
        else:
            hashmap[pos_A]=[pos_B]

        if(pos_B in hashmap.keys()):
            hashmap[pos_B].append(pos_A)
        else:
            hashmap[pos_B]=[pos_A]
    
    return hashmap

#print(create_hashmap(example).keys())

def create_nodes(hashmap):
    start = None
    nodes_array = []
    pos_map = {}


    ## code to create a list of all the nodes
    for index, i in enumerate(list(hashmap.keys())):
        if(i.isupper()):
            nodes_array.append(Node(i, True, [], []))
            pos_map[i]=index
        else:
            nodes_array.append(Node(i, False, [], []))
            pos_map[i]=index
    
    for index, i in enumerate(list(hashmap.keys())):
        connections = hashmap[i]
        for subindex, j in enumerate(connections):
            nodes_array[pos_map[i]].append_connections(nodes_array[pos_map[j]])
    
    return nodes_array[pos_map['start']].count_places()


print(create_nodes(create_hashmap(example)))