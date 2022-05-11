# cw_backend_test
API for The Software Engineer (Backend) role assessment


## Setup Instructions

- Clone this repo
```bash
git clone https://github.com/cAtaman/cowrywise_backend_test.git
```

- Navigate to the project's root and start a virtual environment 
```bash
cd cowrywise_backend_test
```

- Create and activate the virtual environment with the following commands:

  - Linux 
    ```bash
    python3 -m virtualenv venv
    source venv/bin/activate
    ```

  - Windows
    ```cmd
    python -m virtualenv venv
    venv\Scripts\activate
    ```


- Install all dependencies
```bash
pip install -r requirements.txt
```

- Run tests
```bash
pytest tests.py
```

## To run the server 
- Windows
```cmd
set FLASK_APP=app.py:application
flask run
```

- Linux
```bash
export FLASK_APP=app.py:application
flask run
```

### The UUIDs can be accessed at the "/new" route

Example: http://localhost:5000/new
