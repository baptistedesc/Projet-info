from Transformations.transformation import Transformation
from table import Table


class Jointure(Transformation):
    def __init__(self) :
        ''''''

    def execute(table1,cle1,table2,cle2,type):
        '''Joint les deux tables 

        Parameters
        ----------
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

        # elif type=='inner':
            # Table1=Jointure.execute(table1,cle1,table2,cle2,'left')
            # Table2=Jointure.execute(table1,cle1,table2,cle2,'right')
            # y,z=Table1.nom_colonnes.index(cle1),Table2.nom_colonnes.index(cle2)
            # return y,z
            # for k in range(len(Table1.valeurs[y])):
            #     t=0
            #     for p in range(len(Table2.valeurs[z])):
            #         if Table1.valeurs[y][k]==Table2.valeurs[z][p]:
            #             t=t+1
            #     if t==0:
            #         for x in range(len(Table1.valeurs)):
            #             del Table1.valeurs[x][k]
            # return Table1
                

            



if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
    colonnes1=['fruits','legumes','sante']
    colonnes2=['age','fruits','humeur']
    valeurs1=[['kiwi','poire','abricot'],['haricot','pois','mq'],['bien','pas bien','moyen']]
    valeurs2=[['8 ans','12 ans','7 ans'],['poire','pomme','abricot'],['heureux','pas heureux','moyen heureux']]
    test1=Table(nom_colonnes=colonnes1,valeurs=valeurs1)
    test2=Table(nom_colonnes=colonnes2,valeurs=valeurs2)
    test3=Jointure.execute(test1,'fruits',test2,'fruits','inner')
    Table.afficher(test3)