for i in range(get_world_size()):
	for j in range(get_world_size()):
		
		if get_ground_type() == Grounds.Grassland:
			if can_harvest():
				harvest()
			till()
		
		if get_pos_x() == 0:
			plant(Entities.Grass)
		elif get_pos_x() == 1:
			plant(Entities.Bush)
		elif get_pos_x() == 2:
			plant(Entities.Grass)

		harvest()
		
		move(North)
		if j == get_world_size() - 1:
			move(East)
			
		
			
		
		