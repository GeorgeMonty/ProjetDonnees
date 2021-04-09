import csv
import json

class Jeux_donnees:
    def __init__(self,lien_fichier):
        self.lien_fichier = lien_fichier
    
    def importer(self):
        type_fichier= self.lien_fichier.split('.')[-1]
        path = self.lien_fichier.split('\\')
        filename = path[-1]
        folder=''
        for i in range(len(path)-1):
            folder = folder + path[i] + '\\'
            
        if type_fichier == 'csv':
            data = []
            
            with open(folder + filename, encoding='ISO-8859-1') as csvfile :
                covidreader = csv.reader(csvfile, delimiter=';')
                for row in covidreader :
                    data.append(row)
            return data
        
        elif type_fichier == 'json':
            with open(folder + filename) as json_file :
                data = json.load(json_file)
            return data
        
        else:
            raise Exception("Type de fichier inconnu")
        
        def jointure(self,jeux2,variable_jointure):
            pass
        
