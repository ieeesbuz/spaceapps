#!/usr/bin/python3
# -*- coding: utf-8 -*-
import schedule
import time
import autoreply as ar
import config
import followfollowers as ff
import functions as fc
import concienciar

class Count(object):

    def __init__(self):
        self._count = 1

    def increase(self):
        self._count += 1


def autoreply(api):
    ar.main(api)

def followforfollow(api):
    ff.main(api)

def ranking(api):
    fc.rank(api)

def mensajes(api, vector, count):
    concienciar.concienciar(api, vector, count)
    count.increase()
    if count._count==24:
        count.__init__()


f = open("mss.txt", 'r')
vector=[""]
i=0
for line in f:
    vector.append(line)
    i+=1
f.close()
vector.pop(0)
api=config.create_api()
count = Count()

schedule.every(20).seconds.do(autoreply, api)
schedule.every(30).seconds.do(followforfollow, api)
schedule.every().monday.at("22:24").do(ranking,api)
schedule.every().day.at("22:23").do(mensajes,api,vector, count)



while True:
    schedule.run_pending()
    time.sleep(1)


