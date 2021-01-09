from django.db import models

class Transactions(models.Model):
      date_of_pull = models.DateTimeField(db_column='Date of pull', blank=True, null=True)  # Field name made lowercase. Field renamed to r    emove unsuitable characters.
      unique_mail_id = models.CharField(db_column='Unique mail id', primary_key=True, max_length=50)  # Field name made lowercase. Field re    named to remove unsuitable characters.
      reciept_text = models.CharField(db_column='Reciept text', max_length=250, blank=True, null=True)  # Field name made lowercase. Field     renamed to remove unsuitable characters.
      date = models.DateField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
      amount = models.FloatField(db_column='Amount', blank=True, null=True)  # Field name made lowercase.
      time_est = models.TimeField(db_column='Time EST', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuit    able characters.
  
      class Meta:
          managed = False
          db_table = 'Transactions'
