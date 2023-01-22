from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound

import mysql.connector as mariadb


#from .models import customer
  
def index(request,id = 0):
    connection = mariadb.connect(user = 'user', password = '1234qweR', database = 'mysql', host = '127.0.0.1', port = '3306')
   
    print(id)
    if id==1:
        query = "SELECT * FROM products"
        d = []
        with connection.cursor() as cursor:
            cursor.execute(query)
            prod = cursor.fetchall()
            for row in prod:
                d.append(row)          
        connection.close()
        for row in d:
            print("<p>", row[0], ". ", row[1], " - ", row[2], "</p>")
        data = {"id": id, "prod" : d}
     #  data = {"prod": prod, "id": id}
      
        return render(request, "index.html", context=data)
    elif id==2:
        query = "SELECT * FROM customer"
        d = []
        with connection.cursor() as cursor:
            cursor.execute(query)
            prod = cursor.fetchall()
            for row in prod:
                d.append(row)
        connection.close()
        for row in d:
            print("<p>", row[0], ". ", row[1], " - ", row[2], "</p>")
        data = {"id": id, "cus" : d}
        return render(request, "index.html", context=data)
    else:
       print("last")
       return render(request, "index.html", { "id" : id})