# Student Database Management System (Python + MySQL)
📌 Overview
This project is a Student Database Management System built using Python and MySQL.
It allows you to store, manage, and retrieve programming language details in a database using a simple command-line interface (CLI).

The system supports:

Adding new programming language records

Deleting records

Updating ratings

Searching by Language ID

Viewing all records

🚀 Features
Add Record: Insert new language details (ID, name, creator, release date, version, rating).

Delete Record: Remove a record using its Language ID.

Update Rating: Increase or decrease a language's rating.

Search by ID: Find a language by its unique ID.

Show All Records: Display all stored programming languages.

🛠️ Tech Stack
Programming Language: Python 3

Database: MySQL

Connector: mysql-connector-python

📂 Project Structure
bash
Copy
Edit
├── student_dbms.py    # Main Python script
└── README.md          # Project documentation
⚙️ Setup Instructions
1️⃣ Install MySQL
Download & install MySQL from:
https://dev.mysql.com/downloads/

2️⃣ Create Database & Table
Open MySQL shell and run:

sql
Copy
Edit
CREATE DATABASE programming_language;

USE programming_language;

CREATE TABLE program (
    lid INT PRIMARY KEY,
    name VARCHAR(50),
    cname VARCHAR(50),
    rdate VARCHAR(20),
    version INT,
    rating INT
);
3️⃣ Install Python Dependencies
bash
Copy
Edit
pip install mysql-connector-python
4️⃣ Configure Database Credentials
In the Python file, update the connection details if needed:

python
Copy
Edit
mycon = sqltor.connect(
    host='localhost',
    user='root',
    passwd='root',
    database='programming_language'
)
5️⃣ Run the Project
bash
Copy
Edit
python student_dbms.py
🖥️ Usage Example
mathematica
Copy
Edit
Programming Language Details
1. Add Record
2. Delete Record
3. Update Rating Record
4. Search Record On Based ID
5. Show All Records
6. Exit
Enter Your Choice: 1
Enter Language ID: 101
Enter Language Name: Python
Enter Creator Name: Guido van Rossum
Enter Release Date: 1991
Enter Version: 3
Enter Ratings: 10
📌 Notes
Ensure MySQL service is running before executing the script.

Modify the database connection credentials if your MySQL setup differs.

Error handling can be improved for production use.

📜 License
This project is licensed under the MIT License — you are free to use, modify, and distribute it.
