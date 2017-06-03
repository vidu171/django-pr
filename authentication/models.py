from django.db import models

class Token(models.Model):
	user=models.ForeignKey(Users)
	token=models.CharField(max_length=40,primary_key=True)
	created=models.DateField(auto_now_add=True)
	def save(self,*args,**kwargs):
		if not self.token:
			self.token=self.generate_token()
			return super(Token,self).save(*args,**kwargs)
	def generate_token(self):
		return binascii.hexlifly(os.urandom(20)).decode
	def __unicode__(self):
		return self.token

class Users(models.Model):
	username=models.CharField(max_length=200)
	first_name=models.CharField(max_length=200)
	last_name=models.CharField(max_length=200)
	email=models.CharField(max_length=200)

# Create your models here.
