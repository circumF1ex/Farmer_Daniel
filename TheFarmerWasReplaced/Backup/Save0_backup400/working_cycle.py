from movement import *

move_to_xy(0,0)
ws = get_world_size()

x, y = 0, 0

while True:
	
	if get_pos_x() % 2 == 0:
		y += 1
		if get_ground_type() = Grounds.Grassland:
			till()
		plant(Entities.
		move_to_y(y)
	elif get_pos_x() % 2 > 0:
		y -= 1
		move_to_y(y)
	
	if x > 5:
		x = 0
	
	if y == 5 or y == 0:
		x += 1
		move_to_x(x)

	
	print(x,y)

	

	