# Tracker
An application written in Django that track and trace shipments between sender and receiver

## Installation
#### Development
1. create a virtual environment and activate it (optional).
2. rename **.env-sample** to **.env** and fill in environments variables.
3. in the root level of the project run:
    ```bash
       docker-compose -f docker-compose.dev.yml up
    ```
4. change directory to **app** directory and run:
    ```bash
       python manage.py runserver
    ```
___

#### Production
1. rename **.env-sample** to **.env** and fill in environments variables.
2. in the root level of the project run:
    ```bash
       docker-compose -f docker-compose.yml up
    ```
