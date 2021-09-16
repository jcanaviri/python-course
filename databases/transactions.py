import psycopg2

# Credentials for database connection
conn = psycopg2.connect(
    user='postgres',
    password='Josue123$',
    host='localhost',
    port='5432',
    database='test_db'
)

try:
    conn.autocommit = False
    cursor = conn.cursor()
    sql = 'INSERT INTO public.person(first_name, last_name, email) VALUES(%s, %s, %s);'
    me = ('Josue', 'Canaviri', 'josue@gmail.com')
    cursor.execute(sql, me)
    conn.commit()
except Exception as e:
    conn.rollback()
    print(f'Some error happend: {e}')
finally:
    conn.close()
