import pyodbc

connection=pyodbc.connect("DRIVER={InterSystems IRIS ODBC35};SERVER=k8s-64ea0e19-a8475938-131e349afd-7309e19823b7b6b4.elb.us-east-1.amazonaws.com;PORT=1972;DATABASE=USER;UID=SQLAdmin;PWD=!2021Ischk")
print("connected to IRIS SQLCloud")
cursor=connection.cursor()
z="select * from patient where PatientID between ? and ?"
y=cursor.execute(z,3,8)
for i in y: print(i)
connection.close
print("connection closed")
