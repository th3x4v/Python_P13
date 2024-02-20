Installation Instructions
=========================

**Prerequisites**:

- GitHub account with read access to this repository
- Git CLI
- SQLite3 CLI
- Python interpreter, version 3.6 or higher

Throughout the documentation for local development, it is assumed that the `python` command in your OS shell runs the above Python interpreter (unless a virtual environment is activated).

- **Clone the repository**:

.. code-block:: bash

    cd /path/to/put/project/in
    git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git

- **Create the virtual environment**:

.. code-block:: bash

    cd /path/to/Python-OC-Lettings-FR
    python -m venv venv
    apt-get install python3-venv  # If the above step encounters errors with a package not found on Ubuntu
    source venv/bin/activate
    which python  # Confirm the `python` command runs the Python interpreter in the virtual environment
    python --version  # Confirm the Python interpreter version is 3.6 or higher
    which pip  # Confirm the `pip` command runs the pip executable in the virtual environment
    deactivate  # To deactivate the environment

- **Run the site**:

.. code-block:: bash

    cd /path/to/Python-OC-Lettings-FR
    source venv/bin/activate
    pip install --requirement requirements.txt
    python manage.py runserver

Go to `http://localhost:8000` in a browser.
Confirm that the site works and can be navigated (you should see multiple profiles and listings).

- **Linting**:

.. code-block:: bash

    cd /path/to/Python-OC-Lettings-FR
    source venv/bin/activate
    flake8

- **Unit Tests**:

.. code-block:: bash

    cd /path/to/Python-OC-Lettings-FR
    source venv/bin/activate
    pytest

- **Database**:

.. code-block:: bash

    cd /path/to/Python-OC-Lettings-FR
    sqlite3  # Open a shell session
    .open oc-lettings-site.sqlite3  # Connect to the database
    .tables  # Display tables in the database
    pragma table_info(Python-OC-Lettings-FR_profile);  # Display columns in the profiles table
    select user_id, favorite_city from Python-OC-Lettings-FR_profile where favorite_city like 'B%';  # Query the profiles table
    .quit  # Quit the shell

- **Administration Panel**:

Go to `http://localhost:8000/admin`.
Log in with the user `admin`, password `Abc1234!`.
