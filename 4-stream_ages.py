#!/usr/bin/python3
"""
Module for memory-efficient aggregation using generators
"""
import mysql.connector
import seed


def stream_user_ages():
    """
    Generator function that yields user ages one by one
    
    Yields:
        int: User age
    """
    try:
        password = seed.get_password()
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password=password,
            database='ALX_prodev'
        )
        
        cursor = connection.cursor()
        cursor.execute("SELECT age FROM user_data")
        
        for (age,) in cursor:
            yield age
        
        cursor.close()
        connection.close()
        
    except mysql.connector.Error as err:
        print(f"Error: {err}")


def calculate_average_age():
    """
    Calculate the average age without loading entire dataset into memory
    Uses the stream_user_ages generator
    
    Returns:
        float: Average age of all users
    """
    total_age = 0
    count = 0
    
    for age in stream_user_ages():
        total_age += age
        count += 1
    
    if count == 0:
        return 0
    
    return total_age / count


if __name__ == "__main__":
    average_age = calculate_average_age()
    print(f"Average age of users: {average_age}")
