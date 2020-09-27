#@author: bxnign  -- python BIG DATA BDY
import tweepy #libreria para conectar las API de twitter con PYTHON
import settings
from kafka import KafkaProducer
#tweetoyente es la clase con la cual haremos todos los rescate de informacion   
class TweetOyente(tweepy.StreamListener):

    def on_connect(self):
        print("Conectado!")

#en la definicion on_status es donde guardaremos la informacion y haremos el procesamiento
    def on_data(self, raw_data):
        producer.send('Twitter-data', raw_data.encode('utf-8'))



    def on_error(self, status_code):
        print("Error [CODIGO]: ",status_code)

# cadenas de autenticacion
consumer_key= "EgYTTM4N342QtN7ALGKUQPoR0"
consumer_secret= "nXJm35RJSM5B3Jdfl37jiQ0u8n23rNhaa1CP3NxwI28fLmx6pE"
access_token= "412828798-8frolCmaObbdjCNSykj8mxrU5yZIyZMm0AH6PESD"
access_token_secret= "2hvFE4BI3Ea1aOe4E3J1sYxGtYlYaZveZ0gnRiHfCcYaW"

#Realizando la autenticacion de la aplicacion de twitter creada en la paginda de DEVELOPER "(https://developer.twitter.com/en/apps/18103226)"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

#objeto API a el cual le entrego la autenticacion "auth" (auth que me entrega la aplicacion de twitter)
#este objeto realizara todas las llamadas de twitter al momento de rescatar los tweets  #con los dos parametros despues de auth, sirven para notificar cuando se llegue al 
#limite de descarga de datos
api = tweepy.API(auth, wait_on_rate_limit=True,
                 wait_on_rate_limit_notify=True)

stream_oyente = TweetOyente()
producer = KafkaProducer(bootstrap_servers='172.27.1.16:9092')
stream = tweepy.Stream(auth=api.auth, listener=stream_oyente)
stream.filter(track="PlayStation4")


