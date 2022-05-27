from ptd.transformations.transformation import Transformation
from ptd.transformations.selection import Selection
from ptd.table import Table


class Jointure(Transformation):
    def __init__(self,table1) :
        '''
        Parameters
        ----------
        table1 : Table
            Première table
        
        '''
        self.table1=table1

    def execute(self,cle1,table2,cle2):
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
        #Notations
        i,j=self.table1.nom_colonnes.index(cle1),table2.nom_colonnes.index(cle2)
        valeurs1,valeurs2=self.table1.valeurs,table2.valeurs
        colonnes1,colonnes2=self.table1.nom_colonnes,table2.nom_colonnes
        colonnes=colonnes1+colonnes2
        #On ajoute des colonnes de valeurs manquantes à valeurs1
        q=len(valeurs2[0])*['mq']
        for u in range(len(colonnes2)-1):
            valeurs1.append([q])
        indices=[]
        #On fait la jointure pour les valeurs communes des clés1 et clés2
        for p in range(len(valeurs1[0])):
            for k in range(len(valeurs2[0])):
                if valeurs1[i][k]==valeurs2[j][p]:
                    for x in range(len(colonnes1),len(colonnes1)+len(colonnes2)):
                        if (x-len(colonnes1))!=j:
                            valeurs1[x][k]=valeurs2[x-len(colonnes1)][p]
                        pass
            indices.append[p]
        #On fait ensuite la jointure pour les valeurs non communes
        for y in range(len(valeurs1)):
            for s in range(len(valeurs2)):
                for z in range(indices):
                    valeurs1[i].append(valeurs2[j][z])
                    if y<len(colonnes1) and y!=i:
                        valeurs1[y].append('mq')
                    elif s!=i:
                         valeurs1[y].append(valeurs2[s][z])
        del colonnes[len(self.table1.nom_colonnes)+i]

        return Table(colonnes,valeurs1)
  


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
    colonnes=['fruits','âge']
    valeurs1=[['pomme','poire'],['haricot','pois']]
    valeurs2=[['pomme','poire'],['8 ans','12 ans']]
    test1=Table(nom_colonnes=colonnes,valeurs=valeurs1)
    test2=Table(nom_colonnes=colonnes,valeurs=valeurs2)
    test3=Jointure.execute(test1,'fruits',test2,'fruits')
    Table.afficher(test3)