def calcul_nb_voisins(Z):
	"""

	Calcul du nombre de voisins vivants.

	Entrée: Prend en argument une liste (de liste) qui 
        représente la "carte" du jeu de la vie.
    	Sortie: Renvoie le nombre de voisins vivants de chaque cellule.

    """

	
	forme = len(Z), len(Z[0])
	N = [[0, ] * (forme[0]) for i in range(forme[1])]
	for x in range(1, forme[0] - 1):
		for y in range(1, forme[1] - 1):
			N[x][y] = Z[x-1][y-1] + Z[x][y-1] + Z[x+1][y-1] \
					+ Z[x-1][y] +	 0			+ Z[x+1][y] \
					+ Z[x-1][y+1] + Z[x][y+1] + Z[x+1][y+1]
	return N





def iteration_jeu(Z):
	"""

	Entrée : Prend en argument une liste de (listes) représentant l'état initial du jeu. 
	Sortie : Retourne une liste de listes correspondant à l'état du jeu à l'étape suivante .

	Pour chaque cellule qui n'est pas sur le pourtour de la grille (considéré toujours mort), 
	iteration_jeu détermine le nouvel état de la cellule (vivante ou morte)
	en fonction de son nombre de voisins vivants, calculé par la fonction calcul_nb_voisins.

	Une cellule morte avec trois voisins vivants exactement nait (naissance).
	Une cellule vivante ayant deux ou trois voisins vivants reste en vie (équilibre).
	Une cellule vivante ayant au moins quatre voisins vivants meurt par étouffement.
	Une cellule vivante ayant zero ou un voisin vivant meurt par isolement.

	"""

	forme = len(Z), len(Z[0])
	N = calcul_nb_voisins(Z)
	for x in range(1,forme[0]-1):
		for y in range(1,forme[1]-1):
			if Z[x][y] == 1 and (N[x][y] < 2 or N[x][y] > 3):
				Z[x][y] = 0
			elif Z[x][y] == 0 and N[x][y] == 3:
				Z[x][y] = 1
	return Z




from numba import jit

@jit(nopython=True)
def calcul_nb_voisins_jit(Z):
	"""

	Calcul du nombre de voisins vivants.

	Entrée: Prend en argument une liste (de liste) qui 
        représente la "carte" du jeu de la vie.
    	Sortie: Renvoie le nombre de voisins vivants de chaque cellule.

	"""
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
	"""

	Entrée : Prend en argument une liste de (listes) représentant l'état initial du jeu. 
	Sortie : Retourne une liste de listes correspondant à l'état du jeu à l'étape suivante .

	Pour chaque cellule qui n'est pas sur le pourtour de la grille (considéré toujours mort), 
	iteration_jeu détermine le nouvel état de la cellule (vivante ou morte)
	en fonction de son nombre de voisins vivants, calculé par la fonction calcul_nb_voisins.

	Une cellule morte avec trois voisins vivants exactement nait (naissance).
	Une cellule vivante ayant deux ou trois voisins vivants reste en vie (équilibre).
	Une cellule vivante ayant au moins quatre voisins vivants meurt par étouffement.
	Une cellule vivante ayant zero ou un voisin vivant meurt par isolement.

	"""

	forme = len(Z), len(Z[0])
	N = calcul_nb_voisins_jit(Z)
	for x in range(1,forme[0]-1):
		for y in range(1,forme[1]-1):
			if Z[x][y] == 1 and (N[x][y] < 2 or N[x][y] > 3):
				Z[x][y] = 0
			elif Z[x][y] == 0 and N[x][y] == 3:
				Z[x][y] = 1
	return Z







import numpy as np
import matplotlib.pyplot as plt
import math

def affichage_jeu(Etat_jeu, Iteration = 0):
	"""

	Entrée : Prend en arguments un np.array représentant l'état du jeu de la vie
			et un nombre d'itérations du jeu à réaliser.

	affichage_jeu effectue le nombre d'itérations du jeu de la vie
	à partir de l'état renseigné et affiche l'état obtenu du jeu.

	"""

	Z_iter = np.copy(Etat_jeu)
	plt.figure(figsize = (10, 5))

	for i in range(Iteration):
		Z_iter = iteration_jeu(Z_iter)

	plt.imshow(Z_iter)
	plt.title("Etape " + str(Iteration) + " du jeu de la vie")





def fig_digit(x_init, w_regression, alpha = 0.1):
	"""

	Entrées : fit_digit prend en arguments le vecteur codant l'image initiale : x_init,
			le vecteur w contenant les coefficients obtenus par la régression : w_regression,
			un réel alpha.

	fit_digit affiche l'image de x_init, transformée par l'opération suivante :
	x_mod = x_init - alpha * ((w_regression^T * x_init) / norme(w_regression)**2) * w_regression.

	"""

	x_mod = x_init.reshape(784, 1) - alpha * (np.dot(w_regression.T, x_init.reshape(784, 1)) * w_regression) / np.linalg.norm(w_regression)**2

	plt.imshow(x_mod.reshape(28, 28))
	plt.title("Image transformée")

