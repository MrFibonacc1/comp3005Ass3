import psycopg2

#This code creates the connect to the database and connects to it using the given details
def create_connection(db_name, db_user, db_password, db_host, db_port):
    connection = None
    try:
        connection = psycopg2.connect(
            dbname=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port
        )
        print("Connection was successful to the database")
    except Exception as e:
        print(f"The error '{e}' occurred")

    return connection

#This closes the connection to the database
def close_connection(connection):
    if connection:
        connection.close()
        print("Connection closed")

