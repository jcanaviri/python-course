import psycopg2 as db, pool
import sys

from logger_file import log

class Connection:
    _DATABASE = 'test_db'
    _USERNAME = 'postgres'
    _PASSWORD = 'Josue123$'
    _DB_PORT = '5432'
    _HOST = '127.0.0.1'
    _MIN_CONN = 1
    _MAX_CONN = 5
    _pool = None

    @classmethod
    def get_pool(cls):
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(
                    cls._MIN_CONN, 
                    cls._MAX_CONN,
                    host=cls._HOST,
                    user=cls._USERNAME,
                    password=cls._PASSWORD,
                    port=cls._DB_PORT,
                    database=cls._DATABASE)
                
                log.debug(f'Pool created Successfully {cls._pool}')
                return cls._pool
            except Exception as e:
                log.error(f'An error in pool happend')
                sys.exit()
        else:
            return cls._pool

    @classmethod
    def get_connection(cls):
        if cls._conn == None:
            try:
                cls._conn = db.connect(host=cls._HOST,
                                        user=cls._USERNAME,
                                        password=cls._PASSWORD,
                                        port=cls._DB_PORT,
                                        database=cls._DATABASE)
                log.debug(f'Successfully conected: {cls._conn}')
                return cls._conn
            except Exception as e:
                log.error(f'No conected: {e}')
                sys.exit()
        else:
            return cls._conn

    @classmethod
    def get_cursor(cls):
        if cls._cursor == None:
            try:
                cls._cursor = cls.get_connection().cursor()
                log.debug(f'The cursor is open {cls._cursor}')
                return cls._cursor
            except Exception as e:
                log.error(f'No cursor: {e}')
                sys.exit()
        else:
            return cls._cursor

if __name__ == "__main__":
    Connection.get_connection()
    Connection.get_cursor()
