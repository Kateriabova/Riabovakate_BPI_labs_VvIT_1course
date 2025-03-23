import sqlite3

shops = sqlite3.connect("shops.sqlite")
cur = shops.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS shop(
id INTEGER PRIMARY KEY,
name VARCHAR(255) UNIQUE,
balance FLOAT NOT NULL);
""")
shops.commit()
cur.execute("""CREATE TABLE IF NOT EXISTS product (
id INTEGER PRIMARY KEY,
name VARCHAR(255) NOT NULL,
price FLOAT NOT NULL);
""")
shops.commit()
cur.execute("""CREATE TABLE IF NOT EXISTS warehouse (
shop_id INTEGER REFERENCES shop (id),
product_id INTEGER REFERENCES product (id),
quantity INTEGER NOT NULL,
PRIMARY KEY (shop_id, product_id));
""")
shops.commit()

cur.execute("""INSERT INTO shop (id, name, balance) VALUES (1, 'пятерочка', 31)""")
shops.commit()
cur.execute("""INSERT INTO shop (id, name, balance) VALUES (2, 'перекресток',133)""")
shops.commit()
cur.execute("""INSERT INTO product VALUES (1, 'молоко', 100)""")
shops.commit()
cur.execute("""INSERT INTO product VALUES (2, 'хлеб', 25)""")
shops.commit()
cur.execute("""INSERT INTO product VALUES (3, 'хлеб', 30)""")
shops.commit()
cur.execute("""INSERT INTO warehouse VALUES (1, 1, 20)""")
shops.commit()
cur.execute("""INSERT INTO warehouse VALUES (1, 2, 10)""")
shops.commit()
cur.execute("""INSERT INTO warehouse VALUES (2, 1, 30)""")
shops.commit()
cur.execute("""INSERT INTO warehouse VALUES (2, 3, 30)""")
shops.commit()
cur.execute("""INSERT INTO shop (id, name, balance) VALUES (3, 'красное&белое',100)""")
shops.commit()
cur.execute("""INSERT INTO product VALUES (4, 'красное вино', 500)""")
shops.commit()
cur.execute("""INSERT INTO product VALUES (5, 'красное вино', 1500)""")
shops.commit()
cur.execute("""INSERT INTO product VALUES (6, 'макароны ', 80)""")
shops.commit()
cur.execute("""INSERT INTO warehouse VALUES (1, 6, 20)""")
shops.commit()
cur.execute("""INSERT INTO warehouse VALUES (2, 6, 30)""")
shops.commit()
cur.execute("""INSERT INTO warehouse VALUES (3, 4, 40)""")
shops.commit()
cur.execute("""INSERT INTO warehouse VALUES (2, 4, 30)""")
shops.commit()
cur.execute("""INSERT INTO warehouse VALUES (2, 5, 15)""")
shops.commit()
cur.execute("""INSERT INTO warehouse VALUES (3, 1, 10)""")
shops.commit()
cur.execute("""INSERT INTO warehouse VALUES (2, 2, 30)""")
shops.commit()
cur.execute("""CREATE TABLE IF NOT EXISTS worker (
worker_id INTEGER PRIMARY KEY,
shop_id INTEGER REFERENCES shop (id),
name VARCHAR(255),
salary INTEGER NOT NULL,
position VARCHAR(255))""")
shops.commit()
cur.execute("""INSERT INTO worker (worker_id, shop_id, name, salary, position) VALUES (1, 1, 'Галина', 30000, 'старший кассир')""")
shops.commit()
cur.execute("""INSERT INTO worker (worker_id, shop_id, name, salary, position) VALUES (2, 1, 'Геннадий', 25000, 'кассир')""")
shops.commit()
cur.execute("""INSERT INTO worker (worker_id, shop_id, name, salary, position) VALUES (3, 1, 'Алла', 25000, 'кассир')""")
shops.commit()
cur.execute("""INSERT INTO worker (worker_id, shop_id, name, salary, position) VALUES (4, 3, 'Карина', 20000, 'кассир')""")
shops.commit()
cur.execute("""INSERT INTO worker (worker_id, shop_id, name, salary, position) VALUES (6, 3, 'Егор', 25000, 'старший кассир')""")
shops.commit()
cur.execute("""INSERT INTO worker (worker_id, shop_id, name, salary, position) VALUES (7, 2, 'Галина', 40000, 'старший кассир')""")
shops.commit()
cur.execute("""INSERT INTO worker (worker_id, shop_id, name, salary, position) VALUES (5, 2, 'Кристина', 35000, 'кассир')""")
shops.commit()
cur.execute("""INSERT INTO worker (worker_id, shop_id, name, salary, position) VALUES (8, 2, 'Аглая', 35000, 'кассир')""")
shops.commit()