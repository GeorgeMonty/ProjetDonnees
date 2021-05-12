# -*- coding: utf-8 -*-
"""
Created on Fri May  7 13:37:20 2021

@author: georg
"""
import jeux_donnees as jd
import numpy as np
import kmeans as km
import statistique as st
import graphique as gr
import matplotlib.pyplot as plt




data1= jd.Jeux_donnees('C:/Users/georg/OneDrive/Documents/GitHub/ProjetDonnees/Bases_de_donnees/covid-hospit-incid-reg-2021-03-03-17h20.csv').importer()
data2= jd.Jeux_donnees('C:/Users/georg/OneDrive/Documents/GitHub/ProjetDonnees/Bases_de_donnees/donnees-hospitalieres-classe-age-covid19-2021-03-03-17h03.csv').importer()
data3= jd.Jeux_donnees('C:/Users/georg/OneDrive/Documents/GitHub/ProjetDonnees/Bases_de_donnees/donnees-hospitalieres-covid19-2021-03-03-17h03.csv').importer()
data4= jd.Jeux_donnees('C:/Users/georg/OneDrive/Documents/GitHub/ProjetDonnees/Bases_de_donnees/donnees-hospitalieres-etablissements-covid19-2021-03-03-17h03.csv').importer()
data5= jd.Jeux_donnees('C:/Users/georg/OneDrive/Documents/GitHub/ProjetDonnees/Bases_de_donnees/donnees-hospitalieres-nouveaux-covid19-2021-03-03-17h03.csv').importer()
holidays = jd.Jeux_donnees('C:/Users/georg/OneDrive/Documents/GitHub/ProjetDonnees/Bases_de_donnees/VacancesScolaires.json').importer()

data1.variables
data2.variables
data3.variables
data4.variables
data5.variables


#1 Quel est le nombre total d’hospitalisations dues au Covid-19?
data_hosp = data5.selection_variables('incid_hosp')

somme1 = 0
for elem in data_hosp.donnees[1:]:
    somme1 = somme1 + elem[0]
print("Nb total d'hospitalisations: " + str(somme1))

#2 Combien de nouvelles hospitalisations ont eu lieu ces 7 derniers jours dans chaque département ?
data_hosp_7_jour = data5.fenetrage("2021-02-27","2021-03-03")
deps = ["01","02","03","04","05","06","07","08","09"]
for i in range(10,96):
    deps.append(str(i))
deps.append("971")
deps.append("972")
deps.append("973")
deps.append("974")
deps.append("976")
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

data_hosp=data5.fenetrage_numpy("incid_hosp","dep","2020-03-30", "2020-04-05")


x=stat.moyenne_colonne(data_hosp)

data_hosp2=data5.fenetrage_numpy("incid_hosp","dep","2020-04-06", "2020-04-12")
x2=stat.moyenne_colonne(data_hosp2)



print("les premiers moyennes :" + str(x))
print("les deuxième moyennes :" + str(x2))

graphique1 = gr.Graphique(['Lundi','Mardi','Mercredi','Jeudi','Vendredi','Samedi','Dimanche'], x, "Jour de la semaine", "Moyenne des nouvelles hospitalisations", 
                          "L'évolution de la moyenne des nouvelles hospitalisations journalières entre deux semaines", "Première Semaine")

graphique2 = gr.Graphique(['Lundi','Mardi','Mercredi','Jeudi','Vendredi','Samedi','Dimanche'], x2, "Jour de la semaine","Moyenne des nouvelles hospitalisations", 
                          "L'évolution de la moyenne des nouvelles hospitalisations journalières entre deux semaines", "Deuxième Semaine" )
graphique1.affichage_graphique()
graphique2.affichage_graphique()
plt.show()

#Quel est le résultat de k-means avec k = 3 sur les données des départements du mois de Janvier 2021, lissées avec une moyenne glissante de 7 jours?
stat = st.Statistique()
k=3

janv = data4.fenetrage_numpy('nb', 'dep',date_debut="2021-01-01",date_fin="2021-01-31")

gliss = stat.moyenne_glissante_tableau(janv, 7)

kmeans = km.KMeans(np.asarray(gliss), k)

classification = kmeans.clustering(np.asarray(gliss))
classification

#Combien de nouvelles admissions en réanimation ont eu lieu pendant la semaine suivant les vacances de la Toussaint de 2020?
rean_touss = data5.fenetrage("2020-11-08","2020-11-15")
rean_touss = rean_touss.selection_variables("incid_rea")

somme2 = 0
for elem in rean_touss.donnees[1:]:
    somme2 = somme2 + elem[0]
print("{} nouvelles admissions en réanimation ont eu lieu pendant la semaine suivant les vacances de la Toussaint de 2020".format(somme2))

#Combien des hommes et des femmes totals sont mort dues au Covid-19 dès que le 29 août 2020 ?
data29aout = data3.fenetrage("2020-08-29","2020-08-29")

datahomme = data29aout.choisir_sexe('homme')
datafemme = data29aout.choisir_sexe('femme')


data_decH = datahomme.selection_variables('dc')
data_decF = datafemme.selection_variables('dc')

sommeh = 0
sommef = 0
for i in range(len(data_decH.donnees[1:])):
    sommeh = sommeh + data_decH.donnees[1:][i][0]
    sommef = sommef + data_decF.donnees[1:][i][0]
print("nb d'hommes décédés: " + str(sommeh) + " ; nb de femmes décédés: " + str(sommef))


#Afficher un graphique du nombre moyen par région de nouvelles admissions en réanimation pendant le mois de Janvier 2021.
stat=st.Statistique()
x=data1.fenetrage_numpy('incid_rea','numReg',date_debut="2021-01-01",date_fin="2021-01-31")
gliss2 = np.asarray(stat.moyenne_glissante_tableau(x, 7))
x=stat.moyenne_colonne(x)
graph = gr.Graphique(range(1,32),x, "jour", "incid_rea", "Nombre moyen par région de nouvelles admissions en réanimation")
graph.affichage_graphique()
plt.show()
moyennes_gliss = stat.moyenne_colonne(gliss2)
graph2 = gr.Graphique(range(1,26),moyennes_gliss, "index", "incid_rea moyenne glissante", "")
graph2.affichage_graphique()
plt.show()









