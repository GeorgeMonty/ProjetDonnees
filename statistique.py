import numpy as np
import jeux_donnees as jd

class Statistique:
    """
    Une classe qui permet la réalisation de calculs statistiques variées
    
       
    Attributs
    ---------
    None      
                    
    """ 

    def moyenne(self, X):
        """
        Méthode permettant de calculer la moyenne d'une liste Python
        
        Parametres
        ----------
        X: list
        
        Returns
        -------
        Moyenne: integer
            La moyenne de la liste
        """  
        somme = 0
        effectif = len(X)
        for i in range(effectif):
            somme = somme + X[i]
        moyenne = somme / effectif
        return moyenne 
    
    def variance(self, X):
        """
        Méthode permettant de calculer la variance d'une liste Python
        
        Parametres
        ----------
        X: list
        
        Returns
        -------
        Variance: integer
            La variance de la liste
        """ 
        somme = 0
        effectif = len(X)
        for i in range(effectif):
            somme = somme + (X[i] - self.moyenne(X))**2
        variance = somme / effectif
        return variance
    
    def ecart_type(self, X):
        """
        Méthode permettant de calculer l'écart-type d'une liste Python
        
        Parametres
        ----------
        X: list
        
        Returns
        -------
        Ecart-type: integer
            L'écart-type de la liste
        """ 
        return (self.variance(X)**1/2)  
        
    def centrage(self, X):
        """
        Méthode permettant de centrer une liste
        
        Parametres
        ----------
        X: list
        
        Returns
        -------
        liste_centree: liste
            La liste centrée obtenue à partir d'une liste quelconque
        """ 
        moyen = self.moyenne(X)
        liste_centree = X
        for i in range(len(X)):
            liste_centree[i] = X[i] - moyen
        return liste_centree   
        
    def normalisation(self, X):
        """
        Méthode permettant de normaliser une liste
        
        Parametres
        ----------
        X: list
        
        Returns
        -------
        centree_reduite: liste
            La liste normalisée obtenue à partir d'une liste quelconque
        """ 
        ecart = self.ecart_type(X)
        centree = self.centrage(X)
        centree_reduite = X
        for i in range(len(X)):
            centree_reduite[i] = centree[i] / ecart
        return centree_reduite  
        
    def moyenne_mobile(self, X, fenetre):
        """
        Méthode permettant de calculer la moyenne mobile d'une liste Python
        
        Parametres
        ----------
        X: list
        fenetre: int (fenetrage de la moyenne glissante)
        
        Returns
        -------
        Moyenne_mobile: list
            La moyenne mobile d'une liste
        """ 
        sortie = [sum(X[0:fenetre]) / fenetre, ]
        for i in range(fenetre, len(X)):
            sortie.append(sortie[-1] - X[i - fenetre] / fenetre + X[i] / fenetre)
        return sortie    
        
    def moyenne_ligne(self, X):
        """
        Méthode permettant de calculer la moyenne suivant les lignes d'une liste de liste
        
        Parametres
        ----------
        X: liste de liste (équivalent d'une matrice)
        
        Returns
        -------
        Moyenne: array numpy
            La liste des moyennes suivant les lignes
        """  
        resu = []
        for i in range(len(X)):
            resu.append(self.moyenne(X[i]))  
        return np.asarray(resu)
    
    def moyenne_colonne(self, X):
        """
        Méthode permettant de calculer la moyenne suivant les colonnes d'une liste de liste
        
        Parametres
        ----------
        X: liste de liste (équivalent d'une matrice)
        
        Returns
        -------
        Moyenne: array numpy
            La liste des moyennes suivant les colonnes
        """ 
        table = np.asarray(X)
        trans = np.transpose(table)
        resu = self.moyenne_ligne(trans)
        return resu
            
    def centrage_tableau(self, X):       
        """
        Méthode permettant de centrer un tableau (matrice)
        
        Parametres
        ----------
        X: list
        
        Returns
        -------
        table_centree: liste
            La table centrée obtenue à partir d'une table quelconque
        """  
        centree = []
        table = np.asarray(X)
        new_X = np.transpose(table)
        for x in new_X:
            centree.append(self.centrage(x))      
        centre = np.asarray(centree)
        return np.transpose(centre)
    
    def normalisation_tableau(self, X):
        """
        Méthode permettant de normaliser un tableau (matrice)
        
        Parametres
        ----------
        X: list
        
        Returns
        -------
        table_centree_reduite: liste
            La table normalisée obtenue à partir d'une table quelconque
        """  
        trans = np.transpose(np.array(X,dtype=float))
        normal = []
        for x in trans:
            normal.append(self.normalisation(x))
        resu = np.asarray(normal)
        return np.transpose(resu)  

    def moyenne_glissante_tableau(self, X,fenetre):
        """
        Méthode permettant de calculer la moyenne mobile d'une matrice
        
        Parametres
        ----------
        X: list
        fenetre: int (fenetrage de la moyenne glissante)
        
        Returns
        -------
        Moyenne_mobile: list
            La moyenne mobile d'une matrice
        """  
        table_moyenne = []
        for x in X:
            table_moyenne.append(self.moyenne_mobile(x,fenetre))
        return table_moyenne                


