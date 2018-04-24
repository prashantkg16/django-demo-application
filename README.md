"# django-demo-application" 

This app contain simple CRUD operation with soft(Ajax) delete option(JQUERY)

"# Templates and Static data"
For Template and Static file setting, Please check the link:
http://prashantkumargupta.in/#/getdetails/3/Templates-and-Static-data

app Name - Devices

	Model(Table Name) 			- router
	
	Model(Table Name) Structure - 
		sapid = models.CharField(max_length=20, unique=True)    
		hostname = models.CharField(max_length=16, unique=True)
		loopback = models.CharField(max_length=16)
		macaddress = models.CharField(max_length=24)

In views.py: - list, add, edit/update and soft delete functionality.

For other setting, Please check repo