from Transformations.transformation import Transformation

class Centrage (Transformation) :
    def __init__ (self) :
        '''Centre une variable

        Parameters
        ----------
        
        '''
        

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
