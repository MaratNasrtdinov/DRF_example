# DRF_example
A simple example of my little api on Django rest framework

## Installation

1. Сreate and activate a new virtual environment:
   ```bash
   python3.9 -m venv ../venv
   source ../venv/bin/activate
   ```
   
2. Install the libraries:
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```
   
3. Make migrations, load the fixtures and start the server
   ```bash
   ./manage.py migrate
   ./manage.py loaddata <path_to_fixture_files>
   ./manage.py runserver 
   ```
