for i in range(get_world_size()):
	move(North)
	for j in range(get_world_size()):
		if j == get_world_size() - 1:
			move(East)
			
		
		