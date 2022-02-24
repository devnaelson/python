#https://pymysql.readthedocs.io/en/latest/index.html

import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='Admin123.',
                             database='python',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

with connection:
    
    with connection.cursor() as cursor:
        # Create a new record
        sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
        cursor.execute(sql, ('webmaster@python.org', 'very-secret'))

    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT `id` FROM `users`"
        cursor.execute(sql)
        result = cursor.fetchone()
        print(result)