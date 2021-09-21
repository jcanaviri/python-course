from Person import Person
from logger_file import log
from CursorPool import CursorPool

class PersonDAO:
    '''DAO means Data access object'''
    _SELECT = 'SELECT * FROM public.person ORDER BY person_id'
    _INSERT = 'INSERT INTO person(first_name, last_name, email) VALUES (%s, %s, %s)'
    _UPDATE = 'UPDATE public.person SET first_name=%s, last_name=%s, email=%s WHERE person_id=%s'
    _DELETE = 'DELETE FROM public.person WHERE person_id=%s'

    @classmethod
    def select(cls):
        with CursorPool() as cursor:
            cursor.execute(cls._SELECT)
            result = cursor.fetchall()
            person_list = []

            for item in result:
                person = Person(item[0], item[1], item[2], item[3])
                person_list.append(person)

            return person_list

    @classmethod
    def insert(cls, person):
        with CursorPool() as cursor:
            values = (person.first_name, person.last_name, person.email)
            cursor.execute(cls._INSERT, values)

            log.debug(f'Person to insert: {person}')
            return cursor.rowcount

    @classmethod
    def update(cls, person):
        with CursorPool() as cursor:
            values = (person.first_name, person.last_name, person.email, person.person_id)
            cursor.execute(cls._UPDATE, values)
                
            log.debug(f'Person was updated: {person}')

            return cursor.rowcount
    
    @classmethod
    def delete(cls, person):
        with CursorPool() as cursor:
            to_delete = (person.person_id, )
            cursor.execute(cls._DELETE, to_delete)
                
            log.debug(f'Deleted: {person}')

            return cursor.rowcount

if __name__ == '__main__':
    # Insert a person
    jaden = Person(first_name='Jaden', last_name='Smith', email='jaden@gmail.com')
    result = PersonDAO.insert(jaden)
    log.debug(f'Inserted: {result}')

    # Update a person
    bruno = Person(4, 'Bruce', 'Wayne', 'bruce@gmail.com')
    result = PersonDAO.update(bruno)
    log.debug(f'Person update: {result}')


    # Delete a person
    # john = Person(person_id=1)
    # del_persons = PersonDAO.delete(john)
    # log.debug(f'People deleted: {del_persons}')

    # Select all persons
    persons = PersonDAO.select()
    for p in persons:
        log.debug(p)
