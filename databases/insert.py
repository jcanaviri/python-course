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
            sql = '''INSERT INTO public.person(first_name, last_name, email)
                        VALUES(%s, %s, %s)'''
            values = ('Rocio', 'Caballero', 'rocio@gmail.com')
            cursor.execute(sql, values)
            # conn.commit() we don't need this because of the with statement
            counter = cursor.rowcount
            print(f'The counter values are: {counter}')
except Exception as e:
    print(f'Some error happend: {e}')
finally:
    conn.close()
