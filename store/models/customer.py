from django.db import models


class Customer(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    mobile_no = models.CharField(max_length=15)
    email = models.EmailField()
    password = models.CharField(max_length=500)

    def register(self):
        self.save()
        
    def email_exists(self):
        if Customer.objects.filter(email=self.email):
            return True
        return False

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

    class Meta:
        db_table = 'Customer'
