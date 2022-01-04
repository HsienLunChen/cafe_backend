# NextCafe Backend
This is the source code of the backend part of project NextCafe,  a mobile website for Taipei coffee shops searching. This website allows user to search the desired coffee shop by location and specific information (WIFI, atmosphere...)
## Introduction
By selecting the district or mrt station, this application will search the nearby coffee shops from our database. The user can also select specific filters, including WIFI, quietness, and open time, to find the desired coffee shops. This application also integrates the Google Place Api, so user can find the direction to the desired coffee shop if needed.
\
![](search_coffee.gif)
## Backend
The Backend is built with Node.js to handle the HTTP request from the client side. This part of server side code talks with the SQLite database and perform queries with parameters given by the client side, including location and atmosphere filter, to find the corresponding coffee shops and their information.
## Database
The database is expanded from the opensource Taipei coffee shop database, the cafe nomad database. Python scripts were implemented to connect this existing database with the google place api to update the deprecated information about the coffee shops.