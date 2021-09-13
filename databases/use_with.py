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
    with conn:
        with conn.cursor() as cursor:
            sql = 'SELECT * FROM public.person;'
            cursor.execute(sql)
            result = cursor.fetchall()
            print(result) # the result is a list of tuples
except Exception as e:
    print(f'Some error happend: {e}')
finally:
    conn.close()
