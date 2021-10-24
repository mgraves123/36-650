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
cur.execute("CREATE TABLE employees(id SERIAL, fname VARCHAR(10), lname VARCHAR(10))")

#running code throws error in Visual Studio Code, but works in jupyter notebook
#see image from jupyter notebook for Q6-Q8