def move_to_x(x):
	if get_pos_x() > x:
		for _ in range(get_pos_x() - x):
			move(West)
	elif get_pos_x() < x:
		for _ in range(x - get_pos_x()):
			move(East)
	else:
		pass
	
def move_to_y(y):
	if get_pos_y() > y:
		for _ in range(get_pos_y() - y):
			move(South)
	elif get_pos_y() < y:
		for _ in range(y - get_pos_y()):
			move(North)
	else:
		pass
		
def move_to_xy(x, y):
	move_to_x(x)
	move_to_y(y)
		