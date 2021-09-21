from logger_file import log
from ConnPool import Connection 

class CursorPool:
    def __init__(self):
        self._conn = None
        self._cursor = None

    def __enter__(self):
        log.debug('With starts now')
        self._conn = Connection.get_connection()
        self._cursor = self._conn.cursor()
        return self._cursor

    def __exit__(self, exc_type, exc_value, traceback):
        log.debug('__exit__ was triggered')
        if exc_value:
            self._conn.rollback()
            log.error(f'Some error happend: {exc_value} {exc_type}, {traceback}')
        else:
            self._conn.commit()
            log.debug('Commit transaction')
        self._cursor.close()

if __name__ == '__main__':
    with CursorPool() as cursor:
        log.debug('Inside with statement')
        cursor.execute('SELECT * FROM public.person')
        log.debug(cursor.fetchall())
