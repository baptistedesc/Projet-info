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

    def __init__(self,nom_colonnes,valeurs):
        self.nom_colonnes=nom_colonnes
        self.valeurs=valeurs

    def afficher(self):
        '''
        Affiche les n premières lignes de la table
        '''
        print(self.nom_colonnes)
        print(self.valeurs)

    def afficher_n (self,n):
        '''
        Affiche les n premières lignes de la table
        '''
        print(self.nom_colonnes)
        valeurs=[]
        for i in range(len(self.nom_colonnes)):
            valeurs.append(self.valeurs[i][0:n])
        print(valeurs)

    def resume(self):
        resume=[]
        n=len(self.valeurs)
        for i in range(n):
            resume.append([])
        for i in range(n):
            resume[i].append(self.nom_colonnes[i])
            j=0
            while j<len(self.valeurs[i]):
                if self.valeurs[i][j]!='mq':
                    resume[i].append(type(self.valeurs[i][j]))
                    break
                else: 
                    j=j+1
        s=0
        f=0
        for i in range(n):
                if resume[i][1] is str:
                    s=s+1
                else:
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
    nom_colonnes=['fruits','légumes']
    valeurs=[[1,2],[3,4]]
    Objet=Table(nom_colonnes,valeurs)
    Table.exporter(Objet)
    nom_colonnes0=['fruits','légumes','age','route']
    valeurs0=[['mq','mq',1,2,4,5],[3,4,'mq','mq',8,17],['8 ans','12 ans','12 ans','12 ans','12 ans','12 ans'],['du bois','de la rivière','12 ans','12 ans','12 ans','12 ans']]
    alpha0=Table(nom_colonnes0,valeurs0)
    Table.resume(alpha0)
    Table.afficher_n(alpha0,3)

