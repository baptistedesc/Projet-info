<<<<<<< HEAD
#Fonctions pour pouvoir sélectionner une variable avec son nom (comme avec un dictionnaire) 
# plutôt qu'avec son indice, je sais pas encore dans quelle classe mettre ça

class selection:
#On créé la liste des variables
    def __init__(self,dataframe):
        self.dataframe=dataframe

    def nom_variables(self):
        nom_variables=[]
        for i in range(len(self.dataframe)):
            nom_variables.append(self.dataframe[i][0])
        return nom_variables

#On sélectionne la variable recherchée
    def selection_variable(self,variable):
        assert variable in selection.nom_variables(self.dataframe):
        for i in range(len(self.dataframe))
            if self.dataframe[i][0]==variable:
                return self.dataframe[i]

#variables a comme argument une liste composée des variables recherchée, variables = ['population','âge']
#par exemple et renvoie un dataframe composé seulement des colonnes des variables recherchées
    def selection_variables(self,variables):
        variables=[]
        for i in range(len(variables)):
            assert variables[i] in selection.nom_variables(self.dataframe)
            variables.append(selection.selection_variable(self,variables[i]))
        
        
=======
#Fonctions pour pouvoir sélectionner une variable avec son nom (comme avec un dictionnaire) 
# plutôt qu'avec son indice, je sais pas encore dans quelle classe mettre ça

class selection:
#On créé la liste des variables
    def __init__(self,dataframe):
        self.dataframe=dataframe

    def nom_variables(self):
        nom_variables=[]
        for i in range(len(self.dataframe)):
            nom_variables.append(self.dataframe[i][0])
        return nom_variables

#On sélectionne la variable recherchée
    def selection_variable(self,variable):
        assert variable in selection.nom_variables(self.dataframe):
        for i in range(len(self.dataframe))
            if self.dataframe[i][0]==variable:
                return self.dataframe[i]

#variables a comme argument une liste composée des variables recherchée, variables = ['population','âge']
#par exemple et renvoie un dataframe composé seulement des colonnes des variables recherchées
    def selection_variables(self,variables):
        variables=[]
        for i in range(len(variables)):
            assert variables[i] in selection.nom_variables(self.dataframe)
            variables.append(selection.selection_variable(self,variables[i]))
        
        
>>>>>>> 6d986ef1a6b839535f0997ef85a6a31d79cfab26
