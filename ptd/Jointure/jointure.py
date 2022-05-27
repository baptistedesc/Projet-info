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
        assert self.cle1==cle2
        self.table1.nom_colonnes.index(cle1)=j1
        table2.nom_colonnes.index(cle2)=j2
        nom_colonnes=self.table1.nom_colonnes+table2.nom_colonnes
        del nom_colonnes[len(self.table1.nom_colonnes+j2)]
        


        for i in range(len(self.table1.nom_colonnes)):
            for j in range(len(table2.nom_colonnes)):
                

        if type=='interne':


        elif type=='gauche':

        elif type=='droite':
        
        elif type=''


        return Table(nom_colonnes,valeurs2)
  


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)