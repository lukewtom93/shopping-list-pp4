# Shopping List

This is a simple shopping list app hosted on Heroku.

Using CRUD views to create a intuative user experience.

![Mockup](static/images/shopping-list-main.png)

[The live version can be found here](https://shopping-list-1951df8955b3.herokuapp.com/)

## About

Users can create an account and add items delete items and cross out items already purchased.

## Features

### Existing Features

-__Register User__

![Register page](static/images/register-form.png)

-__Login__

![login page](static/images/register-form.png)

-__Create Item__

![Create item](static/images/add-item.png)

-__Delete Item__

![Delete item](static/images/delete-item.png)

-__Cross Off Item__

![Crossed off item](static/images/item-list-complete-example.png)

### Future Features

-__Add multiple lists__

-__Add Prices__

## Technologies Used

-__Backend__: Django

-__Frontend__: HTML, CSS, Javascript

-__Database__: SQlite, PostgreSQL

## Testing

- using google chrome lighthouse 
![lighthouse](static/images/lighthouse-performance.png)

### Validator Testing

- HTML
  - No errors were returned when passing through the official W3C HTML Validator
- CSS
  - No errors were found when passing through the official W3C CSS Validator (Jigsaw)
- Python
  - Passed the code through the PEP8 linter and confirmed there are no problems
- Javascript
  - JShint was used to validate JS code for the website.

### Automated Tests

- Testing for the register page is run with python3 manage.py test

### Deployment

- Steps for deployment

    - Fork or clone this repository

    - Create a new Heroku app

    - Link the Heroku app to the repository

    - Set Debug to FALSE

    - Click on __Deploy__

### Credits

- Dennis Ivy's article on class based views found [here](https://dennisivy.com/django-class-based-views)

- for auth views and generic views I used the resources found on [ccbv.co.uk](https://ccbv.co.uk/)