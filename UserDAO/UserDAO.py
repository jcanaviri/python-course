from User import User
from logger_file import log
from PoolCursor import PoolCursor

class UserDAO:
    '''DAO means Data access object'''
    _SELECT = 'SELECT * FROM public.user ORDER BY user_id'
    _INSERT = 'INSERT INTO public.user(username, password) VALUES (%s, %s)'
    _UPDATE = 'UPDATE public.user SET username=%s, password=%s WHERE user_id=%s'
    _DELETE = 'DELETE FROM public.user WHERE user_id=%s'

    @classmethod
    def select(cls):
        with PoolCursor() as cursor:
            cursor.execute(cls._SELECT)
            users = cursor.fetchall()
            user_list = []

            for user in users:
                u = User(user[0], user[1], user[2])
                user_list.append(u)

            return user_list

    @classmethod
    def insert(cls, user):
        with PoolCursor() as cursor:
            values = (user.username, user.password)
            cursor.execute(cls._INSERT, values)

            log.debug(f'User to insert: {user}')
            return cursor.rowcount

    @classmethod
    def update(cls, user):
        with PoolCursor() as cursor:
            values = (user.username, user.password, user.user_id)
            cursor.execute(cls._UPDATE, values)
            
            log.debug(f'user was updated: {user}')
            return cursor.rowcount
    
    @classmethod
    def delete(cls, user):
        with PoolCursor() as cursor:
            to_delete = (user.user_id, )
            cursor.execute(cls._DELETE, to_delete)
                
            log.debug(f'Deleted: {user}')

            return cursor.rowcount

if __name__ == '__main__':
    # Insert a person
    # erick = User(username='Stan', password='Stan123')
    # result = UserDAO.insert(erick)
    # log.debug(f'Inserted: {result}')

    # Update a person
    # kyle = User(1, 'Kyle', 'Kyle123')
    # result = UserDAO.update(kyle)
    # log.debug(f'User update: {result}')


    # # Delete a person
    # kyle = User(user_id=1)
    # deleted = UserDAO.delete(kyle)
    # log.debug(f'People deleted: {deleted}')

    # Select all persons
    users = UserDAO.select()
    for user in users:
        log.debug(user)
