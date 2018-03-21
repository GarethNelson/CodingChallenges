from tailrecurser import *
width  = 100
height = 100

start_x = int(0 - (width/2))
end_x   = start_x + width

start_y = int(0 - (height/2))
end_y   = start_y + height

mine_map = {}

# key
#  M mine
#  E empty
#  V can be visited

for x in range(start_x,end_x):
    for y in range(start_y,end_y):
        if (x+y) > 21:
          mine_map[(x,y)] = 'M'
        else:
          mine_map[(x,y)] = 'E'

visitable_count = 0

@trampwrap
def calculate_visitable(node,_cont=end_cont):
    global mine_map
    global visitable_count
    if node[0] < -50:  return
    if node[0] > 50:      return
    if node[1] < -50: return
    if node[1] > 50:     return
    if mine_map[node]=='V': return
    if mine_map[node]=='M': return
    mine_map[node] = 'V'
    visitable_count += 1
    return tailcall(calculate_visitable, (node[0],node[1]-1))
    return tailcall(calculate_visitable, (node[0],node[1]+1))
    return tailcall(calculate_visitable, (node[0]-1,node[1]))
    return tailcall(calculate_visitable, (node[0]+1,node[1]))
    return lambda: _cont(True)

calculate_visitable((0,0))

print(visitable_count)
