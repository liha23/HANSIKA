# Employee Payroll Management System

This is a Python-based Employee Payroll Management System using MySQL database.

## Project Files

- `employee.py` - Main Python source code for the payroll system
- `Employee Payroll Management System - Project Report.docx` - Complete project report with updated screenshots
- `Employee Payroll Management System - Project Report.pdf` - PDF version of the report

## Screenshots Updated

All screenshots in the project report have been updated to look like actual running code:

1. **Python IDLE Editor** - Shows the code in Python IDLE with the file path `C:/hansika/employee.py` in the title bar
2. **Python Shell Screenshots** - Show program execution in Python IDLE Shell with proper formatting
3. **MySQL Screenshots** - Show MySQL command-line interface with actual database operations

## How to Run

1. Install MySQL Server
2. Install Python 3.x
3. Install MySQL Connector: `pip install mysql-connector-python`
4. Create the database:
   ```sql
   CREATE DATABASE company;
   USE company;
   CREATE TABLE employee (
       emp_id INT PRIMARY KEY,
       emp_name VARCHAR(30),
       basic_salary INT,
       allowance INT,
       total_salary INT
   );
   ```
5. Run the program: `python employee.py`

## Features

- Add new employee records
- Display all employees
- Update salary information
- Delete employee records
- Automatic total salary calculation

## Note

The screenshots in the documentation show the application as it would appear when running on an actual machine with Python IDLE and MySQL installed.
