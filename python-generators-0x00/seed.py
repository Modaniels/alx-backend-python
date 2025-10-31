#!/usr/bin/python3
"""
Module for database setup and seeding with user data
"""
import mysql.connector
import csv
import uuid
import os
import getpass

# Global password storage
_mysql_password = None


def get_password():
    """Get MySQL password from user input"""
    global _mysql_password
    if _mysql_password is None:
        _mysql_password = getpass.getpass("Enter MySQL root password (press Enter if no password): ")
    return _mysql_password


def connect_db():
    """
    Connects to the MySQL database server
    
    Returns:
        connection: MySQL connection object or None if connection fails
    """
    try:
        password = get_password()
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password=password
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None


def create_database(connection):
    """
    Creates the database ALX_prodev if it does not exist
    
    Args:
        connection: MySQL connection object
    """
    try:
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev")
        cursor.close()
    except mysql.connector.Error as err:
        print(f"Error creating database: {err}")


def connect_to_prodev():
    """
    Connects to the ALX_prodev database in MySQL
    
    Returns:
        connection: MySQL connection object to ALX_prodev database
    """
    try:
        password = get_password()
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password=password,
            database='ALX_prodev'
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error connecting to ALX_prodev: {err}")
        return None


def create_table(connection):
    """
    Creates a table user_data if it does not exist with the required fields
    
    Args:
        connection: MySQL connection object to ALX_prodev database
    """
    try:
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS user_data (
                user_id CHAR(36) PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                email VARCHAR(255) NOT NULL,
                age DECIMAL NOT NULL,
                INDEX(user_id)
            )
        """)
        connection.commit()
        print("Table user_data created successfully")
        cursor.close()
    except mysql.connector.Error as err:
        print(f"Error creating table: {err}")


def insert_data(connection, csv_file):
    """
    Inserts data into the database if it does not exist
    
    Args:
        connection: MySQL connection object to ALX_prodev database
        csv_file: Path to the CSV file containing user data
    """
    try:
        cursor = connection.cursor()
        
        # Check if data already exists
        cursor.execute("SELECT COUNT(*) FROM user_data")
        count = cursor.fetchone()[0]
        
        if count > 0:
            print("Data already exists in user_data table")
            cursor.close()
            return
        
        # Read and insert data from CSV
        if not os.path.exists(csv_file):
            print(f"CSV file {csv_file} not found")
            cursor.close()
            return
            
        with open(csv_file, 'r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                # Generate UUID for user_id if not present
                user_id = row.get('user_id', str(uuid.uuid4()))
                name = row.get('name', '')
                email = row.get('email', '')
                age = row.get('age', 0)
                
                cursor.execute(
                    "INSERT INTO user_data (user_id, name, email, age) VALUES (%s, %s, %s, %s)",
                    (user_id, name, email, age)
                )
        
        connection.commit()
        print(f"Data inserted successfully from {csv_file}")
        cursor.close()
        
    except mysql.connector.Error as err:
        print(f"Error inserting data: {err}")
    except Exception as e:
        print(f"Error reading CSV file: {e}")
