


#IMPORTATION des données


from statistics import variance
from matplotlib.pyplot import boxplot
from table import Table
from importer import Importer
from valeurs_manquantes import Valeurs_manquantes
from operation import Operation
from transformations.transformation import Transformation
from transformations.centrage import Centrage
from transformations.reduction import Reduction
from transformations.jointure import Jointure
from estimateurs.moyenne import Moyenne
from estimateurs.variance import Variance
from estimateurs.sd import Sd
from graphiques.graphique import Graphique
from graphiques.boxplot import Boxplot




if __name__ == '__main__':
    folder = '//filer-eleves.domensai.ecole/id1977/Projet-info/donnees_electricite/'
    filename = '2013-01.json.gz' 
    alpha=Importer(filename,folder)
    electricite=Importer.lire(alpha)

if __name__ == '__main__':
    folder = '//filer-eleves.domensai.ecole/id1977/Projet-info/donnees_meteo/'
    filename = 'synop.201301.csv.gz'
    beta=Importer(filename,folder)
    meteo=Importer.lire(beta)

#Question 1 : Y'a t-il une relation entre température et consommation d'énérgie ?
#Faire un inner-join pour que la statiscticien puisse accéder à toutes les variables simultanément.

# table=Jointure.execute(electricite,cle1,meteo,cle2,type)

Table.afficher_n(electricite,2)
Table.afficher_n(meteo,2)

#On doit faire une jointure entre les deux tables. Comme clé, il faut prendre le doublet (date, région) comme clé.
#Pour la table météo, nous ne disposons des données qu'au niveau des stations donc il faut faire une agrégation spatiale
#au niveau régional. Ensuite, il faut réaliser la jointure entre les deux tables puis ne conserver que les 
#colonnes [région, date, température, consommation d'électricité] avec la méthode sélection

#Le vent joue-t-il un rôle dans cette consommation?
#Centré et réduire?

# print(meteo.resume())

#Peut-on observer des tendances à long terme pour la consommationé lectrique régionale ou nationale?
#Utilisations de la classe agrégation spatiale pour changer de granularité.
#Création de deucx nouveaux jeux de donnée: Le premier aura des données à l'échelle nationnale et le second sera à l'échelle régionale.


#— Observe-t-on des disparités régionales pour la relation entre température et consommation?
