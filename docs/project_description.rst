
Project Description
===================

Refactoring
-----------

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
