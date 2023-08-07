from django.db import models
from django.utils.timezone import now
import datetime

# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description
# - Any other fields you would like to include in car make model
class CarMake(models.Model):
    make_name = models.CharField(null=False, max_length=500, default="")
    make_description = models.CharField(null=False, max_length=500, default="")
# - __str__ method to print a car make object
    def __str__(self):
        return self.make_name + "\n" + self.make_description

# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many Car Models, using ForeignKey field)
# - Name
# - Dealer id, used to refer a dealer created in cloudant database
# - Type (CharField with a choices argument to provide limited choices such as Sedan, SUV, WAGON, etc.)
# - Year (DateField)
# - Any other fields you would like to include in car model
class CarModel(models.Model):
    SEDAN = "Sedan"
    SUV = "SUV"
    WAGON = "Wagon"

    CARS_TYPES = [
        (SEDAN, "Sedan"),
        (SUV, "SUV"),
        (WAGON, "Wagon"),
    ]

    YEAR_CHOICES = []
    for r in range(1969, (datetime.datetime.now().year+1)):
        YEAR_CHOICES.append((r, r))

    car_make = models.ForeignKey(CarMake, null=True, on_delete=models.CASCADE)
    car_name = models.CharField(max_length=500, default="")
    id = models.IntegerField(default=1, primary_key=True)
    car_model = models.CharField(max_length=200, choices=CARS_TYPES, default=SEDAN)
    car_year = models.IntegerField(('year'), choices=YEAR_CHOICES, default=datetime.datetime.now().year)
# - __str__ method to print a car make object
    def __str__(self):
        return self.car_name + ", " + self.car_model + ", " + str(self.car_year)

class CarDealer:

    def __init__(self, address, city, full_name, id, lat, long, short_name, st, zip):
        # Dealer address
        self.address = address
        # Dealer city
        self.city = city
        # Dealer Full Name
        self.full_name = full_name
        # Dealer id
        self.id = id
        # Location lat
        self.lat = lat
        # Location long
        self.long = long
        # Dealer short name
        self.short_name = short_name
        # Dealer state
        self.st = st
        # Dealer zip
        self.zip = zip

    def __str__(self):
        return "Dealer name: " + self.full_name

# <HINT> Create a plain Python class `DealerReview` to hold review data
class DealerReview:
    def __init__(self, dealership, name, purchase, review):
        self.dealership=dealership
        self.name=name
        self.purchase=purchase
        self.review=review
        self.purchase_date=""
        self.car_make=""
        self.car_model=""
        self.car_year=""
        self.sentiment="" 
        self.id=""

    def __str__(self):
        return "Review: " + self.review

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                            sort_keys=True, indent=4)
