import numpy as np
import matplotlib.pyplot as plt
import math


  
    
    


class KMeans:
    def __init__(self, X, nombre_classe):
        self.K = nombre_classe
        self.max_iterations = 100
        self.individu = X.shape[0]
        self.variable = X.shape[1]
            
    def moyenne(self,Y):
        somme = 0
        effectif = len(Y)
        for i in range(effectif):
            somme = somme + Y[i]
        moyenne = somme / effectif
        return moyenne 
    
    def moyenne_ligne(self,X):
        resu = []
        for i in range(len(X)):
            resu.append(self.moyenne(X[i]))  
        return np.asarray(resu)
    
    def moyenne_colonne(self,X):
        Y = np.asarray(X)
        trans = np.transpose(Y)
        resu = self.moyenne_ligne(trans)
        return resu   
      
    def liste_distance(self, X, Y):
        # On calcule les distances du point à l'ensemble des centres de classe
        liste = []
        for i in range(self.K):
            liste.append(math.sqrt(sum([(x - y) ** 2 for x, y in zip(X, Y[i])])))
        return liste      

    def initialisation_centres(self, X):
        centres = np.zeros((self.K, self.variable))
        for k in range(self.K):
            centre = X[np.random.choice(range(self.individu))]
            centres[k] = centre
        return centres

    def creation_clusters(self, X, centres):
        # Création d'une liste contenant l'ensemble des points affectés à chaque cluster
        clusters = [[] for _ in range(self.K)]

        # On cherche le centre de classe le plus proche de notre point 
        for indice_point, point in enumerate(X):
            centre_voisin = np.argmin(
                self.liste_distance(point,centres)
            )
            clusters[centre_voisin].append(indice_point)
        return clusters

    def nouveau_centres(self, clusters, X):
        # On définit les nouveaux centres comme moyenne des points appartenant à la classe
        centres = np.zeros((self.K, self.variable))
        for indice, cluster in enumerate(clusters):
            nouveau_centre = self.moyenne_colonne(X[cluster])
            centres[indice] = nouveau_centre
        return centres

    def prediction_classe(self, clusters, X):
        # On crée la liste des clusters en affectant à chaque individu sa classe
        classification = np.zeros(self.individu)
        for indice_classe, cluster in enumerate(clusters):
            for indice_individu in cluster:
                classification[indice_individu] = indice_classe
        return classification


    def clustering(self, X):
        # On itère le procédé pour un nombre d'itération fixé
        centres = self.initialisation_centres(X)
        for iteration in range(self.max_iterations):
            clusters = self.creation_clusters(X, centres)
            ancien_centroids = centres
            centres = self.nouveau_centres(clusters, X)
        classification = self.prediction_classe(clusters, X)
        return classification

