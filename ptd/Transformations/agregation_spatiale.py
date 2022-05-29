from transformation import Transformation
from ptd.table import Table
from ptd.estimateurs.moyenne import Moyenne

class Agregation(Transformation):
      def __init__(self,nom_var_agrege,indication_type_var):
          #Cette classe permet d'agréger selon n'importe quelle variable. Pour une agrégation spatiale, 
          #on agrégera en fonction de la date. Ainsi, toutes les données seront triées par date, peu 
          #importe la région où elles ont été prélevées.
          self.nom_var_agrege = nom_var_agrege
          self.indication_type_var=indication_type_var
# indication_type_var est une liste de plusieurs indication comme ça : 
# ["nom_var","type_var","parametre_type_var"] 

    
      def execute(self,table):
            m1=Moyenne()
            #Récupération des indices des variables
            indice_agrege = table.nom_colonnes.index(self.nom_var_agrege)
            #Opération préliminaire : comptage du nombre de valeurs distincts de la variable 
            # qui va être agregee ainsi que des valeurs
            count = 0  
            l=[]
            for k in range(len(table.valeurs[indice_agrege])):
                  if table.valeurs[k][indice_agrege] not in l :  
                        count += 1
                        l.append(table.valeurs[k][indice_agrege])
            #Opération préliminaire : Création de la table donnees_finales
            donnees_finales = [[0 for k in range(len(self.indication_type_var)) ] for n in range(count)]
            #Agregation des variables
            #triage des données par valeur distincte
            for k in range(len(self.indication_type_var)):
                  for n in range(count):
                        ligne=[]
                        for x in range(len(table.valeurs[indice_agrege])):
                              if table.valeurs[x][indice_agrege]==l[n]:
                                    ligne.append(table.valeurs[x])
                        #En fonction du type de la variable, différente agrégation
                        if self.indication_type_var[k][1]=="quant_int": #on fait la moyenne 
                              donnees_finales[n][k]=m1.execute(table.nom_colonnes[indice_agrege],table)
                       #manque var de types extensive (on fait la somme) !!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            #On ajoute la variable d'agrégation à la fin
            for indice in range(len(donnees_finales)):
                  donnees_finales[indice].insert(0,l[indice])
            nouvelle_donnee=Table([self.nom_var_agrege]+[self.indication_type_var[k][0] for k in range(len(self.indication_type_var))],donnees_finales)
            return nouvelle_donnee
            

nom_colonnes=["poids","euro","temperature"]
valeurs = [[500,10,200],[500,40,400],[1000,10,200],[1000,40,400]]
test=Table(nom_colonnes,valeurs)
agregation=Agregation("poids",[["euro","quant_ext"],["temperature","quant_int",None]])
#l'agregation se fait sur le poids et on a bien définit euro comme variable quantitative extensive 
# et temperature comme variable quantitative intensive et sans variable de pondération
test_agregation=agregation.execute(test)
res=[[500,50,300],[1000,50,300]]