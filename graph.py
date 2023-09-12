from collections import deque

def seller_mangoes_person(name):
    return name[-1] == 'm'

def bfs(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if seller_mangoes_person(person):
                print(person + " is a mangoe seller")
                return True
            else:    
                search_queue +=graph[person]
                searched.append(person) 
    return False

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []
print(bfs("you"))
