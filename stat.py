import numpy as np
import jeux_donnees as jd

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

test = [[0], [1], [0], [3], [1], [3], [0], [0], [0]]

stat=Statistique('sup')

x=stat.moyenne_colonne(test)

data1= jd.Jeux_donnees('C:/Users/georg/OneDrive/Documents/Projet données/code/data1.csv').importer()
data2= jd.Jeux_donnees('C:/Users/georg/OneDrive/Documents/Projet données/code/data2.csv').importer()
data3= jd.Jeux_donnees('C:/Users/georg/OneDrive/Documents/Projet données/code/data3.csv').importer()
data4= jd.Jeux_donnees('C:/Users/georg/OneDrive/Documents/Projet données/code/data4.csv').importer()
data5= jd.Jeux_donnees('C:/Users/georg/OneDrive/Documents/Projet données/code/data5.csv').importer()
holidays = jd.Jeux_donnees('C:/Users/georg/OneDrive/Documents/Projet données/code/test2.json').importer()

test=data5.fenetrage("2020-03-29", "2020-04-04")

test_hosp = test.selection_variables(["incid_hosp"])

x=stat.moyenne_colonne(test_hosp.donnees[1:])


test2=data5.fenetrage("2020-04-05", "2020-04-12")

test_hosp2 = test2.selection_variables(["incid_hosp"])

x2=stat.moyenne_colonne(test_hosp2.donnees[1:])



test.donnees[1:10]
stat=Statistique()

janv = data4.fenetrage_numpy('nb', 'dep',date_debut="2021-01-01",date_fin="2021-01-31")

gliss = stat.moyenne_glissante_tableau(janv, 7)

