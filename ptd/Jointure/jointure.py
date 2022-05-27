from ptd.table import Table

class Jointure():
    '''
    Examples
    -----------------

    '''
    def __init__(self,table1,cle1) :
        '''
        cle1=nom de la variable qui sert de clé
        '''
        self.table1=table1
        self.cle1=cle1

    def execute(self,table2,cle2,type):
        nom_colonnes=self.table1.nom_colonnes+table2.nom_colonnes
        i,j=self.table1.nom_colonnes.index(self.cle1),table2.nom_colonnes.index(cle2)
        valeurs1,valeurs2=self.table1.valeurs,table2.valeurs
        colonnes1,colonnes2=self.table1.nom_colonnes,table2.nom_colonnes
        nom_colonnes=colonnes1+colonnes2
        q=len(valeurs2[0])*['mq']
        for u in range(len(colonnes2)-1):
            valeurs1.append([q])
        indices=[]
        for p in range(len(valeurs1[0])):
            for k in range(len(valeurs2[0])):
                if valeurs1[i][k]==valeurs2[j][p]:
                    for x in range(len(colonnes1),len(colonnes1)+len(colonnes2)):
                        if (x-len(colonnes1))!=j:
                            valeurs1[x][k]=valeurs2[x-len(colonnes1)][k]
                        pass
            indices.append[p]
        for y in range(len(valeurs1)):
            for s in range(len(valeurs2)):
                for z in range(indices):
                    valeurs1[i].append(valeurs2[j][z])
                    if y<len(colonnes1) and y!=i:
                        valeurs1[y].append('mq')
                    elif s!=i:
                         valeurs1[y].append(valeurs2[s][z])
        del nom_colonnes[len(self.table1.nom_colonnes)+i]

        return Table(nom_colonnes,valeurs1)
  


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
