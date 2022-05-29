from ptd.transformations.transformation import Transformation
from ptd.table import Table

def transpose(l1):
    l2=[]
    for i in range(len(l1[0])):
        row =[]
        for item in l1:
            row.append(item[i])
        l2.append(row)
    return l2

def enlever_individus(liste, indexs):
            '''Supprime d'une liste les individus d'indexs spécifiés

            Parameters
            ----------
            liste: list
                Liste de listes a transposer
            
            Returns
            -------
            list
                Liste sans les individus d'indexs spécifiés
            
            Examples
            --------
            >>> maliste = [1, 2, 3, 4]
            >>> enlever_individus(maliste, 0)
            [2, 3, 4]
            '''

            resultat = []
            for i in range(len(liste)):
                if not i in indexs:
                    resultat.append(liste[i])
            return resultat

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
            # Transposition
            indice1 = [table1.nom_colonnes.index(cle1)]
            indice2 = [table2.nom_colonnes.index(cle2)]
            lignes_table1 = transpose(table1.valeurs)
            lignes_table2 = transpose(table2.valeurs)

            # Nlle table
            nv_variables = table1.nom_colonnes + enlever_individus(table2.nom_colonnes, indice2)
            nv_lignes = []

            # Remplissage de la table
            for ligne1 in lignes_table1:
                for ligne2 in lignes_table2:
                    if [ligne1[indice1[i]] == ligne2[indice2[i]] for i in range(len(indice1))] == [True] * len(indice1):
                        nv_lignes.append(ligne1 + enlever_individus(ligne2, indice2))
        
            nv_valeurs = transpose(nv_lignes)
            return Table(nv_variables, nv_valeurs)

         
            



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