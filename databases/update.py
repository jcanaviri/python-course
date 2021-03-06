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
            sql = '''UPDATE public.person SET first_name=%s, last_name=%s, email=%s WHERE person_id=%s'''

            print('Update user 1')
            first_name = input('New first name: ')
            last_name = input('New last first name: ')
            email = input('New email: ')

            values = (first_name, last_name, email, 1)
            cursor.execute(sql, values)
            # conn.commit() we don't need this because of the with statement
            counter = cursor.rowcount
            print(f'The counter values are: {counter}')
except Exception as e:
    print(f'Some error happend: {e}')
finally:
    conn.close()
