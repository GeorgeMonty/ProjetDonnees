import numpy as np
import matplotlib.pyplot as plt
import math

class KMeans:
    
    """
    Une classe qui permet d'effectuer un clustering par méthode des K-means
    
       
    Attributs
    ---------
    X : array numpy 
        constitué des données préalablement traitées par la classe Donnee
                   
    
    nombre_classe : integer
                    Nombre de classes choisi pour le clustering
                    
    """    
    
    def __init__(self, X, nombre_classe):
        """<Constructeur>
        Création d'un objet Kmeans
        
        Parametres
        ----------
        X : array numpy 
        constitué des données préalablement traitées par la classe Donnee
                   
    
        nombre_classe : integer
                    Nombre de classes choisi pour le clustering
            
        """
        self.K = nombre_classe
        self.max_iterations = 1000
        self.individu = X.shape[0]
        self.variable = X.shape[1]
            
    def moyenne(self,Y):
                """
        Méthode permettant de calculer la moyenne d'une liste Python
        
        Parametres
        ----------
        Y: list
        
        Returns
        -------
        Moyenne: integer
            La moyenne de la liste
        """    
        somme = 0
        effectif = len(Y)
        for i in range(effectif):
            somme = somme + Y[i]
        moyenne = somme / effectif
        return moyenne 
    
    def moyenne_ligne(self,X):
                """
        Méthode permettant de calculer la moyenne suivant les lignes d'une liste de liste
        
        Parametres
        ----------
        Y: liste de liste (équivalent d'une matrice)
        
        Returns
        -------
        Moyenne: array numpy
            La liste des moyennes suivant les lignes
        """  
        resu = []
        for i in range(len(X)):
            resu.append(self.moyenne(X[i]))  
        return np.asarray(resu)
    
    def moyenne_colonne(self,X):
                """
        Méthode permettant de calculer la moyenne suivant les colonnes d'une liste de liste
        
        Parametres
        ----------
        Y: liste de liste (équivalent d'une matrice)
        
        Returns
        -------
        Moyenne: array numpy
            La liste des moyennes suivant les colonnes
        """  
        Y = np.asarray(X)
        trans = np.transpose(Y)
        resu = self.moyenne_ligne(trans)
        return resu   
      
    def liste_distance(self, X, Y):
                """
        Méthode permettant de calculer la liste des distances d'une liste (un individu du jeu de données) à un ensemble de points 
        
        Parametres
        ----------
        X: liste  (équivalent d'un point)
        Y: liste de liste (équivalent de plusieurs points)
        
        Returns
        -------
        Moyenne: list
            La liste des distances du point à l'ensemble des autres points
        """  
        # On calcule les distances du point à l'ensemble des centres de classe
        liste = []
        for i in range(self.K):
            liste.append(math.sqrt(sum([(x - y) ** 2 for x, y in zip(X, Y[i])])))
        return liste      

    def initialisation_centres(self, X):
                """
        Méthode permettant d'initialiser les centres aléatoirement 
        
        Parametres
        ----------
        X: array numpy  (matrice des données)
        
        
        Returns
        -------
        Centres: list
            La liste des centres
        """  
        centres = np.zeros((self.K, self.variable))
        for k in range(self.K):
            centre = X[np.random.choice(range(self.individu))]
            centres[k] = centre
        return centres

    def creation_clusters(self, X, centres):
                """
        Méthode permettant de créer les clusters
        
        Parametres
        ----------
        X: array numpy  (matrice des données)
        centres: liste des centres
        
        
        Returns
        -------
        Clusters: list
            Liste contenant K (nombres de classes) listes où chaque liste contient l'indice de chaque individu appartenant à la classe
        """ 
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
                """
        Méthode permettant de calculer les nouveaux centres
        
        Parametres
        ----------
        X: array numpy  (matrice des données)
        clusters: liste de listes des appartenances à la classe
        
        
        Returns
        -------
        Centres: list
            Liste contenant les nouveaux centres calculés comme moyenne des points de la classe
        """ 
        # On définit les nouveaux centres comme moyenne des points appartenant à la classe
        centres = np.zeros((self.K, self.variable))
        for indice, cluster in enumerate(clusters):
            nouveau_centre = self.moyenne_colonne(X[cluster])
            centres[indice] = nouveau_centre
        return centres

    def prediction_classe(self, clusters, X):
                """
        Méthode permettant d'affecter à chaque individu sa classe
        
        Parametres
        ----------
        X: array numpy  (matrice des données)
        clusters: liste de listes des appartenances à la classe
        
        
        Returns
        -------
        Classification: array numpy
            Array numpy contenant le numéro de classe de chaque individu
        """ 
        # On crée la liste des clusters en affectant à chaque individu sa classe
        classification = np.zeros(self.individu)
        for indice_classe, cluster in enumerate(clusters):
            for indice_individu in cluster:
                classification[indice_individu] = indice_classe
        return classification


    def clustering(self, X):
                """
        Méthode permettant de réaliser le K-means en itérant le processus
        
        Parametres
        ----------
        X: array numpy  (matrice des données)
        
        
        Returns
        -------
        Classification: array numpy
            Array numpy contenant le numéro de classe de chaque individu
        """ 
        # On itère le procédé pour un nombre d'itération fixé
        centres = self.initialisation_centres(X)
        for iteration in range(self.max_iterations):
            clusters = self.creation_clusters(X, centres)
            ancien_centroids = centres
            centres = self.nouveau_centres(clusters, X)
        classification = self.prediction_classe(clusters, X)
        return classification





