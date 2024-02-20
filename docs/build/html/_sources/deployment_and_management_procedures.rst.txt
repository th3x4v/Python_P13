Deployment and management procedures
====================================

This Django application leverages Docker, GitHub Actions, and Render for automated deployment and streamlined management.

Continuous Integration and Deployment (CI/CD)
A dedicated GitHub Actions workflow (django.yml) ensures a robust CI/CD pipeline. Every push triggers the following steps:

- **Enviroment variables**:
Setup environment variables in Render

.. image:: /_static/env_variables.png
    :align: center

- **Unit Testing**: The pipeline executes comprehensive unit tests using pytest to verify code functionality and identify potential issues early in the development cycle.
- **Code Linting**: Static code analysis with flake8 enforces code style consistency and catches potential readability or maintainability problems.
- **Docker Image Build and Push**: Upon successful test and linting, the workflow builds and pushes a Docker image containing the application to the Render platform. This containerized approach ensures consistent and portable deployment across different environments.
- **Deployment Target (only for master branch)**: Render
Render serves as the chosen hosting platform, providing a fully managed infrastructure for seamless deployment and scaling. The generated Docker image from the GitHub Actions workflow gets automatically deployed to Render, ensuring a smooth transition from development to production.

- **Additional Notes**
For local development, refer to the Installation Instructions paragraph for instructions on setting up a virtual environment and running the application.
The specific configuration and deployment settings are documented within the settings.py file and the django.yml workflow.
