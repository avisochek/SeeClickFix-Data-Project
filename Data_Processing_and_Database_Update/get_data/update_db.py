#!update_db.py
###first update local mongodb database,
###then update postgreSQL database.

from update_mongo import update_local_db

print "updating local db..."
update_local_db()