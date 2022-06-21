# IRIS-Cloud-SQL-connet-with-python
Upload a csv to IRIS Cloud SQL, testing the connection with pyodbc


Recently I heard that there is a InterSystems IRIS Cloud SQL on AWS for fast deployment purpose.
At the same time, I am learning the way to talk to IRIS platfrom by Python.
I started this simple project for fun ^^"

​
Deploy a 'IRIS SQL DB Cloud'
---------------------------------------------------------
​Step 1. <br>
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
** the above infromation is for the pyodbc connection <br> <br>

Step 4. <br>
Go to Deployment > SQL Query Tools   to create a table  <br>
    CREATE TABLE Patient (PatientID int, Name varchar(255), Insurance varchar(255), PrimaryPhysician varchar(255),CreditRating varchar(255),HomePhone varchar(255),HomeAdd_City varchar(255),HomeAdd_State varchar(255),HomeAdd_Zip varchar(255))
 <br> <br>
** the above table is created for the .csv upload in the next Step.  <br> <br>

Step 5. <br>
Go to Deployment > Import Files  to upload the .csv file <br>
 <br> <br>
Step 6. <br>
Go to Deployment > SQL Query Tools   to check the upload <br>
    select * from Patient <br>
 <br>
------------------------------------------------------------- 
<br> <br>



