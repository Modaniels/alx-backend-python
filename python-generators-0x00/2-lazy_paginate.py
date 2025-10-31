#!/usr/bin/python3
"""
Module for lazy loading paginated data from database
"""
import mysql.connector
import seed


def paginate_users(page_size, offset):
    """
    Fetches a page of users from the database
    
    Args:
        page_size (int): Number of rows to fetch
        offset (int): Starting position for fetching rows
        
    Returns:
        list: List of user data as dictionaries
    """
    connection = seed.connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    cursor.execute(f"SELECT * FROM user_data LIMIT {page_size} OFFSET {offset}")
    rows = cursor.fetchall()
    cursor.close()
    connection.close()
    return rows


def lazy_pagination(page_size):
    """
    Generator function that implements lazy pagination
    Only fetches the next page when needed
    
    Args:
        page_size (int): Number of rows per page
        
    Yields:
        list: Page of user data as list of dictionaries
    """
    offset = 0
    while True:
        page = paginate_users(page_size, offset)
        if not page:
            break
        yield page
        offset += page_size
