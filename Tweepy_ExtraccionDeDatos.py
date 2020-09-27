#by bxnign  -- python BIG DATA BDY

import tweepy #libreria para conectar las API de twitter con PYTHON
import json    #Para visualizar los datos de manera comoda

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

#PRUEBA (RESCATANDO MIS PROPIOS DATOS)
#data_me = api.me()
#print(json.dumps(data_me._json, indent=2))

#obteniendo informacion de otros usuarios
data_other = api.get_user("bxnign")
print(json.dumps(data_other._json, indent=2))

#obtener followers de un usuario
#data_follows = api.followers(screen_name="nike")
#for user in data:
#    print(json.dumps(user.__json,indent=2))

#obtener informacion a traves del objeto cursor
#for user in tweepy.Cursor(api.followers, screen_name="nike").items(100):
#    print(json.dumps(user._json,indent=2))

#obtener TIMELINE (tweets del usuario)  
#for tweet in tweepy.Cursor(api.user_timeline, screen_name="me", tweet_mode="extended").items(1):
#    print(json.dumps(tweet._json, indent=2))

#rescatando ultimos 2 tweet mios a traves del objeto cursor, con el parametro user
#for i in tweepy.Cursor(api.user_timeline, screen_name="bxnign", tweet_mode="extended").items(5):
#    print(i._json["full_text"])

