def calcul_nb_voisins(Z):
	"""Calcul du nombre de voisins vivants."""
	forme = len(Z), len(Z[0])
	N = [[0, ] * (forme[0]) for i in range(forme[1])]
	for x in range(1, forme[0] - 1):
		for y in range(1, forme[1] - 1):
			N[x][y] = Z[x-1][y-1] + Z[x][y-1] + Z[x+1][y-1] \
					+ Z[x-1][y] +	 0			+ Z[x+1][y] \
					+ Z[x-1][y+1] + Z[x][y+1] + Z[x+1][y+1]
	return N





def iteration_jeu(Z):
	"""Entrée : Prend en argument une liste de (listes) représentant l'état initial du jeu. 
	Sortie : Retourne une liste de listes correspondant à l'état du jeu à l'étape suivante .

	Pour chaque cellule qui n'est pas sur le pourtour de la grille, 
	iteration_jeu détermine le nouvel état de la cellule (vivante ou morte)
	en fonction de son nombre de voisins vivants.

	Une cellule morte avec trois voisins vivants exactement nait.
	Une cellule vivante ayant deux ou trois voisins vivants reste en vie.
	Une cellule vivante ayant au moins quatre voisins vivants meurt.
	Une cellule vivante ayant zero ou un voisin vivant meurt."""

	forme = len(Z), len(Z[0])
	N = calcul_nb_voisins(Z)
	for x in range(1,forme[0]-1):
		for y in range(1,forme[1]-1):
			if Z[x][y] == 1 and (N[x][y] < 2 or N[x][y] > 3):
				Z[x][y] = 0
			elif Z[x][y] == 0 and N[x][y] == 3:
				Z[x][y] = 1
	return Z





@jit(nopython=True)
def calcul_nb_voisins_jit(Z):
	"""Calcul du nombre de voisins vivants."""
	forme = len(Z), len(Z[0])
	N = [[0, ] * (forme[0]) for i in range(forme[1])]
	for x in range(1, forme[0] - 1):
		for y in range(1, forme[1] - 1):
			N[x][y] = Z[x-1][y-1] + Z[x][y-1] + Z[x+1][y-1] \
					+ Z[x-1][y] +	 0			+ Z[x+1][y] \
					+ Z[x-1][y+1] + Z[x][y+1] + Z[x+1][y+1]
	return N






@jit(nopython=True)
def iteration_jeu_jit(Z):
	"""Entrée : Prend en argument une liste de (listes) représentant l'état initial du jeu. 
	Sortie : Retourne une liste de listes correspondant à l'état du jeu à l'étape suivante .

	Pour chaque cellule qui n'est pas sur le pourtour de la grille, 
	iteration_jeu détermine le nouvel état de la cellule (vivante ou morte)
	en fonction de son nombre de voisins vivants.

	Une cellule morte avec trois voisins vivants exactement nait.
	Une cellule vivante ayant deux ou trois voisins vivants reste en vie.
	Une cellule vivante ayant au moins quatre voisins vivants meurt.
	Une cellule vivante ayant zero ou un voisin vivant meurt."""

	forme = len(Z), len(Z[0])
	N = calcul_nb_voisins_jit(Z)
	for x in range(1,forme[0]-1):
		for y in range(1,forme[1]-1):
			if Z[x][y] == 1 and (N[x][y] < 2 or N[x][y] > 3):
				Z[x][y] = 0
			elif Z[x][y] == 0 and N[x][y] == 3:
				Z[x][y] = 1
	return Z
