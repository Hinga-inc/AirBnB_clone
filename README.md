# AirBnB clone

## Overview

this is a project that invloves:

- A command inteerpreter to manipulate data without a visual inerface
- A website(front end) a static and dynamic website that shows the final product on the browser
- A database(backend) file storin the data
- An API that provides communication with te front-end and the back-end

## Steps

It is a step by step build of:

- The console
  - Create a data model
  - Manage objects via a console
  - Store and persist obl=jects to a file(JSON file)
  - Manipulatin a powerful storage system that will give us an abstaction between "my object"
  and "how they are stored and persisted"<br>
  This abstaction will also allow one to change the type of storage easily without updating all of your codebase<br>
  The console will be a tool to validate this storage engine<br>

- The static web
  - Learn HTML/CSS
  - Create the html of the application
  - Create a template of each object

- The MySQL storage
  - Replace the files storage by a Database storage
  - Map the models to a table in a database using an O.R.M.

- Web framework templating
  - Create a web server in python
  - Make a static html file dynamic by using objects stored in a file/database

- The RESTful API
  - Expose all objects stores via a JSON web interface
  - Manipulate objects via a RESTful API

- The dynamic web
  - Learn JQuery
  - Load objects from the client side by using my own RESTful API

## Files and Directories

- ```models```
  - this directory contains all classes used for the entire project(representation of n object/instance)
  - ```base_models.py```
    - the base class of all our models
    - containing common elements:
    - attributes: ```id```, ```create_at``` and ```update_at```
    - methods: ```save()``` and ```to_json()```
  - ```engine```
    - contails all storage class(using the same prototype). For the moment ypu will have only one ```file_storage.py```
- ```tests```
  - this will contain all unit tests
- ```console.py```
  - this is a file that will be our entry point to the command interpreter

### Storage

- Persistency is really important for a web app. this means that everytime a program is executes it starts with all objects previously created from another execution without persistency, all the work done in a previous execution won't be saved and will be gone<br>
- in this project, I manipulated 2 types of storage: file and database(focus on file)
- why separate "storage management" from "model"? >> to make the models modular and independent, With this architecture you can easily replace your storage system without recoding everything everywhere
- one will always use class attributes for any object, Why not instance attributes? for 3 reasons:
  - provide easy class description: everbody will be able to see what a model should contain
  - provide default values of any attributes
  - in the future it will provide the same model behaviour for file storage or database storage

### How one can store an Instance

``` py
    class Student():
        def __init__(self, name):
            self.name = name

    students = []
    s = Student("John")
    students.append(s)
```

here, you are creating a student and store it in a list. But after the program execution my Student instance doesn't exist anymore<br>

``` py
    class Student():
        def __init__(self, name):
            self.name = name

    students = reload() # recreate the list of students objects from a file
    s = Student("John")
    students.append(s)
    save(students) # save all Student objects to a file

```

How it works?<br>

- ``` save(students) ```:

  - can one write each ```Student``` object to a file => NO it will be the momory representation of the object. For<br another program execution, this memory representation can't be reloaded.
  - can one write each ```Student.name``` to a file => YES, but imagine you have other attributes to desribe ```Students``` it would start to become too complex
  - the best silution is to convert this list of ```Students``` objects and saves the




##### AUTHORS
HINGA PETER <hingapeter18@gmail.com>