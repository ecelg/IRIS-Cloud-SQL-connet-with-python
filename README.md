# IRIS-Cloud-SQL-connet-with-python
Upload a csv to IRIS Cloud SQL, testing the connection with pyodbc


Recently I heard that there is a InterSystems IRIS Cloud SQL on AWS for fast deployment purpose.
At the same time, I am learning the way to talk to IRIS platfrom by Python.
I started this simple project for fun ^^"


Deploy a 'IRIS SQL DB Cloud'
---------------------------------------------------------
Step 1. <br>
login to the InterSystems Cloud Service Portal
https://portal.staging.isccloud.io/deployments

Step 2. <br>
Created new deployment <br> <br>

Step 3. <br>
Go to Deployment > Overview > External Connections  to get the following infromation about the instant. <br>
    - Hostname <br>
    - Port <br>
    - Namespace <br>
    - Username <br>
    - Password  <br>
<br>
the above infromation is for the pyodbc connection <br> <br>

Step 4. <br>
Go to Deployment > SQL Query Tools   to create a table  <br>
```
CREATE TABLE Patient (PatientID int, Name varchar(255), Insurance varchar(255), PrimaryPhysician varchar(255),CreditRating varchar(255),HomePhone varchar(255),HomeAdd_City varchar(255),HomeAdd_State varchar(255),HomeAdd_Zip varchar(255))
```
the above table is created for the .csv upload in the next Step.  
<br> <br>

Step 5. <br>
<br>
Go to Deployment > Import Files  to upload the .csv file <br>
<br><br>

Step 6. <br>
Go to Deployment > SQL Query Tools   to check the upload <br>
```
select * from Patient
```
<br><br>

Setup the 'pyodbc'
---------------------------------------------------------
Step 1. <br>
Go to  https://intersystems-community.github.io/iris-driver-distribution/ <br>
Click the "DB-API" to get the wheel file "intersystems_irispython-3.2.0-py3-none-any.whl"
.. you may also click th "ODBC Win" to get the odbc driver for the PowerBI use.
<br><br>

Step 2. <br>
Open the cmd of you windows, go to the download directory of wheel file "intersystems_irispython-3.2.0-py3-none-any.whl" <br>
run the following command <br>
```
py -m pip install pyodbc
py -m pip install intersystems_irispython-3.2.0-py3-none-any.whl
```
<br><br>
------------------------------------------------------------

Open your Python IDE and you may start here  (I think.....)<br>
I amd using Python3.9 today (21st June, 2022)<br>
Because seems Python3.10 is not support by irisnative yesterday (20th June, 2022)<br>
<br><br>

Some Non related link (for my ref only)
----------------------------------------------------------
https://docs.intersystems.com/irislatest/csp/docbook/DocBook.UI.Page.cls?KEY=AB_idesetup#AB_idesetup_python <br>
https://docs.intersystems.com/iris20221/csp/docbook/Doc.View.cls?KEY=PAGE_python_native <br>
https://docs.intersystems.com/components/csp/docbook/Python-Native/v1.0.0/index.html <--- this one is somehow.... <br>
https://docs.intersystems.com/components/csp/docbook/DocBook.UI.Page.cls?KEY=ADRIVE <--- this one may not uptodate... <br>
https://intersystems-community.github.io/iris-driver-distribution/ <-- useful somehow <br>
https://community.intersystems.com/post/iris-native-api-python <-- inspiring, will go through soon <br>
https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-and-highlighting-code-blocks <-- very useful but I am toooooooo lazy to go through <br>
https://github.com/iijimam/selflearning-python-old/blob/master/src/python-pyODBC/HelloWorldPyODBC.py <-- simple but very helpful <br>
