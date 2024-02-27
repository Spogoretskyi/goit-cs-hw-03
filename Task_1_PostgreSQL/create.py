import psycopg2


def create_db(conn, cur):
    with open("create_db.sql", "r") as f:
        sql = f.read()
    try:
        cur.execute(sql)
        conn.commit()
    except psycopg2.Error as e:
        print("Error tables creation:", e)
        conn.rollback()
