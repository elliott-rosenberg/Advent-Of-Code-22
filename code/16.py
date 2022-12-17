# class Valve:
#     def __init__(self, start, flow, nexts, isOpened):
#         self.name = start
#         self.flowRate = flow
#         self.next = nexts
#         self.isOpened = isOpened

#     def getNexts(self):
#         return self.next

#     def setValve(self, opened):
#         self.isOpened = opened
    
#     def checkOpen(self):
#         return self.isOpened

#     def getFlow(self):
#         return self.flowRate

#     def getName(self):
#         return self.name
    



# def process(file):
#     lines = [l.strip() for l in open(file).readlines()]
#     valves = {}
#     for line in lines:
#         name = line.split('Valve ')[1][:2]
#         flowRate = int(line.split('=')[1].split(';')[0])
#         nexts = line.split('valves ')[1]#all of the connecting tunnels
#         nexts = [nexts.split(', ')]
#         if nexts[0][1] == 'x':
#             nexts[0].pop(1)
#         nexts = nexts[0]
#         opened = flowRate == 0
#         valves[name] = Valve(name, flowRate, nexts, opened)
#         print(f"new valve: {name} with flow: {flowRate} and connected valves: {nexts}")

#     print(valves.keys())
#     return valves

# # def getBetPath(valves, start, currPressure, minsLeft):
# #     print(f"GBP, start: {start.getName()}, pressure: {currPressure}, minsLeft: {minsLeft}")
# #     connecteds = start.getNexts()
# #     print(connecteds)
# #     if minsLeft == 0:
# #         return currPressure # should compare currPressure to 
# #     else:
    
# #         maxPressure = 0
# #         for node in connecteds: #does not avoid loops

# #             if valves[node].checkOpen() or minsLeft <= 1: #if the traveling node is open or 0
# #                 print("reachedOpened")
# #                 pressure = getBestPath(valves, valves[node], currPressure, minsLeft - 1) #travels to node and finds best path from that one
# #             else: #if the node that you're traveling to has a flow rate
                
# #                 currPressure = currPressure + (valves[node].getFlow() * (minsLeft - 2))
# #                 print(f"reachedClosed, currPressure {currPressure}")
# #                 valves[node].setValve(True)
# #                 pressure = getBestPath(valves, valves[node], currPressure, minsLeft - 2)
# #                 valves[node].setValve(False)
# #             if pressure > maxPressure:
# #                 maxPressure = pressure
# #                 print(f"max: {maxPressure}")
# #         return maxPressure

# def getBestPath(valves, start, currPressure, minsLeft):
    
#     # print(f"GBP, start: {start.getName()}, pressure: {currPressure}, minsLeft: {minsLeft}")
#     connecteds = start.getNexts()
#     # print(connecteds)
#     didIOpen = False
#     if minsLeft >= 1 and not start.checkOpen():
#         didIOpen = True
#         # print(f"valve setting: {start.getName()}, setting to: {didIOpen}")
#         start.setValve(True)
#         minsLeft = minsLeft - 1
#         # print(f"flow: {start.getFlow()}, minsLeft: {minsLeft}")
#         currPressure = currPressure + (start.getFlow() * (minsLeft))
    
#     if minsLeft  <= 1:
#         return currPressure
    
#     else: 
#         maxP = 0
#         for node in connecteds:
#             pressure = getBestPath(valves, valves[node], currPressure, minsLeft - 1)
#             if pressure > maxP:
#                 maxP = pressure
#                 print(maxP)
        
#         didIOpen = False
#         # print(f"valve setting: {start.getName()}, setting to: {didIOpen}")
#         start.setValve(didIOpen) #Closes the valve afterwards
        
#         return maxP



# def solvePart1(valves, mins):
#     return getBestPath(valves, valves['AA'], 0, mins)
#     #I currently have a dictionary with valves and their connecting valves
#     return True

# def solvePart2(file):
#     return True


# def solve(file):
#     networks = process(file)
#     print(f"Part 1: {solvePart1(networks, 6)}")
#     print(f"Part 2: {solvePart2(networks)}")

# solve("input/16/input1.txt")



# def solve(file):
#     # s1()
#     s2()




# def s1():
#     x=open("input/16/input1.txt","r").read().splitlines()

#     t={}
#     y={}

#     for i in x:
#         i=i.replace("="," ").replace(",","").replace(";","")
#         i=i.split()
#         print(i)

#         y[i[1]]=int(i[5])
#         t[i[1]]=i[10:]


#     from collections import deque as de

#     # min opened curr tot
#     q=de([(0,(),"AA",0)])
#     v=set()
#     w=0

#     print(y) #dictionary from valves to flow rate
#     print(t) #dictionary from valves to connecteds
#     while q:
#         a,b,c,d=q.popleft() #pops out the full de, starting wtih 0, (), AA, 0
#         #a = minute value, b = (), c = start, 'AA', d = 0
#         # print(a,b,c,d)
#         if a==30:
#             w=max(w,d);print(w);continue#print(w), d has something to do with minutes, w is max counter
#         if (b,c) in v:
#             continue #if both b and c are in set, continue
#         v.add((b,c))

#         dd=d #new minutes variable
#         for i in b:
#             dd+=y[i]
#         if y[c]!=0: #if flowrate of c is not 0
#             if c not in b: #b is a list of opened valves
#                 q.append((a+1,tuple(list(b)+[c]),c,dd))

#         for i in t[c]: #connecteds to start value
#             q.append((a+1,b,i,dd)) #add minute, 

# def s2():
#     x=open("input/16/input1.txt","r").read().splitlines()

#     t={}
#     y={}

#     for i in x:
#         i=i.replace("="," ").replace(",","").replace(";","")
#         i=i.split()

#         y[i[1]]=int(i[5])
#         t[i[1]]=i[10:]


#     from collections import deque as de

#     # min opened curr tot
#     q=de([(0,(),"AA","AA",0)])
#     v=set()
#     w=0

#     l=0
#     for i in y.values():
#         if i !=0:l+=1
#     print(l)
#     u=sum(y.values())
#     print(u)
#     from time import sleep
#     sleep(0)

#     from collections import defaultdict as dd
#     h=dd(int)
#     print(y)
#     while q:
#         a,b,c,cc,d=q.popleft()
#         #f,ff=1,1
#         #print(a)
#         #print(b)
#         #print(a,b,c,d)
#         if a==26:w=max(w,d);print(w);continue
#         if len(b)==l:w=max(w,(26-a)*u+d);print(w);continue
#         if (b,c,cc) in v:continue
#         if (b,cc,c) in v:continue
#         v.add((b,c,cc))
#         v.add((b,cc,c))
#         if a > 10:
#             if d<8.5*(h[a]//10):continue

#         dd=d
#         for i in b:
#             dd+=y[i]


#         h[a]=max(h[a],d)
#         if y[c]!=0:
#             if c not in b:
#                 bb=tuple(list(b)+[c])

#                 if y[cc]!=0:
#                     if cc not in b and cc != c:
#                         bbb=tuple(list(bb)+[cc])
#                         q.append((a+1,bbb,c,cc,dd))
#                         if cc != "AA":continue

#                 for i in t[cc]:
#                     q.append((a+1,bb,c,i,dd))
#                 #if c != "AA":continue

#         if y[cc]!=0:
#             if cc not in b:
#                 bb=tuple(list(b)+[cc])


#                 for i in t[c]:
#                     if i in b:continue
#                     #if len(b)==l-1:i=c
#                     q.append((a+1,bb,i,cc,dd))

#                 if cc != "AA":continue

#         for i in t[c]:
#             for ii in t[cc]:
#                 #if ii==i:continue
#                 #if i in b:continue
#                 #if len(b)==l-1:i=c
#                 q.append((a+1,b,i,ii,dd))


# solve("input/16/input1.txt")




from math import inf as INFINITY
from functools import partial
from operator import itemgetter
from itertools import combinations, product
from collections import defaultdict

from utils import advent

def floyd_warshall(g):
	distance = defaultdict(lambda: defaultdict(lambda: INFINITY))

	for a, bs in g.items():
		distance[a][a] = 0

		for b in bs:
			distance[a][b] = 1
			distance[b][b] = 0

	for a, b, c in product(g, g, g):
		bc, ba, ac = distance[b][c], distance[b][a], distance[a][c]

		if ba + ac < bc:
			distance[b][c] = ba + ac

	return distance

def score(rates, valves):
	s = 0
	for v, t in valves.items():
		s += rates[v] * t
	return s

def solutions(distance, rates, valves, time=30, cur='AA', chosen={}):
	for nxt in valves:
		new_time = time - distance[cur][nxt] - 1
		if new_time < 2:
			continue

		new_chosen = chosen | {nxt: new_time}
		yield from solutions(distance, rates, valves - {nxt}, new_time, nxt, new_chosen)

	yield chosen


advent.setup(2022, 16)

from utils.timer import timer_start
timer_start()

graph = defaultdict(list)
rates = {}

with advent.get_input() as fin:
	for fields in map(str.split, fin):
		src  = fields[1]
		dsts = list(map(lambda x: x.rstrip(','), fields[9:]))
		rate = int(fields[4][5:-1])

		rates[src] = rate

		for dst in dsts:
			graph[src].append(dst)

good     = frozenset(filter(rates.get, graph))
distance = floyd_warshall(graph)
score    = partial(score, rates)
best     = max(map(score, solutions(distance, rates, good)))

advent.print_answer(1, best)


maxscore = defaultdict(int)

for solution in solutions(distance, rates, good, 26):
	k = frozenset(solution)
	s = score(solution)

	if s > maxscore[k]:
		maxscore[k] = s

best = max(sa + sb for (a, sa), (b, sb) in combinations(maxscore.items(), 2) if not a & b)
advent.print_answer(2, best)