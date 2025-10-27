from movement import *

move_to_xy(0,0)
ws = get_world_size()

x, y = 0, 0

while True:
	
	if can_harvest():
		harvest()
	
	if get_pos_x() % 2 == 0:
		
		if get_ground_type() == Grounds.Grassland:
			till()
		plant(Entities.Carrot)
		y += 1
		move_to_y(y)
		
	elif get_pos_x() % 2 > 0:
		
		if y % 2 == 0:
			plant(Entities.Tree)
		else:
			pass
		y -= 1
		move_to_y(y)
	
	if x > 5:
		x = 0
	
	if y == 5 or y == 0:
		x += 1
		move_to_x(x)



	

	