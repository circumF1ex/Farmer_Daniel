while True:
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			print(i, j)
			if can_harvest():
				harvest()
			
			if get_ground_type() == Grounds.Grassland:
				till()
			
			if get_pos_x() == 0:
				plant(Entities.Grass)
			elif get_pos_x() == 1:
				plant(Entities.Bush)
			elif get_pos_x() == 2:
				plant(Entities.Carrot)
		
			move(North)
			if get_pos_y() == 2:
				move(East)
			
		
			
		
		