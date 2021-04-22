
class Donnees:
    
    def __init__(self, donnees,type_fichier):
        """<Constructeur>
        
        Parametres
        ----------
        donnees
            Les donnees du jeu de données.
        type_fichier : str
            Le format du fichier d'origin du jeux de donnees.


        """
        self.donnees = donnees
        self.__type_fichier = type_fichier
    
    def testjointure(self,donnee2):
    
        if self.__type_fichier == 'csv':
            if donnee2.__type_fichier == 'csv':
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
                        checking = True
                        for var_par in variables_partages:
                            for j in range(len(variables2)):
                                if var_par == variables2[j]:
                                    for k in range(len(new_variables)):
                                        if new_variables[k] == var_par:
                                            if entry2[j] != new_entry2[k]:
                                                checking = False
                        if checking == True:    
                            for l in range(len(new_variables)):
                                for m in range(len(variables2)):
                                    if new_variables[l] == variables2[m]:
                                        new_entry2.insert(l,entry2[m])
                                        new_entry2.pop(l+1)
                            is_repeat = False
                            for repeat in new_data:
                                if new_entry2 == repeat:
                                    is_repeat = True
                            if is_repeat == False:
                                new_data.append(new_entry2)
                                step = step + 1
                                if step % 25 == 0:
                                    print('step :' + str(step))
                                ####if step >= 200:
                                    ####return Donnees(new_data,'csv')
                print('All rows done')             
                return Donnees(new_data,'csv')       
            else:
                raise Exception("On ne peut que faire les jointures sur les fichiers. csv")                
        else:
            raise Exception("On ne peut que faire les jointures sur les fichiers. csv")
    
    
    def jointure(self,donnee2):
        if self.__type_fichier == 'csv':
            if donnee2.__type_fichier == 'csv':
                step=0
                data1 = self.donnees
                data2 = donnee2.donnees
                variables1 = data1[0]
                variables2 = data2[0]
                variables_partages = []
                for i in variables1:
                    est_partage = False
                    for j in variables2:
                        if i == j:
                            est_partage = True
                    if est_partage == True:
                        variables_partages.append(i)
                tuple_variables = ('jour','dep','numReg','nomReg','sexe','cl_age90','hosp','rea','rad','dc','nb','incid_hosp','incid_rea','incid_rad','incid_dc')
                new_variables = list(tuple_variables)
                new_data = [new_variables]
                print(variables_partages)
                for entry1 in data1[1:]:
                    step=step+1
                    new_entry=[]
                    for variable in new_variables:
                        new_entry.append(None)
                    for j in range(len(new_variables)):
                        for i in range(len(variables1)):
                            if variables1[i] == new_variables[j]:
                                new_entry[j]=entry1[i]
                    new_data.append(new_entry) 
                    print('data1 step:' + str(step))
                step = 0 
                final_data = [new_variables]
                for join_entry in new_data[1:]:
                    step = step + 1
                    for entry2 in data2[1:]:
                        final_entry = tuple(join_entry)
                        final_entry = list(final_entry)
                        join = True
                        for var_par in variables_partages:
                            for j in range(len(variables2)):
                                if variables2[j] == var_par:
                                    for k in range(len(new_variables)):
                                        if new_variables[k] == var_par:
                                            if entry2[j] != join_entry[k]:
                                                join = False
                        if join == True:
                            for l in range(len(new_variables)):
                                for m in range(len(variables2)):
                                    if variables2[m] == new_variables[l]:
                                        final_entry[l]=entry2[m]            
                            final_data.append(final_entry)                
                    print('data2 step:' + str(step))
                                    
                new_donnees = Donnees(final_data,'csv')
                print("Finished")
                return new_donnees                          
            else:
                raise Exception("On ne peut que faire les jointures sur les fichiers. csv")
        else:
            raise Exception("On ne peut que faire les jointures sur les fichiers. csv")
    
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
    
    def selection_variables(self,variables):
        colnums=[]
        all_variables = self.donnees[0]
        
        for i in range(len(all_variables)):
            if all_variables[i] not in variables:
                colnums.append(i)
                
        for entry in self.donnees:
            for ele in sorted(colnums, reverse = True): 
                del entry[ele]

    def aggregation_spatial(self,depreg,liste_nums):
        if depreg not in ['reg','dep']:
            raise Exception('On ne peut que faire l\'aggregation spatial sur les variables \'reg\' ou \'dep\'')
        else:
            if depreg == 'reg':
                depreg = 'numReg'
            colnum = None
            for var in range(len(self.donnees[0])):
                if self.donnees[0][var] == depreg:
                    colnum = var
                    
            for entry in self.donnees[1:]:
                if entry[colnum] not in liste_nums:
                    self.donnees.remove(entry)
                    
                    
    def pendant_vacance(self,vacance,donnees_vacances):
        
        data_vacances = donnees_vacances.donnees
        data = self.donnees
        variables = self.donnees[0]
        col_jour = None
        col_dep = None
        null_entry = False
        
        for i in range(len(variables)):
            if variables[i] == 'jour':
                col_jour = i
                print ('col_jour =' + str(col_jour))
            elif variables[i] == 'dep':
                col_dep = i
                print ('col_dep =' + str(col_dep))
        if col_jour == None:
            raise Exception('Variable \'jour\' non-trouvée')
        elif col_dep == None:
            raise Exception('Variable \'dep\' non-trouvée')
        for entry in data[1:]:
            remove = True
            date = entry[col_jour].split('-')
            for zones in data_vacances['Academie']:
                if entry[col_dep] == zones['Code_Dpt']:
                    zone = zones['Zone']
                    print(zone)
                    for vac in data_vacances['Calendrier']:
                        if vac['Zone'] == zone:
                            if vac['Description'] == vacance:
                                date_fin = vac['Fin']
                                if date_fin == None:
                                    date_fin = [date_fin]
                                else:
                                    date_fin = date_fin.split('-')
                                date_debut = vac['Debut'].split('-')
                                if date[0] in [date_debut[0],date_fin[0]]:
                                    if date_fin == [None]:
                                        null_entry = True
                                    else:
                                         if date_debut[0] == date_fin[0]: #les années sont les mêmes
                                             if date_debut[1] == date_fin[1]: #les mois sont le même
                                                 if int(date[2]) in range(int(date_debut[2]),int(date_fin[2])):
                                                     remove = False
                                             else: #mois differents
                                                 if int(date[1]) in range(int(date_debut[1])+1,int(date_fin[1])):
                                                     remove = False
                                                 elif int(date[1]) == int(date_debut[1]):
                                                     if int(date[2]) in range(int(date_debut[2]),32):
                                                         remove = False
                                                 elif int(date[1]) == int(date_fin[1]):
                                                     if int(date[2]) in range(0,int(date_debut[2])+1):
                                                         remove = False
                                         else: #années differents
                                             if int(date[0]) == int(date_debut[0]):
                                                 if int(date[1]) in range(int(date_debut[1])+1,13):
                                                     remove = False
                                                 elif int(date[1]) == int(date_debut[1]):
                                                     if int(date[2]) in range(int(date_debut[2]),32):
                                                         remove = False
                                             elif int(date[0]) == int(date_fin[0]):            
                                                 if int(date[1]) in range(0,int(date_fin[1])):
                                                     remove = False
                                                 elif int(date[1]) == int(date_fin[1]):
                                                     if int(date[2]) in range(0,int(date_debut[2])+1):
                                                         remove = False       
            if remove == True:
                data.remove(entry)                           
        if null_entry == True:
            print('Note: Au moins un entry a été enlevé parce que le date du fin de ce vacance n\'est pas connu')
        else:
            print('Finished without Nones')
                   
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               