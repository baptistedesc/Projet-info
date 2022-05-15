#Fonctions pour pouvoir sélectionner une variable avec son nom (comme avec un dictionnaire) 
# plutôt qu'avec son indice, je sais pas encore dans quelle classe mettre ça

#On créé la liste des variables
def nom_variables(dataframe):
    nom_variables=[]
    for i in range(len(dataframe)):
        nom_variables.append(dataframe[i][0])

#On sélectionne la variable recherchée
def selection_variable(dataframe,variable):
    assert variable in nom_variables(dataframe):
    for i in range(len(dataframe)):
        if dataframe[i][0]==variable:
            return dataframe[i]
