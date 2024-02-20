Database structure
==================

The database structure consists of four tables: User, Profile, Address, and Letting.

- The User table stores user information such as id, username, email, first name, and last name.
- The Profile table is linked to the User table and includes the user's favorite city.
- The Address table contains details about addresses, including number, street, city, state, zip code, and country ISO code.
- The Letting table stores letting information with a title and a reference to an address from the Address table.

.. image:: /_static/database_structure.png