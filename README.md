# Integrate a Public Web API into your DJANGO_REST_API
---
*note: please note the following application executes on ubuntu 18.04 with Python3 installed. make sure you have virtualenv and pip3 installed on your system.*

The following repository describes the integration of public web API into your Django REST API and its  CRUD operations.

+ Given a public Web API's , the data fetched from public web API's can be integrated into the Django rest api the one that you have created.

+ Steps to be followed:
    - 
    - Create a virtual environment: If you are working on different projects with different requirements, then create an isolated environment for your project where you can install the packages that you need to make your application run.
      create a virtual environment by following command:   
          `virtualenv -p python3 .`
      
      note : make sure you are in a virtualenv directory . you can also check by `pwd` command to check your current working directory.
    
    - Post successful creation of virtual environment, activate the virtual environment by:
           `source ./bin/activate`
           
     - Install the dependencies by following command:
            `pip3 install -r requirements.txt`
            
     - Running the Application
         
         + Before executing the application, we need to create the Database tables.(note: make sure you are at manage.py level)
                `python manage.py migrate`
         
         + Now you can run the development server by:
                 `python manage.py runserver`
         
         + To access the applications go to the URL http://localhost:8000/
         
         

