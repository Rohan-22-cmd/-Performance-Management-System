from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    manager = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='subordinates')
    
    def __str__(self):
        return self.name

class PerformanceReview(models.Model):
    REVIEW_PERIOD_CHOICES = [
        ('Monthly', 'Monthly'),
        ('Quarterly', 'Quarterly'),
        ('Annual', 'Annual'),
    ]

    review_title = models.CharField(max_length=100)
    review_date = models.DateField()
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='reviews')
    reviewed_by = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True, related_name='reviews_conducted')
    review_period = models.CharField(max_length=100, choices=REVIEW_PERIOD_CHOICES)
    rating = models.IntegerField()
    comments = models.TextField(max_length=300, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Review for {self.employee.name} - {self.review_period}"
from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name
