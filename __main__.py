# -*- coding: utf-8 -*-
import donnees as dn

test = dn.Donnees('C:/Users/georg/OneDrive/Documents/Projet données/code/donnees-hospitalieres-etablissements-covid19-2021-03-03-17h03.csv')
test3 = dn.Donnees('C:/Users/georg/OneDrive/Documents/Projet données/code/covid-hospit-incid-reg-2021-03-03-17h20.csv')


x=test.fenetrage('2020-04-16','2020-06-08')
data=test.donnees
data3=test3.donnees
x=test.jointure(test3)
x
x[0]
data[0]
data[1]

data3[0]
data3[1]




import donnees as dn
small = dn.Donnees('C:/Users/georg/OneDrive/Documents/Projet données/code/Book1.csv')
small2= dn.Donnees('C:/Users/georg/OneDrive/Documents/Projet données/code/Book2.csv')

x=small.jointure(small2)
x
small.donnees[0]
small2.donnees[0]
