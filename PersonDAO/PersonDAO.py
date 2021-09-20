from Person import Person
from Connection import Connection
from logger_file import log

class PersonDAO:
    '''DAO means Data access object'''
    _SELECT = 'SELECT * FROM public.person ORDER BY person_id'
    _INSERT = 'INSERT INTO person(first_name, last_name, email) VALUES (%s, %s, %s)'
    _UPDATE = 'UPDATE public.person SET first_name=%s, last_name=%s, email=%s WHERE person_id=%s'
    _DELETE = 'DELETE FROM public.person WHERE person_id=%s'

    @classmethod
    def select(cls):
        with Connection.get_cursor() as cursor:
            cursor.execute(cls._SELECT)
            result = cursor.fetchall()
            person_list = []

            for item in result:
                person = Person(item[0], item[1], item[2], item[3])
                person_list.append(person)

            return person_list

    @classmethod
    def insert(cls, person):
        with Connection.get_connection() as conn:
            with conn.cursor() as cursor:
                values = (person.first_name, person.last_name, person.email)
                cursor.execute(cls._INSERT, values)

                log.debug(f'Person to insert: {person}')
                return cursor.rowcount

    @classmethod
    def update(cls, person):
        with Connection.get_connection() as conn:
            with conn.cursor() as cursor:
                values = (person.first_name, person.last_name, person.email, person.person_id)
                cursor.execute(cls._UPDATE, values)
                
                log.debug(f'Person was updated: {person}')

                return cursor.rowcount
    
    @classmethod
    def delete(cls, person):
        with Connection.get_connection() as conn:
            with conn.cursor() as cursor:
                to_delete = (person.person_id, )
                cursor.execute(cls._DELETE, to_delete)
                
                log.debug(f'Deleted: {person}')

                return cursor.rowcount

if __name__ == '__main__':
    # Insert a person
    # john = Person(first_name='Barry', last_name='Alen', email='john@gmail.com')
    # result = PersonDAO.insert(john)
    # log.debug(f'Inserted: {result}')

    # Update a person
    bruno = Person(4, 'Bruno', 'Diaz', 'batman@gmail.com')
    result = PersonDAO.update(bruno)
    log.debug(f'Person update: {result}')


    # Delete a person
    john = Person(person_id=1)
    del_persons = PersonDAO.delete(john)
    log.debug(f'People deleted: {del_persons}')

    # Select all persons
    persons = PersonDAO.select()
    for p in persons:
        log.debug(p)
