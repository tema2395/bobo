import connect

###Creating a table(1 time)###
conn, cur = connect.connect_db()
cur.execute(
    (
        """CREATE TABLE IF NOT EXISTS users(
    id SERIAL PRIMARY KEY,
    user_id VARCHAR(255) NOT NULL,
    fullname VARCHAR(255),
    link VARCHAR(255),
    address VARCHAR(255),
    size VARCHAR(255),
    price INT
    );
    """
    )
)


conn.commit()


async def add_user_to_db(user_id, fullname, link, address, size, price) -> None:
    "Adding user information to the database"
    try:
        conn, cur = connect.connect_db()

        cur.execute(
            """INSERT INTO users (user_id, fullname, link, address, size, price) 
                   VALUES (%s, %s, %s, %s, %s, %s)""",
            (user_id, fullname, link, address, size, price),
        )
        conn.commit()
        print(
            f"Пользователь {fullname} с user_id {user_id} успешно добавлен в базу данных."
        )
    except Exception as e:
        print(f"Ошибка при добавлении пользователя в базу данных:{e}")


async def get_user_data(user_id: int) -> dict:
    "Getting order information from the database"
    try:
        conn, cur = connect.connect_db()
        query = """SELECT fullname, link, address, size, price FROM users WHERE user_id = %s"""
        cur.execute(query, (str(user_id),))
        row = cur.fetchall()[-1]
        if row:
            return {
                "fullname": row[0],
                "link": row[1],
                "address": row[2],
                "size": row[3],
                "price": row[4],
            }
        else:
            return None
    finally:
        cur.close()
        conn.close()
        print(f"Данные успешно отправлены пользователю")
