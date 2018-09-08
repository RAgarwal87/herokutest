from django.db import models

# Create your models here.
class CUSTOMER(models.Model):
    CustomerId = models.AutoField(db_column='CustomerId', primary_key=True)  # Field name made lowercase.
    CustomerName = models.CharField(db_column='CustomerName', max_length=100, blank=True,null=True)  # Field name made lowercase.
    Address = models.CharField(db_column='Address', max_length=200, blank=True, null=True)  # Field name made lowercase.
    City = models.CharField(db_column='City', max_length=50, blank=True, null=True)  # Field name made lowercase.
    PostalCode = models.CharField(db_column='PostalCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    Country = models.CharField(db_column='Country', max_length=50, blank=True, null=True)  # Field name made lowercase.
    TelephoneNo = models.CharField(db_column='TelephoneNo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    IsDeleted = models.CharField(db_column='IsDeleted', max_length=50, blank=True, null=True)  # Field name made lowercase.
    CREAT_TS = models.DateTimeField(db_column='CREAT_TS', blank=True, null=True)  # Field name made lowercase.
    UPD_TS = models.DateTimeField(db_column='UPD_TS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table= 'CUSTOMER'