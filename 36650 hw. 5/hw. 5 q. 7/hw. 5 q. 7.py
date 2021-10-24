#https://docs.python.org/3/library/random.html
#https://www.w3schools.com/python/ref_func_round.asp
#https://www.w3schools.com/sql/func_sqlserver_round.asp
#https://www.w3schools.com/sql/func_sqlserver_rand.asp

import subprocess
import sys
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
install("psycopg2")
import psycopg2
conn = psycopg2.connect(host="localhost", 
                        port="5432", 
                        user="postgres", 
                        password="hocuspocus", 
                        database="postgres")
cur = conn.cursor()
for val in range(499):
    cur.execute("INSERT INTO employees (id, fname, lname) VALUES ((SELECT a AS id FROM (SELECT random() as a FROM generate_series(1,1)) as _), (SELECT round(a::dec, 8) AS fname FROM (SELECT random() as a FROM generate_series(1,1)) as _), (SELECT round(a::dec, 8) AS lname FROM (SELECT random() as a FROM generate_series(1,1)) as _))")
#running code throws error in Visual Studio Code, but works in jupyter notebook
#see image from jupyter notebook for Q6-Q8