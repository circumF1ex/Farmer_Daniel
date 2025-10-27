from movement import *

move_to_xy(0,0)
ws = get_world_size()

x, y = 0, 0

while True:
	
	if get_pos_x() % 2 == 0:
		y += 1
		move_to_xy(x, y)
	else:
		y -= 1
		move_to_xy(x, y)
	x += 1
	