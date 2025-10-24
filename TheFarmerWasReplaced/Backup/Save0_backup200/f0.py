w_s = get_world_size()
while True:

	for i in range(w_s):
		move(East)
		for j in range(w_s):
			
			
			if can_harvest():
				harvest()
			
			if get_ground_type() == Grounds.Grassland:
				till()
			
			if get_pos_x() == 0:
				plant(Entities.Grass)
			elif get_pos_x() == 1:
				if get_pos_y()
				plant(Entities.Bush)
			elif get_pos_x() == 2:
				plant(Entities.Carrot)

			move(North)
		
			
		
		