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
            sql = 'INSERT INTO public.person(first_name, last_name, email) VALUES(%s, %s, %s);'
            me = ('Rocio', 'Caballero', 'rocio@gmail.com')
            cursor.execute(sql, me)

            sql2 = 'UPDATE public.person SET first_name=%s, last_name=%s, email=%s WHERE person_id=%s'
            values = ('Susan', 'Smith', 'susan@gmail.com', 2)
            cursor.execute(sql2, values)
except Exception as e:
    conn.rollback()
    print(f'Some error happend: {e}')
finally:
    conn.close()
