import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','fbvproject.settings')
import django
django.setup()

from testapp.models import Employee
from faker import Faker
from random import *
fake = Faker()
def populate(n):
    for i in range(n):
        feno = fake.random_int(1001,9999)
        fename = fake.name()
        fesal = fake.random_int(10000,20000)
        feaddr = fake.city()
        emp_record = Employee.objects.get_or_create(eno = feno,ename = fename,esal = fesal,eaddr = feaddr)

n = int(input("Enter number of Records :"))
populate(n)
print(f'{n} Records inserted successfully')
