
import psycopg2

def connect():
    """ Connect to the PostgreSQL database server """
    conn = psycopg2.connect(
    host="localhost",
    database="pagila",
    user="postgres",
    password="postgres")
    try:
        
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
		
        # create a cursor
        cur = conn.cursor()
        
	# execute a statement
        cur.execute('select * from "actor"')

        # display the PostgreSQL database server version
        db_version = cur.fetchmany(5)
        # db_version = cur.fetchall()
        # db_version = cur.fetchone()
        for i in db_version:
            print(i)
        
       
	# close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')

if __name__ == '__main__':
    connect()