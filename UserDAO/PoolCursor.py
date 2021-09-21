from logger_file import log
from Conn import Connection 

class PoolCursor:
    def __init__(self):
        self._conn = None
        self._cursor = None

    def __enter__(self):
        self._conn = Connection.get_connection()
        self._cursor = self._conn.cursor()
        return self._cursor

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_value:
            self._conn.rollback()
            log.error(f'Some error happend: {exc_value} {exc_type}, {traceback}')
        else:
            self._conn.commit()
        self._cursor.close()

if __name__ == '__main__':
    with PoolCursor() as cursor:
        log.debug('Inside with statement')
        cursor.execute('SELECT * FROM public.user')
        log.debug(cursor.fetchall())
