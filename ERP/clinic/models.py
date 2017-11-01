from django.db import models

class Brand(models.Model):
	brand_id = models.CharField(max_length=8,default=None)
	brand_name = models.CharField(max_length=32,default=None)
	brand_address = models.CharField(max_length=300,default=None)
	brand_phone_number = models.CharField(max_length=11,default=None)
	brand_manager_id  = models.IntegerField()
	def __str__(self):
		return self.brandName
class User(models.Model):
	brand_id = models.CharField(max_length=8,default=None)
	user_id = models.CharField(max_length=8,default=None)
	user_login_id = models.CharField(max_length=8,default=None)
	user_password = models.CharField(max_length=32,default=None)
	user_role = models.CharField(max_length=100,default=None)
	user_name = models.CharField(max_length=300,default=None)
	user_dob = models.CharField(max_length=10,default=None)
	user_phone_number = models.CharField(max_length=11,default=None)
	user_address = models.TextField(default=None)
	user_specialize = models.CharField(max_length=200,default=None)
	def __str__(self):
		return self.name
# class Customer(models.Model):
# 	brand_id = models.CharField(max_length=8,default=None)
# 	customer_id = models.CharField(max_length=8,default=None)
# 	customer_name = models.CharField(max_length=32,default=None)
# 	sex = models.CharField(max_length=32,default=None)
# 	dob = models.DateTimeField(default=None)
# 	job = models.TextField(max_length=500,default=None)
# 	company = models.TextField(max_length=500,default=None)
# 	phone_number = models.CharField(max_length=11,default=None)
# 	email = models.TextField(max_length=200,default=None)
# 	address = models.TextField(max_length=500,default=None)
# 	source = models.TextField(max_length=500,default=None)
# 	fingerprint = models.TextField(max_length=500,default=None)
# 	medical_biography = models.TextField(max_length=500,default=None)#sẽ bỏ cái này
# 	def __str__(self):
# 		return self.customer_name
# class MedicalHistory(models.Model):
# 	# medicalhis_id = models.CharField(max_length=8,default=None) 
# 	brand_id = models.CharField(max_length=8,default=None)
# 	customer_id = models.CharField(max_length=8,default=None)
# 	medicalhis_type = models.CharField(max_length=2,default=None)
# 	medicalhis_name = models.CharField(max_length=500,default=None)
# 	medicalhis_status = models.CharField(max_length=500,default=None)
# 	medicalhis_detail = models.CharField(max_length=500,default=None)
# 	create_date = models.CharField(max_length=10,default=None)
# 	create_by = models.CharField(max_length=10,default=None)
# 	update_date = models.CharField(max_length=10,default=None)
# 	update_by = models.CharField(max_length=10,default=None)
# 	delete_flag = models.CharField(max_length=1,default=None)

# class Relationship(models.Model): 
# 	customer_id1 = models.CharField(max_length=8,default=None)
# 	customer_id2 = models.CharField(max_length=8,default=None)
# 	relationship = models.CharField(max_length=32,default=None)
# class CalendarDentist(models.Model):  
# 	brand_id =  models.CharField(max_length=8,default=None)
# 	user_id = models.CharField(max_length=8,default=None)
# 	time = models.DateTimeField(default=None)

# class CalendarAppointment(models.Model):  
# 	brand_id = models.CharField(max_length=8,default=None)
# 	user_id =  models.CharField(max_length=8,default=None)
# 	customer_id =  models.CharField(max_length=8,default=None)
# 	treatment_id = models.CharField(max_length=8,default=None)
# 	appointment_id = models.CharField(max_length=8,null=True)
# 	date_appointment = models.CharField(max_length=10,default=None)
# 	time_appointment = models.TextField(max_length=5,default=None)
# 	appointment_name = models.TextField(max_length=500,null=True)
# 	content = models.TextField(max_length=500,default=None)
# 	assign_id = models.CharField(max_length=8,default=None)
# 	estimated_time = models.CharField(max_length=8,default=None)
# 	estimated_difficulty = models.IntegerField(default=None)
# 	status = models.TextField(max_length=10,default=None)
# 	note = models.TextField(max_length=500,default=None)
# 	create_date = models.CharField(max_length=10,default=None)
# 	create_by = models.CharField(max_length=8,default=None)
# 	update_date = models.CharField(max_length=10,default=None)
# 	update_by = models.CharField(max_length=8,default=None)
# 	delete_flag = models.CharField(max_length=1,default=None)
# 	def __str__(self):
# 		return self.userID
# class Treatment(models.Model):
# 	brand_id = models.CharField(max_length=8,default=None)
# 	user_id = models.CharField(max_length=8,default=None)
# 	customer_id = models.CharField(max_length=8,default=None)
# 	treatment_id = models.CharField(max_length=8,default=None)
# 	describe = models.TextField(max_length=500,default=None)
# 	total_payment =  models.IntegerField(default=None)
# 	payment_status = models.IntegerField(default=None)
# 	treatment_status = models.TextField(max_length=10,default=None)
# 	create_date = models.CharField(max_length=10,default=None)
# 	create_by = models.CharField(max_length=8,default=None)
# 	update_date = models.CharField(max_length=10,default=None)
# 	update_by = models.CharField(max_length=8,default=None)
# 	delete_flag = models.CharField(max_length=1,default=None)

# class TreatmentDetail(models.Model):
# 	treatment_id = models.CharField(max_length=8,default=None)
# 	treatment_detail_id = models.CharField(max_length=8,default=None)
# 	time = models.DateTimeField(default=None)
# 	content = models.TextField(max_length=500,default=None)
# 	price  = models.IntegerField(default=None)

# class Invoice(models.Model):
# 	brand_id = models.CharField(max_length=8,default=None)
# 	user_id = models.CharField(max_length=8,default=None)
# 	customer_id = models.CharField(max_length=8,default=None)
# 	treatment_id = models.CharField(max_length=8,default=None)
# 	invoice_id = models.CharField(max_length=8,default=None)
# 	pay = models.IntegerField(default=None)

# class Inventory(models.Model):
# 	brand_id = models.CharField(max_length=8,default=None)
# 	item_id = models.CharField(max_length=8,default=None)
# 	item_name = models.IntegerField(default=None)
# 	unit = models.CharField(max_length=32,default=None)
# 	quantity = models.IntegerField(default=None)

# class Labo(models.Model):   
# 	brand_id = models.CharField(max_length=8,default=None)
# 	labo_name = models.CharField(max_length=100,default=None)
# 	address =  models.TextField(max_length=500,default=None)
# 	phone_number =  models.CharField(max_length=11,default=None)

# class TreatmentDetailLabo   (models.Model):
# 	labo_id = models.CharField(max_length=8,default=None)
# 	treatment_id = models.CharField(max_length=8,default=None)
# 	send_day = models.DateTimeField(default=None)
# 	received_day = models.DateTimeField(default=None)
# 	price = models.IntegerField(default=None)


