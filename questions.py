# -*- coding: utf-8 -*-
"""
Created on Fri May  7 13:37:20 2021

@author: georg
"""
import jeux_donnees as jd
import numpy as np
import donnees as dn
import kmeans as km
import statistique as st
import graphique as gr




data1= jd.Jeux_donnees('C:/Users/georg/OneDrive/Documents/Projet données/code/data1.csv').importer()
data2= jd.Jeux_donnees('C:/Users/georg/OneDrive/Documents/Projet données/code/data2.csv').importer()
data3= jd.Jeux_donnees('C:/Users/georg/OneDrive/Documents/Projet données/code/data3.csv').importer()
data4= jd.Jeux_donnees('C:/Users/georg/OneDrive/Documents/Projet données/code/data4.csv').importer()
data5= jd.Jeux_donnees('C:/Users/georg/OneDrive/Documents/Projet données/code/data5.csv').importer()
holidays = jd.Jeux_donnees('C:/Users/georg/OneDrive/Documents/Projet données/code/test2.json').importer()

data1.variables
data2.variables
data3.variables
data4.variables
data5.variables


#1 Quel est le nombre total d’hospitalisations dues au Covid-19?
data_hosp = data5.selection_variables('incid_hosp')

somme = 0
for elem in data_hosp.donnees[1:]:
    somme = somme + elem[0]
print("Nb total d'hospitalisations: " + str(somme))

#2 Combien de nouvelles hospitalisations ont eu lieu ces 7 derniers jours dans chaque département ?
data_hosp_7_jour = data5.fenetrage("2021-02-27","2021-03-03")
deps = ["01","02","03","04","05","06","07","08","09"]
for i in range(10,102):
    deps.append(str(i))
deps.append("2A")
deps.append("2B")
resultat = {}
for dep in deps:
    somme = 0
    data_dep = data_hosp_7_jour.aggregation_spatial("dep", [str(dep)])
    data_dep = data_dep.selection_variables('incid_hosp')
    for elem in data_dep.donnees[1:]:
        somme = somme + elem[0]
    resultat[dep] = somme
resultat   
    
#3 Comment évolue la moyenne des nouvelles hospitalisations journalières de cette semaine par rapport à celle de la semaine dernière ? 
stat= st.Statistique()

data_hosp=data5.fenetrage_numpy("incid_hosp","dep","2020-03-29", "2020-04-04")


x=stat.moyenne_colonne(data_hosp)


data_hosp2=data5.fenetrage_numpy("incid_hosp","dep","2020-04-05", "2020-04-11")


x2=stat.moyenne_colonne(data_hosp2)

x
x2

print(" les moyenne a changer de " + str(x) + " à " + str(x2))

#Quel est le résultat de k-means avec k = 3 sur les données des départements du mois de Janvier 2021, lissées avec une moyenne glissante de 7 jours?
stat = st.Statistique()
k=3

janv = data4.fenetrage_numpy('nb', 'dep',date_debut="2021-01-01",date_fin="2021-01-31")

gliss = stat.moyenne_glissante_tableau(janv, 7)

kmeans = km.KMeans(np.asarray(gliss), k)

classification = kmeans.clustering(np.asarray(gliss))


#Combien de nouvelles admissions en réanimation ont eu lieu pendant la semaine suivant les vacances de la Toussaint de 2020?
rean_touss = data5.fenetrage("2020-11-08","2020-11-15")
rean_touss = rean_touss.selection_variables("incid_rea")

somme = 0
for elem in rean_touss.donnees[1:]:
    somme = somme + elem[0]
print("Il y avait {} nouvelles admissions en réanimation ont eu lieu pendant la semaine suivant les vacances de la Toussaint de 2020".format(somme))





