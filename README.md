# cowrywise_test
API for The Software Engineer (Backend) role assessment


## Setup Instructions

- Clone this repo
```
git clone https://github.com/cAtaman/cowrywise_backend_test.git
```

- Navigate to the project's root and start a virtual environment 
```
cd cowrywise_backend_test
```

- Create a virtual environment with python3
```
python3 -m virtualenv venv
```

- Activate the virtual environment with the following command:

  - Linux 
    ```
    source venv/bin/activate
    ```

  - Windows
    ```
    venv/Scripts/activate
    ```


- Install all dependencies
```
pip install -r requirements.txt
```

## To run the server 
- Windows
```
set FLASK_APP=app.py:application
flask run
```

- Linux
```
export FLASK_APP=app.py:application
flask run
```

### The UUIDs can be accessed at the "/new" route

Example: http://localhost:5000/new
