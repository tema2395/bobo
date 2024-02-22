import psycopg2


###подключение к бд###
def connect_db() -> tuple:
    """ Create connection for db

        return `psycopg2.connect` and `cursor`
    """
    conn = psycopg2.connect(host = 'localhost', dbname = 'users_orders', user = 'absq', 
                            password = '2205', port = '5432')
    
    cur = conn.cursor()
    return conn, cur
