# User-Management-System

this is a simple user management system 

Follow these steps to run the project

1. open the terminal and type " pip install -r requirements.txt"
    this will install all the requires libraries

2. open postgressql and create a database according to your preference

3.now go to the "backend-intern-assignment" to use the project

4.now open src/utils/constants.py and enter all the details regarding the database such as DATABASE_USER, DATABASE_PASS, DATABASE_URL, DATABASE_DB.

5.now run the project by typing uvicorn main:app --host 0.0.0.0 --port 8000
 
6.now you can acces the api by opening the browser and typing "http://localhost:8000/docs"
