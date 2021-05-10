import unittest
import jeux_donnees as jd
import donnees as dn

class JeuxTest(unittest.TestCase):

    def test_importe_classe(self):
        test1 = jd.Jeux_donnees('C:/Users/georg/OneDrive/Documents/GitHub/ProjetDonnees/Bases_de_donnees/VacancesScolaires.json')
        test2 = jd.Jeux_donnees('C:/Users/georg/OneDrive/Documents/GitHub/ProjetDonnees/Bases_de_donnees/donnees-hospitalieres-classe-age-covid19-2021-03-03-17h03.csv')
        self.assertIsInstance(test1.importer(),dn.Donnees)
        self.assertIsInstance(test2.importer(),dn.Donnees)
        
    def test_import_type_fichier(self):
        test1 = jd.Jeux_donnees('C:/Users/georg/OneDrive/Documents/GitHub/ProjetDonnees/Bases_de_donnees/VacancesScolaires.json')
        test2 = jd.Jeux_donnees('C:/Users/georg/OneDrive/Documents/GitHub/ProjetDonnees/Bases_de_donnees/donnees-hospitalieres-classe-age-covid19-2021-03-03-17h03.csv')
        self.assertTrue(test1.importer().type_fichier == "json")
        self.assertTrue(test2.importer().type_fichier == "csv")
        
    def test_lien_fichier(self):
        test1 = jd.Jeux_donnees('C:/Users/georg/OneDrive/Documents/GitHub/ProjetDonnees/Bases_de_donnees/VacancesScolaires.json')
        self.assertTrue(test1.lien_fichier == "C:/Users/georg/OneDrive/Documents/GitHub/ProjetDonnees/Bases_de_donnees/VacancesScolaires.json" )
     
    
unittest.main()