# Food Order Database Python:
A Python project that uses SQLite to manage foods and customer orders.

# Features:
* Create a foods table
* Create an orders table
* Add food items to the database
* Add orders to the database
* Search for foods
* Display orders
* Calculate the total price of an order

# Technologies Used:
* Python
* SQLite
* `sqlite3` module
* SQL

# Database Structure:
## Foods Table:
The `foods` table contains:

| Column  | Type    | Description |
| ------- | ------- | ----------- |
| `id`    | INTEGER | Food ID     |
| `name`  | TEXT    | Food name   |
| `price` | INTEGER | Food price  |

## Orders Table:
The `orders` table contains:

| Column     | Type    | Description             |
| ---------- | ------- | ----------------------- |
| `id`       | INTEGER | Order ID                |
| `food_id`  | INTEGER | ID of the ordered food  |
| `quantity` | INTEGER | Number of ordered items |

## How It Works:
The program connects to a SQLite database named `data.python`.
It creates two tables:
* `foods`
* `orders`
The program adds several food items to the `foods` table and creates an order using the food ID and quantity.
It then uses a SQL `JOIN` to connect the foods and orders tables and calculate the total price.
The total price is calculated by multiplying the food price by the order quantity.

## SQL Operations Demonstrated:
* `CREATE TABLE`
* `INSERT`
* `DELETE`
* `SELECT`
* `JOIN`

## Files:
* `p8.py` — Main Python program
* `data.python` — SQLite database file created by the program

## How to Run:
Run the following command in the terminal:

```bash id="q3s8f2"
python p8.py
```

The program will create the SQLite database and display food information, order information, and the calculated total price.

