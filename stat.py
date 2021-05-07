import numpy as np

class Statistique:
    
    def moyenne(self, X):
        somme = 0
        effectif = len(X)
        for i in range(effectif):
            somme = somme + X[i]
        moyenne = somme / effectif
        return moyenne 
    
    def variance(self, X):
        somme = 0
        effectif = len(X)
        for i in range(effectif):
            somme = somme + (X[i] - moyenne(X))**2
        variance = somme / effectif
        return variance
    
    def ecart_type(self, X):
        return (variance(X)**1/2)  
        
    def centrage(self, X):
        moyen = moyenne(self, X)
        liste_centree = X
        for i in range(len(X)):
            liste_centree[i] = X[i] - moyen
        return liste_centree   
        
    def normalisation(self, X):
        ecart = ecart_type(X)
        centree = centrage(X)
        centree_reduite = X
        for i in range(len(X)):
            centree_reduite[i] = centree[i] / ecart
        return centree_reduite  
        
    def moyenne_mobile(self, X, fenetre):
        sortie = [sum(X[0:fenetre]) / fenetre, ]
        for i in range(fenetre, len(X)):
            sortie.append(sortie[-1] - X[i - fenetre] / fenetre + X[i] / fenetre)
        return sortie    
        
    def moyenne_ligne(self, X):
        resu = []
        for i in range(len(X)):
            resu.append(self.moyenne(X[i]))  
        return np.asarray(resu)
    
    def moyenne_colonne(self, X):
        table = np.asarray(X)
        trans = np.transpose(table)
        resu = self.moyenne_ligne(trans)
        return resu
            
    def centrage_tableau(self, X):
        centree = []
        table = np.asarray(X)
        new_X = np.transpose(table)
        for x in new_X:
            centree.append(self.centrage(x))      
        centre = np.asarray(centree)
        return np.transpose(centre)
    
    def normalisation_tableau(self, X):
        trans = np.transpose(np.array(X,dtype=float))
        normal = []
        for x in trans:
            normal.append(self.normalisation(x))
        resu = np.asarray(normal)
        return np.transpose(resu)  

    def moyenne_glissante_tableau(self, X,fenetre):
        table_moyenne = []
        for x in X:
            table_moyenne.append(self.moyenne_mobile(x,fenetre))
        return table_moyenne                

test = Statistique() 

y = [[1, 2, 3, 6, 98, 65, 32], [2, 4, 6, 5, 9, 23, 200], [10, 5, 9, 90, 76, 34, 2000]]  
   