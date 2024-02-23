. image:: /_static/OC-Lettings.png
   :align: center


Overview
========

This documentation outlines the objectives, improvements, and technical details of the `Python Project P13 Repository <https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR>`_ . It aims to provide comprehensive guidance for developers, testers, and stakeholders involved in the project.

1. Project Objectives
---------------------

The project focuses on enhancing the existing web application with Web 2.0 features and improvements. Key objectives include:

- Enhancing Modular Architecture: Restructuring the monolithic codebase into multiple distinct applications for improved flexibility, maintainability, and scalability.

- Addressing Various Project Issues: Resolving linting errors, fixing pluralization errors, improving error handling, documenting code, and implementing comprehensive testing.

- Implementing Error Monitoring with Sentry: Integrating Sentry for robust error monitoring and management, ensuring strategic placement of logs within the codebase.

- CI/CD Pipeline and Deployment: Establishing a CI/CD pipeline for automated testing, containerization, and deployment to production environments.

2. Technical Documentation ([link](https://python-p13.readthedocs.io/))
---------------------------------------------------------------------------------

The technical documentation covers various aspects of the project, including:

- Overview
- Project Description
- Installation Instructions
- Get started
- Technologies and Programming Languages
- Database structure
- API interfaces
- Deployment and Application Management Procedures

This documentation serves as a comprehensive resource for understanding and working with the P13_OC_LETTINGS project, promoting effective collaboration and smooth development processes.

2. Installation Instructions
----------------------------
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
