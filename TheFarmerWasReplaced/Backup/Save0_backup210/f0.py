w_s = get_world_size()
while True:

	for i in range(w_s):
		move(East)
		for j in range(w_s):
			
			
			if can_harvest():
				harvest()
			
			if get_water() < 0.4:
				use_item(Items.Water)
			
			if get_ground_type() == Grounds.Grassland:
				till()
			
			if get_pos_x() == 0:
				plant(Entities.Grass)
			elif get_pos_x() == 1:
				if get_pos_y() % 2 == 0:
					plant(Entities.Bush)
				else: 
					plant(Entities.Tree)
			elif get_pos_x() == 2 or 3:
				plant(Entities.Carrot)

			move(North)
		
			
		
		