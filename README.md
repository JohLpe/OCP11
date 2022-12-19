# OCP11


## Presentation

Pur Beurre is an application made for users to be able to find healthier alternatives for their favorite food!
Used data on this application has been pulled from the [OpenFoodFacts](https://fr.openfoodfacts.org/) database.

If a user chooses to create an account on the application, they will be able to add products in their "favorites".


## Installation


    > git clone https://github.com/JohLpe/OCP11.git

Install the virtual environment of your choice.

    > pip install -r requirements.txt

#### ENVIRONMENT VARIABLES

The settings.py file of the Django project includes different environment variables which need to be defined in a .env file

    - SECRET_KEY: which your personnal Django secret key
    - ALLOWED_HOSTS
    - DATABASES: NAME, USER, PASSWORD
    - dsn: which is the Sentry dsn key

