# ShyftLabs.io
Made by-Shreya Saxena for ShyftLabs. This is the GitHub repository for my Devlopment Technical Test.

### Tech stack used: 
1. Frontend-HTML/CSS for structure and styling.
2. Server-Python with Flask for handling HTTP requests and server logic, Flask extensions for additional functionalities, and Jinja for template rendering.
3. Backend-SQL for data storage, with SQLAlchemy as the ORM to interact with the database.
4. Wallpaper/images- Adobe Firefly(Generative Ai).

## The following steps are to be followed ti run the app:
## 1. Cloning the Repository

Navigate to your desired directory and clone the ShyftLabs_DTT repository.

For both Windows and macOS:

```sh
cd path/to/directory
git clone https://github.com/your-username/ShyftLabs_DTT.git
cd ShyftLabs_DTT
```
## 2. Creating a Virtual Environment

For Windows:
```sh
py -m venv .venv
.venv\Scripts\activate
```

For macOS:
```sh
python3 -m venv .venv
source .venv/bin/activate
```

## 3. Installing Dependencies

Ensure you are in the project directory and your virtual environment is activated before proceeding.

Install dependencies on mac:
```sh
pip install requests python-dotenv Flask
```
Upgrade pip (optional but recommended):
```sh
pip install --upgrade pip
```
Install Flask and extensions:
```sh
pip install flask flask-sqlalchemy flask-login
```
## 4. Running the Application

To run the application, ensure your virtual environment is activated and execute the main script:

For both Windows and macOS:
```sh
python main.py
```
The application will be running on http://127.0.0.1:5000 .

## Re-initialising the database 
If the user wants to re-initialise the database/start with a fresh database:
1. The user should navigate to the instance folder and delete the database.db file.
2. The user should then run the following command which will re-initialise the database and run the application again:
```sh
python main.py
```

## Manually checking the database
The application displays the list of students and courses and the database has been already been initialised with one student and one course.

However, if the user wants to check the content of the database:
1. The user should navigate to the instance folder and locate the database.db file.
2. Next, open the webiste https://inloop.github.io/sqlite-viewer/ and drag and drop or manually locate the file database.db on your file system and upload it to the website link given to view the contents of the database. 
