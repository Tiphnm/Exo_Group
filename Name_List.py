#!/usr/bin/env python 
# coding=utf-8
import random 
import logging
import json 

logging.basicConfig(filename='text.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

logging.info("getting text file: start")
my_file = open("Name_List", "r")
name_list= my_file.read()
logging.info("getting text file: end")


logging.info("Splitting my file into a list: start")
my_list = name_list.split(" ")
logging.info("Splitting my file into a list: end")

person_per_group = 2
nb_groups = int((len(my_list)) / person_per_group)

logging.info("Creating my final list of group in Json: start")
group = open("My_group.json", "a")

def final_list(person_per_group, nb_groups):
    d = dict()
   
    for i in range(nb_groups):
        selected = random.sample(my_list, int(person_per_group))
        d['Groupe'] = selected 
        logging.info(d)
        print(d)

        for sel in selected:
            my_list.remove(sel)

        json.dump(d, group, indent = 3, sort_keys = False)

logging.info("Executing my function: start")
final_list(person_per_group, nb_groups)
logging.info("Executing my function: end")

group.close()
logging.info("Creating my final list of group in Json: end")


#Penser à faire d'autres logs ex-> et si je n'arrive pas à trouver une liste, quel message afficher ? 
#Format json, j'ai fait plusieurs json dans mon json, chaque groupe et deux noms sont un unique dictionnaire. Du coup au lieu d'avoir 1 dictionnaire j'en ai plusieurs. 
#Faire avec un person_per_group qui change 

''' Intro classe en python 
Les classes en Python commencent toujours par une majuscule
Avant de déclarer la classe on le note ainsi -> class Students : 
Les classes me permettent de déclarer de manière globale dans un fichier mes variables (def __init__(self)) et aussi les fonctions qui va me rendre mon résultats. 
Du coup j'ai un fichier avec ma logique et un autre fichier livrable et claire qui appelle simplement mes fonctions avec des variables prédéfinies 
'''

'''
Packaging (ici appeler son fichier directement dans sa console sans écrire python)
Faire la structure de son dossier (ex: dossier parent Test Pack avec un fichier setup.py (ttes les infos de mon programme comme version auteur nom et aussi comment je vais l'appeler dans ma consoleetc), 
ensuite dossier children Mon jeu avec mon fichier.py et un fichier __init__.py(prend mes librairies))

les étapes à faire dans la console : $ sudo python3 setup.py install

regarder sur la doc python mais attention pas de entry points dans la doc .... fair en sorte de la rajouter 
'''