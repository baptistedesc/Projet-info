from ptd.table import Table

class Agregation_temp():

    def __init__(self) :
        pass

    def execute(table1,table2):
        nv_donnees=[]
        assert (table1.nom_colonnes==table2.nom_colonnes)
        for i in range(len(table1.valeurs)):
            for j in range(len(table2.valeurs[i])):
                table1.valeurs[i].append(table2.valeurs[i][j])
        nv_table=Table(table1.nom_colonnes,table1.valeurs)
        return nv_table


if __name__ == '__main__':
    nom_colonnes=['fruits','legumes']
    valeurs1=[['pomme','poire'],['haricot','pois']]
    valeurs2=[['fraise','framboise'],['poireau','tomate']]
    table1=Table(nom_colonnes,valeurs1)
    table2=Table(nom_colonnes,valeurs2)
    table=Agregation_temp.execute(table1,table2)
    Table.afficher(table)
