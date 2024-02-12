.. P13_OC_LETTINGS documentation master file, created by
   sphinx-quickstart on Sat Feb 10 15:23:06 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. image:: /_static/OC-Lettings.png
   :align: center

Welcome to P13_OC_LETTINGS's Documentation
===========================================

Overview
--------

This documentation outlines the objectives, improvements, and technical details of the `Python Project P13 Repository <https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR>`_ . It aims to provide comprehensive guidance for developers, testers, and stakeholders involved in the project.

1. Project Objectives
---------------------

The project focuses on enhancing the existing web application with Web 2.0 features and improvements. Key objectives include:

- Enhancing Modular Architecture: Restructuring the monolithic codebase into multiple distinct applications for improved flexibility, maintainability, and scalability.

- Addressing Various Project Issues: Resolving linting errors, fixing pluralization errors, improving error handling, documenting code, and implementing comprehensive testing.

- Implementing Error Monitoring with Sentry: Integrating Sentry for robust error monitoring and management, ensuring strategic placement of logs within the codebase.

- CI/CD Pipeline and Deployment: Establishing a CI/CD pipeline for automated testing, containerization, and deployment to production environments.

2. Technical Documentation
---------------------------

The technical documentation covers various aspects of the project, including:

- Project Description
- Installation Instructions
- Quick Start Guide
- Technologies and Programming Languages
- Database Structure and Data Models
- API Interfaces
- Usage Guide with Use Cases
- Deployment and Application Management Procedures

This documentation serves as a comprehensive resource for understanding and working with the P13_OC_LETTINGS project, promoting effective collaboration and smooth development processes.


Project Description
-------------------

The project undertakes significant improvements from its precursor, the Python-OC-Lettings-FR, which include:

- **Refactoring for Technical Debt**: Key refactoring was performed to alleviate the technical debt, fostering a more maintainable and efficient codebase.
- **Linting Error Resolution**: Adherence to coding standards was reinforced by resolving all linting errors.
- **Admin Site Model Normalization**: Model names were normalized for pluralization consistency across the admin site.
- **Introduction of Modular Architecture**: The application was split into three separate Django apps—`lettings`, `profiles`, and `home`—each encapsulating specific functionalities.
- **Django Project Refactor**: `oc_lettings_site` was converted into a full-fledged Django project to enhance the organizational structure.
- **Comprehensive Testing Suite**: A new suite of tests was created to ensure the reliability and stability of code changes.

CI/CD Pipeline Implementation
-----------------------------

Automation of development processes has been achieved through a CI/CD pipeline, set up as follows:

- **Build and Test**: With every new commit, a suite of linting checks and tests is executed.
- **Docker Containerization**: Successful testing leads to the creation and pushing of a Docker image to DockerHub, this step being exclusive to the master branch.
- **Application Deployment**: The final step in the pipeline is an automated deployment to Render, contingent on the successful Docker image push.

Monitoring Solutions
--------------------

Application performance and error tracking are maintained vigilantly with the use of Sentry, ensuring high reliability and swift issue mitigation.

Installation Instructions
--------------------------

Prerequisites
^^^^^^^^^^^^^

- GitHub account with read access to this repository
- Git CLI
- SQLite3 CLI
- Python interpreter, version 3.6 or higher

Throughout the documentation for local development, it is assumed that the `python` command in your OS shell runs the above Python interpreter (unless a virtual environment is activated).

macOS / Linux
^^^^^^^^^^^^^

Clone the repository
~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

    cd /path/to/put/project/in
    git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git

Create the virtual environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

    cd /path/to/Python-OC-Lettings-FR
    python -m venv venv
    apt-get install python3-venv  # If the above step encounters errors with a package not found on Ubuntu
    source venv/bin/activate
    which python  # Confirm the `python` command runs the Python interpreter in the virtual environment
    python --version  # Confirm the Python interpreter version is 3.6 or higher
    which pip  # Confirm the `pip` command runs the pip executable in the virtual environment
    deactivate  # To deactivate the environment

Run the site
~~~~~~~~~~~~

.. code-block:: bash

    cd /path/to/Python-OC-Lettings-FR
    source venv/bin/activate
    pip install --requirement requirements.txt
    python manage.py runserver

Go to `http://localhost:8000` in a browser.
Confirm that the site works and can be navigated (you should see multiple profiles and listings).

Linting
~~~~~~~

.. code-block:: bash

    cd /path/to/Python-OC-Lettings-FR
    source venv/bin/activate
    flake8

Unit Tests
~~~~~~~~~~

.. code-block:: bash

    cd /path/to/Python-OC-Lettings-FR
    source venv/bin/activate
    pytest

Database
~~~~~~~~

.. code-block:: bash

    cd /path/to/Python-OC-Lettings-FR
    sqlite3  # Open a shell session
    .open oc-lettings-site.sqlite3  # Connect to the database
    .tables  # Display tables in the database
    pragma table_info(Python-OC-Lettings-FR_profile);  # Display columns in the profiles table
    select user_id, favorite_city from Python-OC-Lettings-FR_profile where favorite_city like 'B%';  # Query the profiles table
    .quit  # Quit the shell

Administration Panel
~~~~~~~~~~~~~~~~~~~~

Go to `http://localhost:8000/admin`.
Log in with the user `admin`, password `Abc1234!`.

Quick Start Guide

Technologies and Programming Languages

- **Programming Language**: Python 3.9
- **Web Framework**: Django 3.2
- **Version Control**: GitHub Actions
- **Containerization**: Docker (4.25.1)
- **Hosting Platform**: Render

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   Project Description
   Installation Instructions
   Quick Start Guide
   Technologies and Programming Languages
   Database Structure and Data Models
   API Interfaces
   Usage Guide with Use Cases
   Deployment and Application Management Procedures


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`