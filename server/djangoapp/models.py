from django.db import models

# CarMake Model
class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    # Optional: Add any additional fields you want
    # country = models.CharField(max_length=100, blank=True)
    # founded_year = models.IntegerField(null=True, blank=True)
    
    def __str__(self):
        return self.name


# CarModel Model
class CarModel(models.Model):
    # Choices for car type
    SEDAN = 'Sedan'
    SUV = 'SUV'
    WAGON = 'Wagon'
    HATCHBACK = 'Hatchback'
    COUPE = 'Coupe'
    CONVERTIBLE = 'Convertible'
    
    CAR_TYPE_CHOICES = [
        (SEDAN, 'Sedan'),
        (SUV, 'SUV'),
        (WAGON, 'Wagon'),
        (HATCHBACK, 'Hatchback'),
        (COUPE, 'Coupe'),
        (CONVERTIBLE, 'Convertible'),
    ]
    
    # Many-to-one relationship with CarMake
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    
    # Dealer ID from Cloudant database
    dealer_id = models.IntegerField()
    
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=20, choices=CAR_TYPE_CHOICES, default=SEDAN)
    year = models.IntegerField()
    
    # Optional: Add any additional fields
    # color = models.CharField(max_length=50, blank=True)
    # price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    
    def __str__(self):
        return f"{self.car_make.name} {self.name} ({self.year})"
