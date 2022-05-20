from Importer import importer
from distutils.log import error
import csv

class Datatable:
        
    def __init__(self):

    def chargement(self,filename,folder):
        self.datatable=importer.lire(filename,folder)

    def resume(self):
        resume=[]
        n=len(self.datatable)
        for i in range(n):
            resume.append([])
        for i in range(n):
            resume[i].append(self.datatable[i][0])
            resume[i].append(type(self.datatable[i][1]))
        s=0
        f=0
        for i in range(n):
                if resume[i][1] is str:
                    s=s+1
                f=f+1
        print('Il y a ' + str(s) + ' variables str et ' + str(f) + ' variables numériques soit ' + str(s+f) +' variables.')
        return resume

    def exporter(self):
        with open('dataframe.csv','w',newline='') as file:
            writer=csv.writer(file,quoting=csv.QUOTE_ALL,delimiter=';')
            writer.writerows(self.datatable)


# Pour tester la fonction chargement (je sais pas comment faire avec le __main__)
# folder = '//filer-eleves.domensai.ecole/id1977/Projet-info/donnees_meteo/'
# filename = 'synop.201301.csv.gz'
folder = '//filer-eleves.domensai.ecole/id1977/Projet-info/donnees_electricite/'
filename = '2022-03.json.gz'

Frac=[['a',2,3],['b',5,6]]
# print(datatable.chargement(Frac,filename,folder))
# print(datatable.resume(Frac))


datatable.exporter(Frac)

