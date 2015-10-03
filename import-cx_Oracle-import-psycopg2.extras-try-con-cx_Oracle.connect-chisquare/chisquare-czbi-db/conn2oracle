import cx_Oracle
import psycopg2.extras


try:
    #connection to oracle
    con = cx_Oracle.connect('<username>/<password>@<hostname>/<service_name>')
    #connection to postgresql
    conn_string = "host={} dbname={} user={} password={}".format('<hostname>','<dbname>','<user>','<password>')
    #priting success details
    print (con.version)
    conn = psycopg2.connect(conn_string)
    pgcur = conn.cursor()
except Exception as e:
    print("encountered error while connecting to the DB {}".format(e))

for mon in range(0, 21):
    cur = con.cursor()
    SQL = <sql statement for data fetchfrom oracle>
    
    cur.execute(SQL)p
    #fetching all data in one go
    rows = cur.fetchall()
    
    for row in rows:
        # "row" array contains the data that has been fetched from oracle create insert statement to insert into potgresql
        inssql="<insert statement>";
        #execute insert
        pgcur.execute(inssql);
    conn.commit()
pgcur.close()
conn.close()
cur.close()
con.close()
