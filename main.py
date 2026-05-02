def back(x=0, y=0):
	while x != get_pos_x() or y != get_pos_y():
		if (get_pos_x() < x):
			move(East)
		else:
			move(West)
		if (get_pos_y() < y):
			move(North)
		else:
			move(South)

def _back(x=0, y=0):
	while x != get_pos_x() or y != get_pos_y():
		if (get_pos_x() != x):
			move(West)
		if (get_pos_y() != y):
			move(South)

def _select(entity=None):
	if entity == "Cactus":
		if get_ground_type() == Grounds.Grassland:
			till()
		plant(Entities.Cactus)
	if entity == "Carrot":
		if get_ground_type() != Grounds.soil:
			till()
		plant(Entities.Carrot)
	if entity == "Pumpkin":
		if get_ground_type() == Grounds.Grassland:
			till()
		while get_entity_type() != Entities.Pumpkin:
			plant(Entities.Pumpkin)
			use_item(Items.Fertilizer)
			while not can_harvest() and get_entity_type() != Entities.Dead_Pumpkin:
				continue
	if entity == "Tree":
		plant(Entities.Tree)

def reverse(dir):
	if (dir == West):
		return East
	if (dir == East):
		return West
	if (dir == North):
		return South
	if (dir == South):
		return North

def _plant(entity, x, y, size=11):
	for i in range(size):
		for j in range(size):
			use_item(Items.Water)
			_select(entity)
			if (j != size - 1):
				move(x)
		if (i != size - 1):
			move(y)
		x = reverse(x)

def initFarm():
	eDir = East
	nDir = North
	wDir = West
	sDir = South
	size = 8
	
	while True:
		sorted = False
		vsorted = False

		_plant("Pumpkin", eDir, nDir)
		move(nDir)

		_plant("Pumpkin", eDir, nDir)
		move(wDir)

		_plant("Pumpkin", wDir, sDir)
		move(sDir)

		_plant("Pumpkin", wDir, sDir)

		_back()
		break

	while True:
		for i in range(get_world_size()):
			if can_harvest():
				harvest()
			elif get_entity_type() == Entities.Dead_Pumpkin:
				_plant("Pumpkin", eDir, nDir)
			move(North)
		move(East)
		if get_ground_type() != Grounds.Soil:
			continue

while True:
	clear()
	initFarm()
