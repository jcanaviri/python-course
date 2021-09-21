from psycopg2 import pool

from logger_file import log

class Connection:
    _DATABASE = 'test_db'
    _USERNAME = 'postgres'
    _PASSWORD = 'Josue123$'
    _DB_PORT = '5432'
    _HOST = '127.0.0.1'
    _MIN_CON = 1
    _MAX_CON = 5
    _pool = None

    @classmethod
    def get_pool(cls):
        if cls._pool is None:
            try:
               cls._pool = pool.SimpleConnectionPool(
                   cls._MIN_CON,
                   cls._MAX_CON,
                   host=cls._HOST,
                   user=cls._USERNAME,
                   password=cls._PASSWORD,
                   port=cls._DB_PORT,
                   database=cls._DATABASE
               )
               return cls._pool
            except Exception as e:
                log.error(f'Some error happend in pool: {e}')
        else:
            return cls._pool

    @classmethod
    def get_connection(cls):
        conn = cls.get_pool().getconn()
        return conn

    @classmethod
    def clone_conn(cls):
        cls.get_pool().closeall()

    @classmethod
    def free_conn(cls, conn):
        cls.get_pool().putconn(conn)

if __name__ == "__main__":
    conn1 = Connection.get_connection()
    Connection.free_conn(conn1)
    
    conn2 = Connection.get_connection()

    conn3 = Connection.get_connection()
    conn4 = Connection.get_connection()
    conn5 = Connection.get_connection()
