import jeux_donnees as jd

class Donnees(jd.Jeux_donnees):
    
    def __init__(self, lien_fichier):
        jd.Jeux_donnees.__init__(self,lien_fichier)
        self.__type_fichier = self.lien_fichier.split('.')[-1]
        self.donnees = self.importer()
        
    def jointure(self,donnee2):
    
        if self.__type_fichier == 'csv':
            data1 = self.donnees
            data2 = donnee2.donnees
            variables1 = data1[0]
            variables2 = data2[0]
            
            ######################################################################################################

            #creer une liste des variables partagées entre les jeux de données
            variables_partages = []
            for i in variables1:
                est_partage = False
                for j in variables2:
                    if i == j:
                        est_partage = True
                if est_partage == True:
                    variables_partages.append(i)
            if variables_partages == []:
                raise Exception('Aucun variables partagées entre ces jeux de données')
                
            variables_partages = tuple(variables_partages)
                        
            ######################################################################################################
       
            #creer une nouvelle liste des variables du jeu de données
            new_variables = list(variables_partages)
            for i in variables1:
                is_new = True
                for j in variables_partages:
                    if i == j:
                        is_new = False
                if is_new:
                    new_variables.append(i)
                    
            for i in variables2:
                is_new = True
                for j in variables_partages:
                    if i == j:
                        is_new = False
                if is_new:
                    new_variables.append(i)
                    
            ######################################################################################################
           
            new_data = [new_variables]
            step = 0
            for entry1 in data1[1:]:
                new_entry1 = []
                for new_var in new_variables:
                    check = False
                    for i in range(len(variables1)):
                        if new_var == variables1[i]:
                            new_entry1.append(entry1[i])
                            check = True
                    if check == False:
                        new_entry1.append(None)
                new_entry1 = tuple(new_entry1)
                for entry2 in data2[1:]:
                    new_entry2 = list(new_entry1)
                    
                    for var_par in variables_partages:
                        for j in range(len(variables2)):
                            if var_par == variables2[j]:
                                checking = True
                                for k in range(len(new_variables)):
                                    if new_variables[k] == var_par:
                                        if entry2[j] != new_entry2[k]:
                                            checking = False
                    if checking == True:    
                        for l in range(len(new_variables)):
                            for m in range(len(variables2)):
                                if new_variables[l] == variables2[m]:
                                    if new_entry2[l] == None:
                                        new_entry2.insert(l,entry2[m])
                                        new_entry2.pop(l+1)
                        is_repeat = False
                        for repeat in new_data:
                            if new_entry2 == repeat:
                                is_repeat = True
                        if is_repeat == False:
                            new_data.append(new_entry2)
                            print('step :' + str(step))            
                            step = step + 1
                            if step >= 20000:
                                return new_data
            print('done')             
            return new_data       
            
        elif self.__type_fichier == 'json':
            return ("json files not coded yet")
        
        else:
            raise Exception("Type de fichier inconnu")
        
        
    def fenetrage(self,date_debut='0000-00-00',date_fin='999999-999-999'):
        data = self.donnees
        date_debut = date_debut.split('-')
        date_fin = date_fin.split('-')
        variables = data[0]
        i=0
        for var in variables:
            if var == 'jour':
                col_jour = i
            i = i+1
            
        for entry in data[1:]:
            date = entry[col_jour].split('-')
            if int(date[0]) < int(date_debut[0]):
                data.remove(entry)
            elif int(date[0]) == int(date_debut[0]):
                if int(date[1]) < int(date_debut[1]):
                    data.remove(entry)
                elif int(date[1]) == int(date_debut[1]):
                    if int(date[2]) < int (date_debut[2]):
                        data.remove(entry)
            if int(date[0]) > int(date_fin[0]):
                data.remove(entry)
            elif int(date[0]) == int(date_fin[0]):
                if int(date[1]) > int(date_fin[1]):
                    data.remove(entry)
                elif int(date[1]) == int(date_fin[1]):
                    if int(date[2]) > int (date_fin[2]):
                        data.remove(entry)
            

