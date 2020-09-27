#by bxnign  -- python BIG DATA BDY
import tweepy #libreria para conectar las API de twitter con PYTHON
import settings
#tweetoyente es la clase con la cual haremos todos los rescate de informacion   
class TweetOyente(tweepy.StreamListener):

    def on_connect(self):
        print("Conectado!")

#en la definicion on_status es donde guardaremos la informacion y haremos el procesamiento
    def on_status(self, status):
         print(status.user.screen_name,"+", status.text,"+", status.user.location) 
         
        


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

stream = TweetOyente()
#variable que instancia el stream  "api.auth es la autenticacion"
streamingaApi = tweepy.Stream(auth=api.auth, listener=stream)

#filtro el steam api por distintos parametros, estos parametros pueden ser:
#follows= filtra por el ID de un usuario, por lo cual solo va a obtener la ID de ese usuario
#track= filtra por topico
#location= filtra por lugar, se le entrega la cordenada que te entrega google maps o cualquier mapa 

#usuario = api.me()
#print(usuario)

streamingaApi.filter(
    #follow=["118527527"]
    track=(settings.TERMS)


)


