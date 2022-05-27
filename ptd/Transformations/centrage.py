from Transformations.transformation import Transformation

class Centrage (Transformation) :
<<<<<<< HEAD
    def __init__ (self) :
=======
    def __init__ (self, table) :
>>>>>>> e774166cca24f91122be2d25ea4bf2e8a1df8ab8
        '''Centre une variable

        Parameters
        ----------
<<<<<<< HEAD
        
        '''
        
=======
        table : table
            La base de données
        '''
        
        self.table=table
>>>>>>> e774166cca24f91122be2d25ea4bf2e8a1df8ab8

    def execute(self,colonne, table) :
        '''Centre la variable demandée 

        Parameters
        ----------
        colonne : str
            Le nom de la variable à centrer
        table : Table
            Le tableau contenant la variable à centrer

        Returns
        -------
        table
            La base de données initiale, avec la variable en question centrée
        ''' 
        
<<<<<<< HEAD
        
        indice = table.nom_colonnes.index(colonne)
        moyenne = 0
        somme = 0
        ecart_moyenne_carre = 0
        somme_ecarts_carre = 0
        for k in range(0,len(table.valeurs[indice])):
            somme = somme + table.valeurs[indice][k]
        moyenne=somme/(len(table.valeurs[indice]))
        for j in range(0,len(table.valeurs[indice])):
                    table.valeurs[indice][j]=table.valeurs[indice][j] - moyenne
        print('MOYENNNNNNNNNNNNE' + str(moyenne))
        return table
=======
        for i in range(len(self.table)) :
            if str(self.table[i][0])==colonne :
                somme=0
                moyenne=0
                for k in range(1,len(self.table[i])):
                    somme = somme + self.table[i][k]
                moyenne=somme/(len(self.table[i])-1)
                for j in range(1,len(self.table[i])):
                    self.table[i][j]=self.table[i][j] - moyenne
        return self.table
>>>>>>> e774166cca24f91122be2d25ea4bf2e8a1df8ab8
