#Ce fichier est conçu pour la SOUTENANCE de projet traitement de donnée
#Elle nous servira à faire une démonstration de notre code.
#Pour ce test, nous avons choisie de prend la variable de type float rafper. EXPLIQUER CE QU EST CETTE VARIABLE



#IMPORTATION des données


from table import Table
from importer import Importer

if __name__ == '__main__':
    folder = '//filer-eleves.domensai.ecole/id1953/Projet-info/donnees_electricite/'
    filename = '2013-01.json.gz' 
    beta=Importer(filename,folder)
    alpha=Importer.lire(beta)
    # table.Table.afficher(alpha)

if __name__ == '__main__':
    folder = '//filer-eleves.domensai.ecole/id1953/Projet-info/donnees_meteo/'
    filename = 'synop.201301.csv.gz'
    beta=Importer(filename,folder)
    electricite=Importer.lire(beta)
    # table.Table.afficher(alpha)
    electricite_stock = electricite #Permet d'afficher conjointement pour montrer les stades d'évolutions dans la boucle for ci dessous
    #(MARCHE PAS)

indice = electricite.nom_colonnes.index('rafper')

#PREMIER AFFICHAGE
print('///////////////////////////////////////////////////////////////////////////')
print("PREMIER AFFICHAGE : Jeux de donnée initial")

for k in range(55,65):
    print(electricite_stock.valeurs[indice][k])



#Test de la classe VALEURS_MANQUANTES:

from valeurs_manquantes import Valeurs_manquantes
indice = electricite.nom_colonnes.index('rafper')
Val_manquante1 = Valeurs_manquantes()
elec_sans_mq = Val_manquante1.execute("rafper", electricite,'mean')
# print(elec_sans_mq.valeurs[indice]) 
elec_sans_mq_stock = elec_sans_mq #Permet d'afficher conjointement pour montrer les stades d'évolutions dans la boucle for ci dessous
 #MARCHE PAS)
#SECOND AFFICHAGE
print("SECOND AFFICHAGE : Jeux de donnée après traitement des données manquantes")
for k in range(55,65):
    print(elec_sans_mq.valeurs[indice][k])


#TEST des classes TRANSFORMATIONS

from operation import Operation
from Transformations.transformation import Transformation
# from Transformations.selection import Selection
from Transformations.centrage import Centrage
from Transformations.reduction import Reduction


#Test des CLASSES CENTRAGE & REDUCTION
c1 = Centrage()
red1 = Reduction()



#Test sur la table elec_sans_mq et sur la variable RAFPER

#TROISIEME AFFICHAGE
elec_sans_mq_rafper_centre = c1.execute('rafper', elec_sans_mq)

print("TROISIEME AFFICHAGE : Jeux de donnée après centrage")
for k in range(55,65): #Cette séquence de valeur contient des valeurs manquantes : démonstration
    print(elec_sans_mq_rafper_centre.valeurs[indice][k])



#QUATRIEME AFFICHAGE
elec_sans_mq_rafper_centre_reduit = red1.execute('rafper', elec_sans_mq)

print("QUATRIEME AFFICHAGE : Jeux de donnée après centrage et reduction") #PROBLEME REDUCTION RENVOI SOUS FORME DE COMPLEXE
for k in range(55,65): #Cette séquence de valeur contient des valeurs manquantes : démonstration
    print(elec_sans_mq_rafper_centre_reduit.valeurs[indice][k])


#//////////////////////////////////////////////////////////////////////////////////////////////////
#TEST des classes ESTIMATEURS
#//////////////////////////////////////////////////////////////////////////////////////////////////
from Estimateurs.moyenne import Moyenne

#On change de variable, prenons : 

m1 = Moyenne()
print("Test des classes Moyenne, Variance, Ecart-type")


indice = electricite.nom_colonnes.index('phenspe1')
#traitement des données manquantes :
elec_sans_mq = Val_manquante1.execute("phenspe1", electricite,'mean')

for k in range(55,65): #Cette séquence de valeur contient des valeurs manquantes : démonstration
    print(elec_sans_mq_rafper_centre_reduit.valeurs[indice][k])
print("La moyenn est:")
print(m1.execute('phenspe1',elec_sans_mq))
