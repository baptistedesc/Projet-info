from Transformations.transformation import Transformation
from table import Table


class Jointure(Transformation):
    def __init__(self) :
        pass

    def execute(table1,cle1,table2,cle2,type):
        '''Joint les deux tables 

        Parameters
        ----------
        table1 : Table
            1ème table
        cle1 :
            Cle de la première table
        table2 : Table
            2ème table
        cle2 :
            Cle de la deuxième table
        '''
        if type=='left':
            temporaire=[]
            i,j=table1.nom_colonnes.index(cle1),table2.nom_colonnes.index(cle2)
            temporaire=table2.valeurs[j]
            del table2.nom_colonnes[j]
            del table2.valeurs[j]
            n=len(table1.valeurs)
            table1.nom_colonnes=table1.nom_colonnes+table2.nom_colonnes
            for u in range(len(table1.valeurs)-1):
                table1.valeurs.append(['mq']*(len(table2.valeurs[j])))
            for k in range(len(table1.valeurs[i])):
                for p in range(len(temporaire)):
                    if table1.valeurs[i][k]==temporaire[p]:
                        for z in range(n,n+len(table2.valeurs)):
                            table1.valeurs[z][k]=table2.valeurs[z-len(table1.valeurs)][p] 
            return table1
        elif type=='right':
            return Jointure.execute(table2,cle2,table1,cle1,'left')
        elif type=='inner':
            temporaire=[]
            i,j=table1.nom_colonnes.index(cle1),table2.nom_colonnes.index(cle2)
            temporaire=table2.valeurs[j]
            del table2.nom_colonnes[j]
            del table2.valeurs[j]
            n=len(table1.valeurs)
            table1.nom_colonnes=table1.nom_colonnes+table2.nom_colonnes
            for u in range(len(table1.valeurs)-1):
                table1.valeurs.append(['mq']*(len(table2.valeurs[j])))
            for k in range(len(table1.valeurs[i])):
                for p in range(len(temporaire)):
                    if table1.valeurs[i][k]==temporaire[p]:
                        for z in range(n,n+len(table2.valeurs)):
                            table1.valeurs[z][k]=table2.valeurs[z-len(table1.valeurs)][p]
            for x in range(len(table1.valeurs[i])):
                if table1.valeurs[i][x] not in table2.valeurs[j]:
                    for y in range(0,len(table1.valeurs)):
                        del table1.valeurs[y][x]
            return table1
            
                

            



if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
    colonnes1=['fruits','legumes','sante']
    colonnes2=['age','fruits','humeur']
    valeurs1=[['kiwi','poire','abricot'],['haricot','pois','mq'],['bien','pas bien','moyen']]
    valeurs2=[['8 ans','12 ans','7 ans'],['poire','pomme','abricot'],['heureux','pas heureux','moyen heureux']]
    test1=Table(nom_colonnes=colonnes1,valeurs=valeurs1)
    Table.afficher(test1)
    test2=Table(nom_colonnes=colonnes2,valeurs=valeurs2)
    Table.afficher(test2)
    # test3=Jointure.execute(test1,'fruits',test2,'fruits','left')
    # Table.afficher(test3)
    # test4=Jointure.execute(test1,'fruits',test2,'fruits','right')
    # Table.afficher(test4)
    # Quand on fait fonctionner test3 et test4 en même temps, ça bug
    test5=Jointure.execute(test1,'fruits',test2,'fruits','inner')
    Table.afficher(test5)