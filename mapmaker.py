import queue
import sys
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

print(start_x,end_x)
print(start_y,end_y)

visitable_count = 0

for x in range(start_x,end_x):
    for y in range(start_y,end_y):
        if (x+y) > 21:
          mine_map[(x,y)] = 'M'
        else:
          mine_map[(x,y)] = 'V'
          visitable_count += 1


print(visitable_count)

