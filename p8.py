import sqlite3

#-----------------------------------------------------------------------------------------------------------------
#Connecting to the food database
db = sqlite3.connect("data.python")
cur = db.cursor()

#Creating foods table
cur.execute(
    """
    CREATE TABLE IF NOT EXISTS foods (
        id  INTEGER PRIMARY KEY,
        name TEXT,
        price INTEGER
    )
    """
)

# List of food 
new_foods = [
    ("pizza", 400000),
    ("pasta", 500000),
    ("burger", 550000),
    ("Cheeseburger", 600000),
    ("Breaded mushrooms", 300000)
]

# Delete all foods
cur.execute("DELETE FROM foods")

#--------------------------------------------------------------------------------------------------------------
#Creating orders table
cur.execute(
    """
    CREATE TABLE IF NOT EXISTS orders (
        id  INTEGER PRIMARY KEY,
        food_id INTEGER,
        quantity INTEGER
    )
    """
)

#----------------------------------------------------------------------------------------------------------------
#insert query foods
cur.executemany("""INSERT INTO foods(name, price) VALUES(?,?)""" , new_foods)
db.commit()

#search qurery
cur.execute("SELECT * FROM foods WHERE name = ?", ('burger',) )
result = cur.fetchall()
print(result)
#----------------------------------------------------------------------------------------------------------------
# Delete old orders
cur.execute("DELETE FROM orders")
db.commit()

#insert query orders
cur.execute("""INSERT INTO orders(food_id, quantity) VALUES(?,?)""", (3, 1) )
db.commit()

#search qurery
cur.execute("SELECT * FROM orders ")
result = cur.fetchall()
print(result)

#------------------------------------------------------------------------------------------------------------------
#Calculate total price
cur.execute("""
            SELECT foods.name , foods.price, orders.quantity, foods.price * orders.quantity
            FROM foods
            JOIN orders
            ON foods.id = orders.food_id
            """)
result = cur.fetchall()
for item in result:
    print("Food:", item[0])
    print("Price:", item[1])
    print("Quantity:", item[2])
    print("Total:", item[3])





db.close()