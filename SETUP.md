# Setup and Testing Guide

## Prerequisites

1. **MySQL Server** - Install and start MySQL server on your machine
   - Windows: Download from [MySQL Downloads](https://dev.mysql.com/downloads/installer/)
   - Verify MySQL is running: `mysql -u root -p`

2. **Python 3.x** - Already configured with virtual environment

3. **MySQL Connector** - Already installed ✅

## Step-by-Step Setup

### 1. Configure Database Credentials

Edit the database connection settings in the Python files if your MySQL credentials are different:
- Default: `host='localhost'`, `user='root'`, `password=''`
- Files to update: `seed.py`, `0-stream_users.py`, `1-batch_processing.py`, `4-stream_ages.py`

### 2. Test Database Setup (Task 0)

```powershell
cd "c:\Users\Modaniels\OneDrive\Documents\Work\-alx-backend-python\python-generators-0x00"
python 0-main.py
```

**Expected Output:**
```
connection successful
Table user_data created successfully
Database ALX_prodev is present
[(user_id, name, email, age), ...]
```

### 3. Test User Streaming (Task 1)

```powershell
python 1-main.py
```

**Expected Output:**
First 6 users printed as dictionaries

### 4. Test Batch Processing (Task 2)

```powershell
python 2-main.py
```

**Expected Output:**
All users with age > 25 printed

To see only first 5:
```powershell
python 2-main.py | Select-Object -First 5
```

### 5. Test Lazy Pagination (Task 3)

```powershell
python 3-main.py
```

**Expected Output:**
All users printed in pages of 100

To see only first 7:
```powershell
python 3-main.py | Select-Object -First 7
```

### 6. Test Memory-Efficient Aggregation (Task 4)

```powershell
python 4-stream_ages.py
```

**Expected Output:**
```
Average age of users: XX.XX
```

## Troubleshooting

### MySQL Connection Error
- Ensure MySQL server is running
- Verify credentials in the Python files
- Check if port 3306 is accessible

### Module Import Error
- Ensure you're in the correct directory
- Activate virtual environment if needed

### CSV File Not Found
- Verify `user_data.csv` exists in the directory
- Check file path in `seed.py`

## Project Structure

```
python-generators-0x00/
├── README.md                 # Project documentation
├── SETUP.md                  # This file
├── seed.py                   # Database setup and seeding
├── 0-stream_users.py        # Task 1: Stream users
├── 1-batch_processing.py    # Task 2: Batch processing
├── 2-lazy_paginate.py       # Task 3: Lazy pagination
├── 4-stream_ages.py         # Task 4: Average calculation
├── 0-main.py                # Test for Task 0
├── 1-main.py                # Test for Task 1
├── 2-main.py                # Test for Task 2
├── 3-main.py                # Test for Task 3
├── user_data.csv            # Sample data
└── .env.example             # Configuration template
```

## Key Concepts Demonstrated

1. **Python Generators** - Using `yield` for memory efficiency
2. **Database Streaming** - Fetching data without loading all at once
3. **Batch Processing** - Processing data in chunks
4. **Lazy Loading** - Loading data only when needed
5. **Memory Optimization** - Computing aggregates without full data load

## Notes

- All generators use the `yield` keyword
- Loop count constraints are met in each function
- Database connections are properly closed
- Error handling is implemented
