w_s = get_world_size()

for i in range(w_s):
	if i == 0:
		continue
	move(East)
	for j in range(w_s):
		move(North)
		#if i + 1 == w_s:
			
		
		
		