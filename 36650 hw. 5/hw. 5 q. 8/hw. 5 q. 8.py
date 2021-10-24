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
cur.execute("select * from employees limit 10")
print (cur.description)
for row in cur:
    print (row)

#running code throws error in Visual Studio Code, but works in jupyter notebook
#see image from jupyter notebook for Q6-Q8