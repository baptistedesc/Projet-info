


#IMPORTATION des données


from statistics import variance
from matplotlib.pyplot import boxplot
from table import Table
from importer import Importer
from valeurs_manquantes import Valeurs_manquantes
from operation import Operation
from Transformations.transformation import Transformation
from Transformations.centrage import Centrage
from Transformations.reduction import Reduction
from Transformations.jointure import Jointure
from Estimateurs.moyenne import Moyenne
from Estimateurs.variance import Variance
from Estimateurs.sd import Sd
from Graphiques.graphique import Graphique
from Graphiques.boxplot import Boxplot




if __name__ == '__main__':
    folder = '//filer-eleves.domensai.ecole/id1953/Projet-info/donnees_electricite/'
    filename = '2013-01.json.gz' 
    beta=Importer(filename,folder)
    electricite=Importer.lire(beta)
    # table.Table.afficher(alpha)

if __name__ == '__main__':
    folder = '//filer-eleves.domensai.ecole/id1953/Projet-info/donnees_meteo/'
    filename = 'synop.201301.csv.gz'
    beta=Importer(filename,folder)
    meteo=Importer.lire(beta)

#Question 1 : Y'a t-il une relation entre température et consommation d'énérgie ?
#Faire un inner-join pour que la statiscticien puisse accéder à toutes les variables simultanément.

#Le vent joue-t-il un rôle dans cette consommation?
#Centré et réduire?

print(meteo.resume())

#Peut-on observer des tendances à long terme pour la consommationé lectrique régionale ou nationale?
#Utilisations de la classe agrégation spatiale pour changer de granularité.
#Création de deucx nouveaux jeux de donnée: Le premier aura des données à l'échelle nationnale et le second sera à l'échelle régionale.


#— Observe-t-on des disparités régionales pour la relation entre température et consommation?
