from distutils.log import error
import csv

class Datatable:
        
    def __init__(self,valeurs,variables):
        self.valeurs=valeurs
        self.variables=variables

    def resume(self):
        resume=[]
        n=len(self.variables)
        for i in range(n):
            resume.append([])
        for i in range(n):
            resume[i].append(self.variables[i])
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
        with open('dataframe.csv','w',newline='') as file:
            writer=csv.writer(file,quoting=csv.QUOTE_ALL,delimiter=';')
            for i in range(len(self.variables)):
                datatable=self.valeurs[:][:]
                datatable[i].insert(0,self.variables[i])
            writer.writerows(datatable)


# Pour tester la fonction chargement (je sais pas comment faire avec le __main__)
# folder = '//filer-eleves.domensai.ecole/id1977/Projet-info/donnees_meteo/'
# filename = 'synop.201301.csv.gz'
# folder = '//filer-eleves.domensai.ecole/id1977/Projet-info/donnees_electricite/'
# filename = '2022-03.json.gz'

# Frac=[['a',2,3],['b',5,6]]
# print(datatable.chargement(Frac,filename,folder))
# print(datatable.resume(Frac))


# datatable.exporter(Frac)


