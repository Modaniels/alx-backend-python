#!/usr/bin/python3
"""
Database configuration module
"""
import os
import getpass

# Default database configuration
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'ALX_prodev'
}


def get_db_config():
    """
    Get database configuration from environment or prompt user
    
    Returns:
        dict: Database configuration
    """
    config = DB_CONFIG.copy()
    
    # Check if password is needed
    if not config['password']:
        # Try to get from environment variable first
        config['password'] = os.getenv('MYSQL_PASSWORD', '')
    
    return config


def prompt_password():
    """
    Prompt user for MySQL password if needed
    
    Returns:
        str: MySQL password
    """
    print("MySQL password required.")
    password = getpass.getpass("Enter MySQL root password (press Enter if no password): ")
    return password
