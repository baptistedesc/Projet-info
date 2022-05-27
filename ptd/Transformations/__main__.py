from ptd .transformations.selection import Selection
from ptd.table import Table
nom_colonnes=['fruits','légumes']
valeurs=[[1,2],[3,4]]
Objet=Table(nom_colonnes,valeurs)
fruits=Selection()
fruits.execute(Objet,'fruits')
print(fruits)