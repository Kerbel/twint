import time
from multiprocessing import Process


from peewee import *
from multiprocessing import Pool

import twint

db = SqliteDatabase('tweets.db')


class tweets(Model):
    id = AutoField(primary_key=True)
    user_id = TextField()
    screen_name = TextField()

    class Meta:
        database = db


def download_user(screen_name):
    try:
        c = twint.Config()
        c.Username = screen_name
        c.Database = 'users.db'
        twint.run.Lookup(c)
    except Exception as e:
        print(e)


user_ids_query = tweets.select(tweets.user_id, tweets.screen_name)
for t in user_ids_query.iterator():
    p = Process(target=download_user, args=(str(t.screen_name),))
    p.start()
    time.sleep(0.1)



