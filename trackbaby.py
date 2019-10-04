# 
# PROJET TRACKBABY
# Programme de suivis de constantes (poids, taille, périmètre cranien) de nourrissons
# 
# Définition des constantes pour les garçons
low_weights_boys = [2.6, 3.6, 4.5, 5.2, 5.8, 6.2, 6.6, 6.9, 7.2, 7.4, 7.7, 7.9, 8.1, 8.2, 8.4, 8.6, 8.8,
8.9, 9.1, 9.3, 9.4, 9.6, 9.8, 9.9, 10.1, 10.2, 10.4, 10.5, 10.7, 10.8, 11, 11.1, 11.2, 11.4, 11.5, 11.6,
11.8, 11.9, 12, 12.2, 12.3, 12.4, 12.5, 12.7, 12.8, 12.9, 13, 13.2, 13.3, 13.4, 13.5, 13.7, 13.8, 13.9, 14,
14.1, 14.3, 14.4, 14.5, 14.6, 14.7]
high_weights_boys = [4.2, 5.5, 6.8, 7.7, 8.4, 9, 9.5, 9.9, 10.3, 10.6, 10.9, 11.2, 11.5, 11.8, 12.1, 12.3, 12.6,
12.9, 13.1, 13.4, 13.6, 13.9, 14.2, 14.4, 14.7, 14.9, 15.2, 15.4, 15.7, 15.9, 16.2, 16.4, 16.6, 16.9, 17.1,
17.3, 17.5, 17.8, 18, 18.2, 18.4, 18.6, 18.9, 19.1, 19.3, 19.5, 19.8, 20, 20.2, 20.4, 20.7, 20.9, 21.1, 21.4,
21.6, 21.8, 22.1, 22.3, 22.5, 22.8, 23]

low_heights_boys = [46.8, 51.5, 55.1, 58.1, 60.5, 62.4, 64.1, 65.6, 67, 68.3, 69.5, 70.7, 71.8, 72.9, 74, 75,
76, 76.9, 77.8, 78.7, 79.6, 80.4, 81.2, 82, 82.8, 82.8, 83.6, 84.3, 85, 85.7, 86.3, 87, 87.6, 88.2, 88.8, 89.4,
90, 90.6, 91.1, 91.7, 92.2, 92.8, 93.3, 93.9, 94.4, 94.9, 95.4, 95.9, 96.4, 96.9, 97.4, 97.9, 98.4, 98.9, 99.4,
99.9, 100.4, 100.9, 101.4, 101.9, 102.3]
high_heights_boys = [53, 57.9, 61.7, 64.8, 67.3, 69.4, 71.1, 72.7, 74.2, 75.7, 77, 78.4, 79.7, 80.9, 82.1, 83.3,
84.5, 85.6, 86.7, 87.8, 88.8, 89.9, 90.9, 91.9, 92.8, 93.1, 94, 94.9, 95.8, 96.7, 97.5, 98.4, 99.2, 99.9, 100.7,
101.4, 102.2, 102.9, 103.6, 104.3, 105, 105.7, 106.4, 107, 107.7, 108.3, 109, 109.6, 110.2, 110.8, 111.5, 112.1,
112.7, 113.3, 113.9, 114.5, 115.2, 115.8, 116.4, 117, 117.6]

low_skulls_boys = [32.4, 35.4, 37.2, 38.6, 39.7, 40.6, 41.3, 42, 42.5, 42.9, 43.3, 43.7, 44, 44.2, 44.4, 44.7, 44.8,
45, 45.2, 45.3, 45.5, 45.6, 45.8, 45.9, 46, 46.1, 46.2, 46.3, 46.5, 46.6, 46.6, 46.7, 46.8, 46.9, 47, 47.1, 47.1, 47.2,
47.3, 47.3, 47.4, 47.4, 47.5, 47.6, 47.6, 47.7, 47.7, 47.8, 47.8, 47.9, 47.9, 47.9, 48, 48, 48.1, 48.1, 48.1, 48.2,
48.2, 48.2, 48.3]
high_skulls_boys = [36.6, 39.2, 41.1, 42.5, 43.6, 44.5, 45.3, 46, 46.6, 47.1, 47.5, 47.9, 48.2, 48.5, 48.7,
49, 49.2, 49.4, 49.6, 49.7, 49.9, 50.1, 50.2, 50.3, 50.5, 50.6, 50.8, 50.9, 51, 51.1, 51.2, 51.3, 51.4, 51.5,
51.6, 51.7, 51.8, 51.9, 52, 52, 52.1, 52.2, 52.2, 52.3, 52.4, 52.4, 52.5, 52.6, 52.6, 52.7, 52.7, 52.8, 52.8,
52.9, 52.9, 53, 53, 53.1, 53.1, 53.2, 53.2]

# Définition des constantes pour les filles
low_weights_girls = [2.5, 3.3, 4.1, 4.7, 5.2, 5.6, 6, 6.3, 6.5, 6.8, 7, 7.2, 7.3, 7.5, 7.7, 7.9, 8.1, 8.2, 8.4,
8.6, 8.7, 8.9, 9.1, 9.2, 9.4, 9.6, 9.8, 9.9, 10.1, 10.2, 10.4, 10.5, 10.7, 10.8, 11, 11.1, 11.3, 11.4, 11.6, 11.7,
11.8, 12, 12.1, 12.2, 12.4, 12.5, 12.6, 12.8, 12.9, 13, 13.2, 13.3, 13.4, 13.5, 13.7, 13.8, 13.9, 14, 14.2, 14.3, 14.4]
high_weights_girls = [4, 5.2, 6.3, 7.2, 7.9, 8.4, 8.9, 9.4, 9.7, 10.1, 10.4, 10.7, 11, 11.3, 11.5, 11.8, 12.1,
12.3, 12.6, 12.9, 13.1, 13.4, 13.6, 13.9, 14.2, 14.4, 14.7, 15, 15.2, 15.5, 15.7, 16, 16.2, 16.5, 16.8, 17, 17.3,
17.5, 17.8, 18, 18.3, 18.6, 18.8, 19.1, 19.3, 19.6, 19.9, 20.1, 20.4, 20.6, 20.9, 21.2, 21.4, 21.7, 22, 22.2, 22.5,
22.7, 23, 23.3, 23.5]

low_heights_girls = [46.1, 50.5, 53.7, 56.3, 58.5, 60.4, 62, 63.5, 64.9, 66.2, 67.4, 68.6, 69.8, 70.9, 72, 73,
74, 75, 75.9, 76.9, 77.7, 78.6, 79.5, 80.3, 81.1, 81.2, 82, 82.7, 83.5, 84.2, 84.9, 85.6, 86.2, 86.9, 87.5,
88.2, 88.8, 89.4, 90, 90.6, 91.2, 91.8, 92.4, 92.9, 93.5, 94, 94.6, 95.1, 95.6, 96.2, 96.7, 97.2, 97.7, 98.2,
98.7, 99.2, 99.7, 100.2, 100.7, 101.1, 101.6]
high_heights_girls = [52.2, 56.9, 60.4, 63.3, 65.7, 67.7, 69.5, 71.1, 72.6, 74.1, 75.5, 76.9, 78.3, 79.5, 80.8,
82, 83.2, 84.4, 85.5, 86.6, 87.7, 88.7, 89.7, 90.7, 91.7, 92, 92.9, 93.8, 94.7, 95.6, 96.5, 97.3, 98.2, 99, 99.8,
100.5, 101.3, 102.1, 102.8, 103.6, 104.3, 105, 105.7, 106.4, 107.1, 107.8, 108.5, 109.2, 109.8, 110.5, 111.1, 111.8,
112.4, 113, 113.6, 114.3, 114.9, 115.5, 116.1, 116.7, 117.2]

low_skulls_girls = [31.9, 34.6, 36.3, 37.5, 38.5, 39.3, 40.1, 40.7, 41.2, 41.6, 42, 42.4, 42.7, 42.9, 43.2, 43.4,
43.6, 43.8, 44, 44.1, 44.3, 44.5, 44.6, 44.7, 44.9, 45, 45.2, 45.3, 45.4, 45.5, 45.6, 45.7, 45.8, 45.9, 46, 46.1,
46.2, 46.3, 46.3, 46.4, 46.5, 46.6, 46.6, 46.7, 46.8, 46.8, 46.9, 46.9, 47, 47.1, 47.1, 47.2, 47.2, 47.3, 47.3, 47.4,
47.4, 47.4, 47.5, 47.5, 47.6]
high_skulls_girls = [35.8, 38.5, 40.2, 41.6, 42.7, 43.6, 44.3, 45, 45.6, 46, 46.4, 46.8, 47.1, 47.4, 47.7, 47.9,
48.1, 48.3, 48.5, 48.7, 48.9, 49, 49.2, 49.3, 49.5, 49.6, 49.8, 49.9, 50, 50.1, 50.2, 50.4, 50.5, 50.6, 50.7, 50.7,
50.8, 50.9, 51, 51.1, 51.2, 51.2, 51.3, 51.4, 51.4, 51.5, 51.6, 51.6, 51.7, 51.7, 51.8, 51.8, 51.9, 51.9, 52, 52,
52.1, 52.1, 52.2, 52.2, 52.3]
#
#
# Fonctions
#  
# vérification valeur entière
def is_number_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False
#
# vérification valeur numérique (entier ou décimal)
def is_number_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
#
# messages pour le poids
def msg_poids(genre1,age1,poids_min1,poids_max1,poids1):
    if genre1 =='g' :
        print(f'La norme de poids pour un garçon de {age1} mois est situé entre {poids_min1}kg et {poids_max1}kg')
    else:
        print(f'La norme de poids pour une fille de {age1} mois est situé entre {poids_min1}kg et {poids_max1}kg')
    if float(poids1)<poids_min1 or float(poids1)>poids_max1:
        print(f'Le poids de votre nourrisson ({poids1}kg) est hors norme')
    else:
        print(f'Le poids de votre nourrisson ({poids1}kg) est dans la norme')
#
# messages pour la taille
def msg_taille(genre2,age2,taille_min2,taille_max2,taille2):
    if genre2 =='g':
        print(f'La norme de taille pour un garçon de {age2} mois est situé entre {taille_min2}cm et {taille_max2}cm')
    else:
        print(f'La norme de taille pour une fille de {age2} mois est situé entre {taille_min2}cm et {taille_max2}cm')
    if float(taille2)<taille_min2 or float(taille2)>taille_max2:
        print(f'La taille de votre nourrisson ({taille2}cm) est hors norme')
    else:
        print(f'La taille de votre nourrisson ({taille2}cm) est dans la norme')
#
# messages pour le périmètre cranien
def msg_cranien(genre3,age3,cranien_min3,cranien_max3,cranien3):
    if genre3 =='g':
        print(f'La norme de perimetre cranien pour un garçon de {age3} mois est situé entre {cranien_min3}cm et {cranien_max3}cm')
    else:
        print(f'La norme de perimetre cranien pour une fille de {age3} mois est situé entre {cranien_min3}cm et {cranien_max3}cm')
    if float(cranien3)<cranien_min3 or float(cranien3)>cranien_max3:
        print(f'Le perimetre cranien de votre nourrisson ({cranien3}cm) est hors norme')
    else:
        print(f'Le perimetre cranien de votre nourrisson ({cranien3}cm) est dans la norme')
#
#
# Bienvenue !
print()
print("Bienvenue dans ce programme de vérification des constantes de votre nourrisson !")
print()
#
# Saisie des informations
# genre : 2 valeurs possibles
while True:
    genre = input ("Entrez le genre de votre nourrisson (g pour garcon, f pour fille) : ")
    if genre == 'g' or genre == 'f':
        break
# age en mois : entier obligatoirement
while True:
    age = input ("Veuillez entrer l'age de votre nourrisson en mois (entre 0 et 60 mois) : ")
    if is_number_int(age)==True:
        break
# poids en kg : numérique obligatoirement
while True:
    poids = input ("Veuillez entrer le poids de votre nourrisson en kg : ")
    if is_number_float(poids)==True:
        break
# taille en cm : numérique obligatoirement
while True:
    taille = input ("Veuillez entrer la taille de votre nourrisson en cm : ")
    if is_number_float(taille)==True:
        break
# périmètre cranien : numérique obligatoirement
while True:
    cranien = input ("Veuillez entrer le perimetre cranien en cm : ")
    if is_number_float(cranien)==True:
        break
# 
print()
#
# recuperation des bornes de la norme et affichage des messages
# garcon puis fille ; poids puis taille puis perimetre cranien
if genre == 'g':
    poids_min=low_weights_boys[int(age)]
    poids_max=high_weights_boys[int(age)]
    msg_poids(genre,age,poids_min,poids_max,poids)
# 
    print()
#
    taille_min=low_heights_boys[int(age)]
    taille_max=high_heights_boys[int(age)]
    msg_taille(genre,age,taille_min,taille_max,taille)
#
    print()
#
    cranien_min=low_skulls_boys[int(age)]
    cranien_max=high_skulls_boys[int(age)]
    msg_cranien(genre,age,cranien_min,cranien_max,cranien)
#
else:
    poids_min=low_weights_girls[int(age)]
    poids_max=high_weights_girls[int(age)]
    msg_poids(genre,age,poids_min,poids_max,poids)
# 
    print()
#
    taille_min=low_heights_girls[int(age)]
    taille_max=high_heights_girls[int(age)]
    msg_taille(genre,age,taille_min,taille_max,taille)
#
    print()
#
    cranien_min=low_skulls_girls[int(age)]
    cranien_max=high_skulls_girls[int(age)]
    msg_cranien(genre,age,cranien_min,cranien_max,cranien)