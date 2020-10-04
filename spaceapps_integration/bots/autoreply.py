#!/usr/bin/env python
# tweepy-bots/bots/autoreply.py
import os
import tweepy
import logging
import time
import functions as fc
import DBinterface as DB

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

FILE_NAME = '../last_seen.txt'

def read_last_seen(FILE_NAME):
    file_read= open(FILE_NAME, 'r')
    last_seen_id = int(file_read.read().strip())
    file_read.close()
    return last_seen_id

def store_last_seen(FILE_NAME, last_seen_id):
    file_write= open(FILE_NAME, 'w')
    file_write.write(str(last_seen_id))
    file_write.close()
    return

def check_mentions(api, keywords, since_id):
    interface = DB.nasaDBinterface()
    logger.info("Retrieving mentions")
    new_since_id = since_id
    for tweet in tweepy.Cursor(api.mentions_timeline,since_id=since_id).items():
        try:
            new_since_id = max(tweet.id, new_since_id)
            if tweet.in_reply_to_status_id is not None:
                continue
            if any(keyword in tweet.text.lower() for keyword in keywords):
                TEXT = tweet.text
                hashtag=""
                try:
                    hashtag=fc.leer_hashtag(TEXT)
                except Exception:
                    api.update_status(status="@" + tweet.user.screen_name + "Sorry, I didn't understand you. Check the instructions in the pinned tweet!" ,
                    in_reply_to_status_id=tweet.id)
                    # print("hashtag error")
                    hashtag=None

                logger.info(f"Answering to {tweet.user.name}")
                v=['ccc',1111,1112]

                if hashtag=="consult":
                    #v es un vector que guarda tanto las emision de CO2 como el puesto en el ranking
                    nombre_ciudad=fc.get_city(TEXT)
                    v=interface.get_consulta(nombre_ciudad)
                    print("resultado de consulta: " + str(v))
                    image_dir = "./"+str(interface.get_city_image(nombre_ciudad))
                    print(image_dir)
                    media = api.media_upload(image_dir)
                    api.update_status(status="@" + tweet.user.screen_name + "Your city is in the position " + str(v[0][1]) + 
                    " in the ranking. It emits " + str(v[0][2]) + "kg of CO2 per habitant.", in_reply_to_status_id=tweet.id, media_ids=[media.media_id] )
                    try:
                        os.rmdir(image_dir)
                    except OSError as e:
                        print("Error deleting: %s : %s" % (image_dir, e.strerror))

        except Exception as e:
            api.update_status(status="@" + tweet.user.screen_name + " This tweet has already been answered.", in_reply_to_status_id=tweet.id )
            print(e)
    return new_since_id

def main(api):

    #Interacción con el usuario, consulta
    hashtags=["#consult"]
    since_id = read_last_seen(FILE_NAME)
    since_id = check_mentions(api, hashtags, since_id)
    logger.info("Waiting...")
    store_last_seen(FILE_NAME, since_id)