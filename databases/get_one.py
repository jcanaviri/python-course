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
            sql = 'SELECT * FROM public.person WHERE person_id=%s;'
            person_id = input('Write the person_id that you want: ')
            cursor.execute(sql, (person_id,))
            result = cursor.fetchone()
            if not result:
                print(f'There is no user with id {person_id}')
            else:
                print(result)
except Exception as e:
    print(f'Some error happend: {e}')
finally:
    conn.close()
