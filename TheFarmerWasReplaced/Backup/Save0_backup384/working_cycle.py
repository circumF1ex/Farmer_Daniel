from movement import *

move_to_xy(0,0)
ws = get_world_size()

x, y = 0, 0

while True:
	
	if get_pos_x() % 2 == 0:
		y += 1
		move_to_y(y)
	elif get_pos_x() % 2 > 0:
		y -= 1
		move_to_y(y)
	
	print(x,y)
	if get_pos_y() == 5 or get_pos_y() == 0:
		if x > 5:
			x = 0
		else:
			x += 1
		move_to_x(x)

	

	