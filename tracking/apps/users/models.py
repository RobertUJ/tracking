#encoding:utf-8
from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.db.models.signals import post_save

states = (
        ('AK', 'Alaska'),
        ('AL', 'Alabama'),
        ('AR', 'Arkansas'),
        ('AS', 'American Samoa'),
        ('AZ', 'Arizona'),
        ('CA', 'California'),
        ('CO', 'Colorado'),
        ('CT', 'Connecticut'),
        ('DC', 'District of Columbia'),
        ('DE', 'Delaware'),
        ('FL', 'Florida'),
        ('GA', 'Georgia'),
        ('GU', 'Guam'),
        ('HI', 'Hawaii'),
        ('IA', 'Iowa'),
        ('ID', 'Idaho'),
        ('IL', 'Illinois'),
        ('IN', 'Indiana'),
        ('KS', 'Kansas'),
        ('KY', 'Kentucky'),
        ('LA', 'Louisiana'),
        ('MA', 'Massachusetts'),
        ('MD', 'Maryland'),
        ('ME', 'Maine'),
        ('MI', 'Michigan'),
        ('MN', 'Minnesota'),
        ('MO', 'Missouri'),
        ('MP', 'Northern Mariana Islands'),
        ('MS', 'Mississippi'),
        ('MT', 'Montana'),
        ('NA', 'National'),
        ('NC', 'North Carolina'),
        ('ND', 'North Dakota'),
        ('NE', 'Nebraska'),
        ('NH', 'New Hampshire'),
        ('NJ', 'New Jersey'),
        ('NM', 'New Mexico'),
        ('NV', 'Nevada'),
        ('NY', 'New York'),
        ('OH', 'Ohio'),
        ('OK', 'Oklahoma'),
        ('OR', 'Oregon'),
        ('PA', 'Pennsylvania'),
        ('PR', 'Puerto Rico'),
        ('RI', 'Rhode Island'),
        ('SC', 'South Carolina'),
        ('SD', 'South Dakota'),
        ('TN', 'Tennessee'),
        ('TX', 'Texas'),
        ('UT', 'Utah'),
        ('VA', 'Virginia'),
        ('VI', 'Virgin Islands'),
        ('VT', 'Vermont'),
        ('WA', 'Washington'),
        ('WI', 'Wisconsin'),
        ('WV', 'West Virginia'),
        ('WY', 'Wyoming')
)

# Create your models here.
class UserProfile(models.Model):
	user				= models.ForeignKey(User,unique = True)
	address				= models.CharField(null=True,blank=True,max_length=255)
	city				= models.CharField(max_length=150,verbose_name="City",null=True,blank=True)
	state 				= models.CharField(choices=states,max_length=150,verbose_name="State",null=True,blank=True)
	zip_code			= models.IntegerField(verbose_name="CP",null=True,blank=True)
	dtl_code 			= models.CharField(verbose_name="DTL Code",null=True,blank=True,max_length=100)
	phone 				= models.CharField(max_length=150,verbose_name="Phone",null=True,blank=True)
	mobile				= models.CharField(max_length=150,verbose_name="Mobile",null=True,blank=True)
	date_purchased		= models.DateField(verbose_name="Date membership purchased",null=True,blank=True,default='2000-01-01')
	license				= models.BooleanField(default=False)
	read_terms			= models.BooleanField(default=False)
	status_membership   = models.BooleanField(default=False)

	def __unicode__(self):
		_user = self.user
		if _user.first_name == "":
			return _user.username
		else:
			return "%s %s"%(_user.first_name,_user.last_name)

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
post_save.connect(create_user_profile, sender=User)



