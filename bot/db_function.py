import connect


###создание таблицы(1 раз)###
conn, cur = connect.connect_db()
cur.execute(("""CREATE TABLE IF NOT EXISTS users(
    id SERIAL PRIMARY KEY,
    user_id VARCHAR(255) NOT NULL,
    photo_id VARCHAR(255) NOT NULL,
    fullname TEXT,
    link VARCHAR(255),
    address VARCHAR(255),
    size VARCHAR(10),
    price INT
    );
    """))


conn.commit()
    
    
###добавление информации о пользователе в бд###
async def add_user_to_db(user_id, photo_id, fullname, link, address, size, price) -> None:
    try:
        conn, cur = connect.connect_db()
    
        cur.execute("""INSERT INTO users (user_id, photo_id, fullname, link, address, size, price) 
                   VALUES (%s, %s, %s, %s, %s, %s, %s)""",
                (user_id, photo_id, fullname, link, address, size, price))
        conn.commit()
        print(f"Пользователь {fullname} с user_id {user_id} успешно добавлен в базу, данных.")
    except Exception as e:
        print(f"Ошибка при добавлении пользователя в базу данных:{e}")
    
    
###полчение информации о заказе из бд###
async def get_user_data(user_id: int) -> dict:
    try:
        conn, cur = connect.connect_db()
        query = """SELECT fullname, photo_id, link, address, size, price FROM users WHERE user_id = %s"""
        cur.execute(query, (str(user_id),))
        row = cur.fetchone()
        if row:
            return {
                'photo_id': row[0],
                'fullname': row[1],
                'link': row[2],
                'address': row[3],
                'size': row[4],
                'price': row[5]
            }
        else:
            return None
    finally:
        print(f"Данные успешно отправлены пользователю")