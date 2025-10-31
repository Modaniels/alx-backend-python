#!/usr/bin/python3
"""
Module for streaming users from database using generator
"""
import mysql.connector
import seed


def stream_users():
    """
    Generator function that streams rows from user_data table one by one
    
    Yields:
        dict: User data as dictionary with keys: user_id, name, email, age
    """
    try:
        password = seed.get_password()
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password=password,
            database='ALX_prodev'
        )
        
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM user_data")
        
        for row in cursor:
            yield row
        
        cursor.close()
        connection.close()
        
    except mysql.connector.Error as err:
        print(f"Error: {err}")
