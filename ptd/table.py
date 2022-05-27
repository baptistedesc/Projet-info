from distutils.log import error
import csv

def transpose(l1):
    l2=[]
    for i in range(len(l1[0])):
        row =[]
        for item in l1:
            row.append(item[i])
        l2.append(row)
    return l2


class Table:
    '''
    >>> nom_colonnes=['fruits','légumes']
    >>> variables=[[1,2],[3,4]]
    >>> alpha=Table(nom_colonnes,variables)
    >>> Table.resume(alpha)
    Il y a 0 variables str et 2 variables numériques soit 2 variables.
    [['fruits', <class 'int'>], ['légumes', <class 'int'>]]
    ''' 
    def __init__(self,nom_colonnes,valeurs):
        self.nom_colonnes=nom_colonnes
        self.valeurs=valeurs

    def afficher(self):
        print(self.nom_colonnes)
        print(self.valeurs)
    def resume(self):
        resume=[]
        n=len(self.valeurs)
        for i in range(n):
            resume.append([])
        for i in range(n):
            resume[i].append(self.nom_colonnes[i])
            resume[i].append(type(self.valeurs[i][0]))
        s=0
        f=0
        for i in range(n):
                if resume[i][1] is str:
                    s=s+1
                f=f+1
        print('Il y a ' + str(s) + ' variables str et ' + str(f) + ' variables numériques soit ' + str(s+f) +' variables.')
        return resume

    def exporter(self):
        with open('table.csv','w',newline='') as file:
            writer=csv.writer(file,quoting=csv.QUOTE_ALL,delimiter=';')
            for i in range(len(self.nom_colonnes)):
                datatable=self.valeurs[:][:]
                datatable[i].insert(0,self.nom_colonnes[i])
            dataframe=transpose(datatable)
            writer.writerows(dataframe)


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
    nom_colonnes=['fruits','légumes']
    valeurs=[[1,2],[3,4]]
    Objet=Table(nom_colonnes,valeurs)
    Table.exporter(Objet)

*