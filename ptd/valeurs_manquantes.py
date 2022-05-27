import table


class Valeurs_manquantes():
    def __init__(self) -> None:
        pass
    


    def execute(self, colonne, table, methode): #Modifie la table
        indice = table.nom_colonnes.index(colonne)

        if methode == 'mean':
            somme = 0
            moyenne = 0
            for k in range(0,len(table.valeurs[indice])):
                if table.valeurs[indice][k] != 'mq':
                    somme = somme+ table.valeurs[indice][k]
            moyenne = somme/len(table.valeurs[indice])
            for k in range(0,len(table.valeurs[indice])):
                if table.valeurs[indice][k] == 'mq':
                    table.valeurs[indice][k] = moyenne
        return table