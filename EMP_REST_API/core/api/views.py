from rest_framework.generics import ListAPIView, RetrieveAPIView, DestroyAPIView , UpdateAPIView, ListCreateAPIView
from core.models import Employee
from .serializers import EmployeeSerializer
from django.shortcuts import render,redirect 
from django.http import HttpResponse
from rest_framework.parsers import JSONParser
import requests
import urllib
import io
import json

class EmployeeListView(ListAPIView):
    #query to retrieve all the employee records from db
    queryset = Employee.objects.all() 
    serializer_class = EmployeeSerializer

    
def save_emp(request): 
    
    if request.method == "GET" and not request.COOKIES.get("api_token"): 
        
        #called a python library requests to fetch the content from the public web api provided
        r_obj=requests.get('http://dummy.restapiexample.com/api/v1/employees')
        
        # display the request object
        # print(r)
        
        #urllib module to open the url by accepting request object or the string as arguments and to read data from the specified url.
        json_string = urllib.request.urlopen(r_obj.url).read()
        # print(json_string)  
        
        # Rest comes with a JSON parser to parse the json data converted from bytes to json format.
        stream = io.BytesIO(json_string)
        data = JSONParser().parse(stream)
        # print("Parsed into native datatypes:",data)
        for index,each in enumerate(data,start=1):
            serialize_obj = EmployeeSerializer(data=each)
            if serialize_obj.is_valid():
                print("API record ",index,"saved")
                serialize_obj.save()
        print("Successfully saved data from Web API to the local db!!")
        response = HttpResponse(json_string,content_type="application/json")        
        response.set_cookie('api_token', '1234')
        return response
        
        
    else:
        # print("else block") # just to verify whether on the second hit of the api , will it print this
        return redirect("/api/v1/details")
              
#Retrieve a record
class EmployeeDetailView(RetrieveAPIView):
    #retrieveing all the Employee records from db
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

#Update the record
class EmployeeUpdateView(UpdateAPIView):
    #query to retrieve all the employee records from db
    queryset = Employee.objects.all() 
    serializer_class = EmployeeSerializer

#Delete the record
class EmployeeDeleteView(DestroyAPIView):
    #query to retrieve all the employee records from db
    queryset = Employee.objects.all() 
    serializer_class = EmployeeSerializer   


