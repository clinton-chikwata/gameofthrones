Structure of the Web app
-#-template folder --contains html code responsible for rendering content to the website in this case our table 
-#-static folder     --contains our css files for styling our html tags 
-#-app.py    This  python file is responsible for handling our the functionality needed for web page to run that include import libraries and reading from csv files and parsing that data to the views for rendering
-#-Two csv files we are reading data from 
-#-Library --containes all the special libraries we need for our web app to run

1)Used Framework

#Flask 
 is a lightweight webframework that  is used handle python  code in an efficient way when building web applications.
 Flask supports extensions that can add application features as if they were implemented in Flask itself  as you would observe in my code.

2)Thrd Party Libraries

#Tablib
 is a tabular dataset library, written in Python. It allows you to import, export, and manipulate tabular data sets.
 Advanced features include, segregation, dynamic columns, tags & filtering, and seamless format import & export.
I need to render csv files in tabular format  hence I used this Libarary

3)Configuring Port Number to 8080

As I am using PyCharm IDE (Intergrated Development Environment) it contains port tweak file  in its configuration  files ,thats where I set port number to 8080: 
and added a syntax line --> port = 80

4)Steps In Installation of Libraries such as tablib and pandas

*If using command prompt
Go to your root directory of your project and type pip installs "name of the library"

*When installing through an IDE such as PyCharm
Click on file go to settings-->project interpreter-->click add-->search for library-->click install.


