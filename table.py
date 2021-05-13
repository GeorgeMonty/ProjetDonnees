
from tabulate import tabulate
from statistique import Statistique
import numpy as np

class Table :
    """Permet de créer des tableaux
    
    Attributes
    ----------
    liste_stat : une liste contenant des listes de statistiques
        les listes de statistiques viennent de la classe Statistique
    
    Example
    -------
    >>> liste_stat=[["Auvergne-Rhône-Alpes", "Bourgogne-Franche-Comté", "Bretagne", "Centre-Val de Loire", "Corse", "Grand-Est", "Guadeloupe", "Guyane", "Hauts-de-France", "Ile-de-France", "La Réunion", "Martinique", "Mayotte", "Normandie", "Nouvelle-Aquitaine", "Occitanie", "Pays de la Loire", "Provence-Alpes-Côte d'Azur"],[12,10,13.2,12.8,9,7,6.7,5.9,13,12,12,10.3,10.4,9.3,14,16,10.6,12.5]]
    >>> table1 = Table(liste_stat)
    >>> table1.creer_table()
    >>> table1.afficher_table()
    >>> table1.exporter_csv("C:/Users/.../table1.csv")    
    
    """
    def __init__(self,liste_stat):
        """
        <Constructeur>
        Création d'un objet de classe Table

        Parameters
        ----------
        liste_stat : list
            une liste composée de listes de statistiques.

        Returns
        -------
        None.

        """
        self.liste_stat=liste_stat
        
    def creer_table(self):
        """
        Méthode qui crée une table mais ne la retourne pas.
        
        Elle crée à la fois une nouvelle liste composée de listes qui permettra d'exporter la table en csv
        et une table au format tabulate que l'on pourra afficher après. 

        Returns
        -------
        None.

        """
        self.nb_colonnes = len(self.liste_stat)
        self.nb_lignes=len(self.liste_stat[0])
        self.interieur_table=[]
        for j in range(self.nb_lignes):
            listetable = [self.liste_stat[i][j] for i in range(self.nb_colonnes)]
            self.interieur_table.append(listetable)
        self.tableàretourner = tabulate(self.interieur_table,tablefmt='fancy_grid')
        
    def afficher_table(self):
        """
        La méthode qui permet d'afficher la table créée précedemment

        Returns
        -------
        None.

        """
        print(self.tableàretourner)
    
    def exporter_csv(self, chemintable):
        """
        La méthode qui permet d'exporter au format csv la table que l'on a créé.

        Parameters
        ----------
        chemintable : path
            le chemin qui mène au répertoire dans lequel vous voulez enregistrer la table ainsi que le nom que vous voulez donner à la table.

        Returns
        -------
        None.

        """
        np.savetxt(chemintable, self.interieur_table, delimiter=",", fmt="% s")




