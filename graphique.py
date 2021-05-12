import numpy as np
import matplotlib.pyplot as plt
import math

class Graphique:
    """
    Une classe qui permet la réalisation de graphiques
    
       
    Attributs
    ---------
    abscisse : array numpy 
        constitué des abscisses du graphe
    
    ordonnee : array numpy 
        constitué des ordonnées du graphe
    
    nom_absicce : str
        Nom de l'axe des abscisses      
    
    nom_ordonnee : str
        Nom de l'axe des ordonnées
        
    titre : str
        Titre du graphique         
                    
    """   
    def __init__(self, abscisse, ordonnee, nom_abscisse, nom_ordonnee, titre):
        """<Constructeur>
        Création d'un objet de classe graphique
        
        """
        self.abscisse = abscisse
        self.ordonnee = ordonnee
        self.nom_abscisse = nom_abscisse
        self.nom_ordonnee = nom_ordonnee
        self.titre = titre
        
    def affichage_graphique(self):
        """
        Méthode permettant d'afficher un graphique
        
        Parametres
        ----------
        None
        
        Returns
        -------
        Graphique de la série temporelle désirée
        """ 
        plt.plot(self.abscisse, self.ordonnee, 'r')
        plt.title(self.titre)
        plt.xlabel(self.nom_abscisse)
        plt.ylabel(self.nom_ordonnee)
    
