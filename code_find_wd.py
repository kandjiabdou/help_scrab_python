import json
import itertools
from time import time
tic = time()
with open("C:/Users/abdou/DisqueD/informatique/python/scrable/dictionnaire_liste_mots.js","r") as dico:
	dictionnaire = json.load(dico)
	dico.close()
l="kandji"
l=l.lower()
scores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
         "f": 4, "i": 1, "h": 4, "k": 10 , "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
         "x": 10, "z": 10}

def calc_score(word):
    """Calculate the score of a given word."""
    word_score = 0
    for x in word:
        word_score += scores[x]
    return word_score

tab = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
compteur=0
i = 2
while i < len(l) + 1:
	for c in itertools.combinations(l, i):
		for p in itertools.permutations(c):
			mot = ""
			j = 0
			while j < len(p):
				mot += p[j]
				j += 1
			if mot in dictionnaire[mot[0]][mot[1]][str(len(mot))]:
				tab[len(mot)].append(mot)
				compteur+=1
	i += 1
print("###############")
print("\033[34mIl y a \033[m\033[31m",compteur,"\033[m\033[34mmots trouvés avec la chaine",'"',l,'"\033[m')

les_meilleurs_mots=["","",""]
les_meilleurs_pt=[0,0,0]
def get_ind_min(tab):
	i=0
	min=max(tab)
	ind=-1
	while i<len(tab):
		if tab[i]<min:
			min=tab[i]
			ind=i
		i+=1
	return ind

for tb in reversed(tab):
	if len(tb)!=0:
		r="\033[m\t\t\t\t\033[34m"+str(len(tb))+" mots à "+ str(len(tb[0]))+ " lettres :\033[m\n"
		for wd in tb:
			r+="\033[30m"+wd+" ("+str(calc_score(wd))+"), "

			if calc_score(wd)>min(les_meilleurs_pt) and wd not in les_meilleurs_mots:
				les_meilleurs_mots[get_ind_min(les_meilleurs_pt)] = wd
				les_meilleurs_pt[get_ind_min(les_meilleurs_pt)]=calc_score(wd)
		print(r)

resultat_des_m="\033[32mLes meilleurs mots trouvés sont:"
i=len(les_meilleurs_pt)-1
while i>=0:
	resultat_des_m+=" "+les_meilleurs_mots[i]+" ("+str(les_meilleurs_pt[i])+"), "
	i-=1
resultat_des_m+="\033[m"
print(resultat_des_m)
tac=time()
print("Exécution en",round(tac-tic,2),"s")

