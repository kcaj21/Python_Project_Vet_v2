import psycopg2  
import psycopg2.extras as ext
import os



# DATABASE_URL = 'postgres://poufywjyblxian:8a0302bc724daaf7bccade249d45f173e7240912f943eda93b4e116f94e343ac@ec2-54-208-11-146.compute-1.amazonaws.com:5432/deff1uvmaa8k2q'

DATABASE_URL = os.environ.get('DATABASE_URL')

def run_sql(sql, values = None):
    conn = None
    results = []
    
    try:
        # conn=psycopg2.connect(DATABASE_URL, sslmode='require')
        conn=psycopg2.connect("dbname='vet_database'", sslmode='require')
        cur = conn.cursor(cursor_factory=ext.DictCursor)   
        cur.execute(sql, values)
        conn.commit()
        results = cur.fetchall()
        cur.close()           
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    return results
