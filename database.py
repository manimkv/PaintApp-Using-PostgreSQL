import psycopg2


cur = con.cursor()
cur.execute("DROP TABLE IF EXISTS savedimage")
cur.execute("CREATE TABLE savedimage(id serial,title text,imagedata text)")
con.commit()
con.close()
