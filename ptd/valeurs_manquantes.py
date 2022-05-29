from ptd.table import Table

class Valeurs_manquantes():
    def __init__(self) -> None:
        pass
    


    def execute(colonne, table, methode): #Modifie la table
        indice = table.nom_colonnes.index(colonne)

        if methode == 'mean':
            somme = 0
            moyenne = 0
            t=0
            for k in range(0,len(table.valeurs[indice])):
                if table.valeurs[indice][k] != 'mq':
                    somme = somme+ table.valeurs[indice][k]
                if table.valeurs[indice][k]=='mq':
                    t=t+1
            moyenne = somme/(len(table.valeurs[indice])-t)
            for k in range(0,len(table.valeurs[indice])):
                if table.valeurs[indice][k]=='mq':
                    table.valeurs[indice][k] = moyenne
        return table


if __name__ == '__main__':
    nom_colonnes=['fruits','legumes']
    valeurs=[['pomme','poire','pomme','poire'],[8,'mq',8,8]]
    table=Table(nom_colonnes,valeurs)
    alpha=Valeurs_manquantes.execute('legumes',table,'mean')
    Table.afficher(alpha)
