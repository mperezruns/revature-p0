# import psycopg


# The conn variable is where I am connecting my Postgres database from pycharm
# conn = psycopg.connect(host="localhost", port="5432", dbname="prj0", user="postgres", password="@zul@6")
#
# cur = conn.cursor() # Retrieve a crusor object from our connection object
# Cursor objects allow us to send queries to the Postgres database
#
# cur.execute("SELECT * FROM customers")  # This will send query to the project-0 database
#
# string


# print(cur.fetchone())   # (1, 'Perez', 'Mark', '626-833-4002', 'Azusa', True) <- Tuple
# print(cur.fetchone())   # (2, 'Granados', 'Ayla', '626-822-7008', 'Castro Valley', True) <- Tuple
# print(cur.fetchone())   # (3, 'Cota', 'Daniel', '626-852-9090', 'Chino Hills', True) <- Tuple
# print(cur.fetchone())   # (4, 'Ruelas', 'Trinity', '626-878-8888', 'Fullerton', True) <- Tuple

# my_customers = cur.fetchall()  # Return a list of tuples
# print(my_customers)

# for record in cur:
#     print(record[1:3]) # customer_name

# Insert data
# m = cur.execute("INSERT INTO customers (last_name, first_name, customer_phone, customer_city) VALUES ('Martinez', 'Mario', '512-826-0008', 'La Verne')")
# print(m)
#
# conn.commit()   # Notice we commit using the connection object and not the cursor object
# We need to commit because psycopg by default doest not automatically commit DML commands
# Autocommit is turned off for psycopg (we can turn it on if we want to)

# conn.close()    # the close() method is where I will close the connection
