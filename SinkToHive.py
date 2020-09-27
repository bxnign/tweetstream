from pyhive import hive
import json
from kafka import KafkaConsumer

def conexion_hive(host_name,port,user,password,database):
    conn = hive.Connection(host=host_name,port=port,username=user,password=password,database=database, auth='CUSTOM')
    consumer = KafkaConsumer('Twiiter-data', bootstrap_servers='172.27.1.16:9092')
    cur = conn.cursor()
    for msg in consumer:
        tweet = json.loads(msg.value.decode("utf-8",'ignore'))
        print(tweet['text'])
        cur.execute('insert to default.tweet values ("'+ tweet['text']+'")')

if __name__ == '__main__':
    host_name = "172.27.1.7"
    port = "10000"
    user = "hive"
    password = "hive"
    database = "default"
    conexion_hive(host_name,port,user,password,database)