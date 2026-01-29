# Employee Payroll Management System

[![Python Version](https://img.shields.io/badge/python-3.6%2B-blue.svg)](https://www.python.org/downloads/)
[![MySQL](https://img.shields.io/badge/MySQL-8.0%2B-orange.svg)](https://www.mysql.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A comprehensive Python-based Employee Payroll Management System built for managing employee records and salary calculations. This project uses MySQL database for persistent data storage and provides a command-line interface for easy interaction.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Database Setup](#database-setup)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Documentation](#documentation)
- [Contributing](#contributing)
- [License](#license)
- [Author](#author)

## 🎯 Overview

This Employee Payroll Management System is designed as a Computer Science project (Class 12th, CBSE) to demonstrate database connectivity with Python and CRUD operations. The system allows users to manage employee records including personal information and salary details with automatic total salary calculations.

## ✨ Features

- **Add Employee Records**: Create new employee entries with ID, name, basic salary, and allowances
- **Display All Employees**: View complete list of all employee records in the database
- **Update Salary Information**: Modify employee salary details with automatic recalculation
- **Delete Employee Records**: Remove employee records from the database
- **Automatic Calculations**: Total salary automatically computed from basic salary and allowances
- **Data Persistence**: All data stored securely in MySQL database
- **User-Friendly Interface**: Simple menu-driven command-line interface

## 📦 Prerequisites

Before running this application, ensure you have the following installed:

- **Python 3.6 or higher** - [Download Python](https://www.python.org/downloads/)
- **MySQL Server 8.0 or higher** - [Download MySQL](https://dev.mysql.com/downloads/mysql/)
- **MySQL Connector for Python** - Installed via pip (see Installation section)

## 🚀 Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/liha23/HANSIKA.git
cd HANSIKA
```

### Step 2: Install Python Dependencies

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install mysql-connector-python
```

### Step 3: Verify MySQL Installation

Ensure MySQL Server is running on your system. You can check this by running:

```bash
mysql --version
```

## 🗄️ Database Setup

### Step 1: Start MySQL Server

Start your MySQL server (method varies by operating system).

### Step 2: Login to MySQL

```bash
mysql -u root -p
```

### Step 3: Create Database and Table

Execute the following SQL commands:

```sql
CREATE DATABASE company;
USE company;

CREATE TABLE employee (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(30) NOT NULL,
    basic_salary INT NOT NULL,
    allowance INT NOT NULL,
    total_salary INT NOT NULL
);
```

### Step 4: Configure Database Connection

Open `employee.py` and update the database connection parameters if needed:

```python
mydb = mysql.connector.connect(
    host="localhost",
    user="root",           # Change if needed
    password="root",       # Change to your MySQL password
    database="company"
)
```

## 💻 Usage

### Running the Application

```bash
python employee.py
```

### Menu Options

Once the application starts, you'll see the following menu:

```
1. Add Employee
2. Display Employees
3. Update Salary
4. Delete Employee
5. Exit
```

### Example Workflow

1. **Adding an Employee**:
   - Select option `1`
   - Enter Employee ID (e.g., 101)
   - Enter Employee Name (e.g., John Doe)
   - Enter Basic Salary (e.g., 50000)
   - Enter Allowance (e.g., 10000)
   - System automatically calculates and saves total salary (60000)

2. **Viewing Employees**:
   - Select option `2`
   - All employee records will be displayed

3. **Updating Salary**:
   - Select option `3`
   - Enter Employee ID to update
   - Enter new Basic Salary and Allowance
   - Total salary is recalculated automatically

4. **Deleting an Employee**:
   - Select option `4`
   - Enter Employee ID to delete
   - Record is removed from database

## 📁 Project Structure

```
HANSIKA/
├── employee.py                                    # Main application source code
├── requirements.txt                               # Python dependencies
├── .gitignore                                     # Git ignore file
├── LICENSE                                        # MIT License
├── README.md                                      # This file
├── CONTRIBUTING.md                                # Contribution guidelines
├── CODE_OF_CONDUCT.md                            # Code of Conduct
├── docs/                                          # Documentation folder
│   ├── Employee Payroll Management System - Project Report.docx
│   ├── Employee Payroll Management System - Project Report.pdf
│   ├── Front Page - Computer Science Project.docx
│   ├── PDF_UPDATE_INSTRUCTIONS.md
│   ├── front-page.html                           # Project front page template
│   └── images.jpg                                # School logo/image
└── scripts/                                       # Utility scripts
    └── convert_to_pdf.py                         # PDF conversion utility
```

## 📚 Documentation

This repository includes comprehensive project documentation in the `docs/` folder:

- **Project Report (DOCX)**: Complete project documentation with screenshots
- **Project Report (PDF)**: PDF version of the project report
- **PDF Update Instructions**: Guide for updating the PDF documentation
- **Front Page Template**: HTML template for project front page
- **Front Page (DOCX)**: Word document for project front page

All screenshots in the project report show authentic-looking Python IDLE and MySQL interfaces demonstrating actual program execution.

### Utility Scripts

The `scripts/` folder contains utility scripts:
- `convert_to_pdf.py`: Script to convert DOCX documentation to PDF format

## 🤝 Contributing

Contributions are welcome! Please read our [Contributing Guidelines](CONTRIBUTING.md) and [Code of Conduct](CODE_OF_CONDUCT.md) before getting started.

### Ways to Contribute

1. **Report Bugs**: Found a bug? Please open an issue with:
   - Clear description of the bug
   - Steps to reproduce
   - Expected vs actual behavior
   - Your environment details (OS, Python version, MySQL version)

2. **Suggest Features**: Have ideas for improvements? Open an issue with:
   - Feature description
   - Use case/benefit
   - Possible implementation approach

3. **Submit Pull Requests**: Want to contribute code?
   - Fork the repository
   - Create a feature branch (`git checkout -b feature/AmazingFeature`)
   - Commit your changes (`git commit -m 'Add some AmazingFeature'`)
   - Push to the branch (`git push origin feature/AmazingFeature`)
   - Open a Pull Request

### Development Guidelines

- Follow PEP 8 style guide for Python code
- Add comments for complex logic
- Test your changes thoroughly
- Update documentation if needed
- Keep commits focused and atomic

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

The MIT License is a permissive license that allows:
- ✅ Commercial use
- ✅ Modification
- ✅ Distribution
- ✅ Private use

## 👨‍💻 Author

**Hansika**
- School: Shree Kali Devi Vidya Mandir, Hansi
- Class: 12th (Computer Science)
- Session: 2025-2026
- GitHub: [@liha23](https://github.com/liha23)

## 🙏 Acknowledgments

- Teacher: Priyanka Mam
- School: Shree Kali Devi Vidya Mandir, Hansi
- Subject: Computer Science (083) - CBSE Class 12

---

**Note**: This is an educational project created for Computer Science curriculum requirements. It demonstrates database connectivity concepts using Python and MySQL.
