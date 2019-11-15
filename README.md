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
      
      note : make sure you are in a virtualenv directory . you can also check by `pwd` command to check your current working       directory.
    
    - Post successful creation of virtual environment, activate the virtual environment by:
           `source ./bin/activate`
           
     - Install the dependencies by following command:
            `pip3 install -r requirements.txt`
            
     - Running the Application
         
         + Before executing the application, we need to create the Database tables.(note: make sure you are at manage.py level). But here I have already created the database tables, so you can skip this step. But if making any changes in models file, then you need to run this step by:
         
                `python manage.py makemigrations`
                `python manage.py migrate`
         
         + Now you can run the development server by:
                 `python manage.py runserver`
         
         + To access the applications go to the URL http://localhost:8000/
                  
         + few things to remember : Post running the application at localhost, you will see the error page which also                    mentions the urls to hit . Following are the urls to hit and perform CRUD operations on the same:
         
             - `localhost:8000/api/v1/` : Hit this url to fetch the records from the public web api as mentioned by me                        in the code. When you hit for the first time, it will fetch the records from the public web API and                          store it in your local database. 
             
                 The first snapshot is the terminal log which displays the successful fetch record statement of the web api                    into your localhost database. `note: it will take some time if the public api has huge amount of records.`
                 
                 ![api2](https://user-images.githubusercontent.com/21193492/68829285-5b1edb80-06ce-11ea-8a92-98df413c5e09.png)
                 
                 The second snapshot displays the json records post completion of the above data storing process:
                 
                  ![api1](https://user-images.githubusercontent.com/21193492/68829284-5b1edb80-06ce-11ea-9a99-d914555a1593.png)
                  
                    
             - `localhost:8000/api/v1/details`: when you again hit the same url `localhost:8000/api/v1` again, it will fetch                 the records from your local database instead of fetching from public web API (which is time consuming) since                 the same records already being stored in your local database. This url will display all the employee details                 fetched.
             
                 The third snapshot displays the LISTVIEW of the API when you hit the same url `localhost:8000/api/v1` for the second time: This will fetch directly from local db.
                  
                 ![api3](https://user-images.githubusercontent.com/21193492/68829286-5b1edb80-06ce-11ea-800b-b1e5cb3f4717.png)
                  
             
             - `localhost:8000/api/v1/employee/1`: If you want to fetch a single employee record , then you need to hit this                 url which will basically retrieve from your local database.
             
                The fourth snapshot displays retrieval of the single record.
                ![api4](https://user-images.githubusercontent.com/21193492/68829287-5bb77200-06ce-11ea-894d-8dc16bc5f05f.png)
               `note: Before proceeding with update and delete, you should create a superuser (eg: admin) so that you can                                 perform the update, delete operations with superuser privileges by following command:`
                      `python manage.py createsuperuser`
                      
                      here u need to mention the username, password and email id(optional).
                      
            - `localhost:8000/api/v1/employee/<pk>/update` : If you want to update the specific record , then u need                         to specify the id (<pk>). following is the snapshot for the same.
    
                ![api5](https://user-images.githubusercontent.com/21193492/68892669-8397eb80-0749-11ea-8834-593508e7c2ea.png)
            
            - `localhost:8000/api/v1/employee/delete` : If you want to delete the specific record , then u need to specify                  the id(which is basically a primary key).

                ![api6](https://user-images.githubusercontent.com/21193492/68892677-87c40900-0749-11ea-920a-ae3056fe84ac.png)

             
         

