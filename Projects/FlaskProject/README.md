# website

## templates folder
this is where we store the html files/code for each route and is referenced in the views. uses jinja as the templating language. without the need for javascript

the base file is typcically what the whole website looks like. all the detail and nuance is built off of this baseline html template. you'll override more specific parts of the base template with other templates.

## init.py
for initiating flask app

## views.py
where we store all the standard routes for our web and we'll refer to them in the main.py file

