import jeux_donnees as jd

class Donnees(jd.Jeux_donnees):
    
    def __init__(self, lien_fichier):
        jd.Jeux_donnees.__init__(self,lien_fichier)
        self.donnees = self.importer()
        
    def jointure(self,donnee2,variable_jointure):
    
        if self.__type_fichier == 'csv':
            data1 = self.donnees
            data2 = donnee2.donnees
            variables1 = data1[0]
            variables2 = data2[0]
            new_variables = variables1
            
            #creer une liste des nouvelles variables du jeu de données
            for i in variables2:
                is_new = True
                for j in new_variables:
                    if i == j:
                        is_new = False
                if is_new:
                    new_variables.append(i)
            ######################################################################################################
            colnum1 = None
            for col in range(len(variables1)):
                if variables1[col] == variable_jointure:
                    colnum1 = col
                    break
            if colnum1 == None:
                raise Exception("Le variable de jointure n'est pas présent dans un/tout les jeux de données")
                  
            
        elif self.__type_fichier == 'json':
            return ("json files not coded yet")
        
        else:
            raise Exception("Type de fichier inconnu")
        

