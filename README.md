# ShyftLabs_DTT

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
