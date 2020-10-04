import DBinterface as DB
import random 
import datetime as dt
import re

def print_ranking(my_ranking,ranking_size,top_or_bottom):
    Tweet=""
    if top_or_bottom == True:
        Tweet += ("The first " + ranking_size + " cities with more CO2 emissions due to traffic are: \r\n ")     
    else: 
        Tweet += ("The first " + ranking_size + " cities with less CO2 emissions due to traffic are: \r\n")  

    for i in range(ranking_size):
        Tweet += (str((i+1)) + "º " + str(my_ranking[i][0]) + " with a CO2 value of " + str(my_ranking[i][1]) + "\r\n")
    return(Tweet)

def rank(api):

    interface = DB.nasaDBinterface()
    ranking_size = random.randint(3,5)
    top_or_bottom =  random.choice([True, False]) 
    my_ranking = interface.get_ranking(ranking_size, top_or_bottom)
    Tweet=print_ranking(my_ranking,ranking_size,top_or_bottom)

    api.update_status(status=Tweet)


def leer_hashtag(T):

    L=list(T)
    L.append(" ")
    for a in range(len(L)):
        if L[a]=="#":
            a=a+1
            ht=[]
            while L[a]!=" ":
                ht.append(L[a])
                a=a+1
    ht_salida= ""
    for e in ht:
        ht_salida += e
    return ht_salida

def get_city(TEXT):
    #m = re.search('city: (.+?)#consult', text)
    #print(m)


    L=TEXT.lower().split()
    print(L)
    
    city = []
    # for a in range(len(L)):
    #     if L[a]=="#consult":
    #         break
    #     if L[a]=="city:":
    #         for i in range(len(L)-a-2):
    #             c += L[a+i+1] + " "
    index1 = None
    index2 = None
    for a in range(len(L)):
        if L[a]=="#consult":
            index2=a
        if L[a]=="city:":
            index1=a

    if index1 != None and index2 != None:
        city = L[index1+1:index2]
        print(city)
        city = str(' '.join(city))

    # for a in L:
    #     if a=="#consult":
    #         break
    #     if a=="city:":
    #         for i in range(len(L)-a-2):
    #             c += L[a+i+1] + " "
    # x=c.split()
    # for i in range(len(x)-1):
    #     ciudad += x[i]+" "
    # if len(x) != 1:
    #     ciudad += x[len(x)-1]
    print('ciudad leida: ' + str(city))
    return city