# Python Generators Project

## About
This project introduces advanced usage of Python generators to efficiently handle large datasets, process data in batches, and simulate real-world scenarios involving live updates and memory-efficient computations.

## Learning Objectives
- Master Python Generators using the `yield` keyword
- Handle Large Datasets with batch processing and lazy loading
- Simulate Real-world Scenarios with streaming data
- Optimize Performance using memory-efficient operations
- Apply SQL Knowledge for dynamic data fetching

## Requirements
- Python 3.x
- MySQL database
- Understanding of `yield` and generator functions
- Familiarity with SQL and database operations

## Project Structure
- `seed.py` - Database setup and data seeding
- `0-stream_users.py` - Stream database rows one by one
- `1-batch_processing.py` - Batch processing of large data
- `2-lazy_paginate.py` - Lazy loading with pagination
- `4-stream_ages.py` - Memory-efficient aggregation

## Tasks

### 0. Getting started with python generators
Set up MySQL database and seed with user data.

### 1. Generator that streams rows from an SQL database
Create a generator to fetch rows one by one from the database.

### 2. Batch processing Large Data
Fetch and process data in batches, filtering users over age 25.

### 3. Lazy loading Paginated Data
Implement lazy pagination to load pages only when needed.

### 4. Memory-Efficient Aggregation with Generators
Calculate average age using generators without loading entire dataset.
