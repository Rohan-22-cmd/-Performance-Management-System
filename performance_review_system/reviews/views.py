from django import forms
from django.shortcuts import render, redirect
from .forms import PerformanceReviewForm
from .models import PerformanceReview
from django.contrib.auth.decorators import login_required
from .models import PerformanceReview, Department, Employee

from .models import Employee, PerformanceReview

def add_review(request):
    # Assuming you want to assign "rohan" as an example:
    # You need to get the Employee instance from the database
    try:
        employee = Employee.objects.get(name="rohan")  # Retrieve the Employee instance based on the name
    except Employee.DoesNotExist:
        employee = None  # Handle case where employee is not found

    # The rest of the logic where the employee instance is used:
    form = PerformanceReviewForm(initial={'employee': employee})

    if request.method == 'POST':
        form = PerformanceReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('review_list')

    return render(request, 'reviews/add_review.html', {'form': form})

from django.shortcuts import render
from .models import PerformanceReview

from django.shortcuts import render
from .models import PerformanceReview, Department, Employee
from django.db.models import Q  # For complex queries

from django.shortcuts import render
from .models import PerformanceReview, Department
from django.shortcuts import render
from .models import PerformanceReview, Department, Employee

def review_list(request):
    # Initialize query filters
    employee_name = request.GET.get('employee_name', '')
    department_id = request.GET.get('department', '')

    # Fetch all performance reviews
    reviews = PerformanceReview.objects.all()

    # Apply filter by employee name if specified
    if employee_name:
        reviews = reviews.filter(employee__name__icontains=employee_name)

    # Apply filter by department if specified
    if department_id:
        reviews = reviews.filter(employee__department_id=department_id)

    # Fetch all departments for the dropdown in the search form
    departments = Department.objects.all()
    
    # Fetch all employees for the employee dropdown
    employees = Employee.objects.all()

    # Calculate the statistics (number of reviews by period)
    monthly_reviews = reviews.filter(review_period=1).count()
    quarterly_reviews = reviews.filter(review_period=2).count()
    annually_reviews = reviews.filter(review_period=3).count()

    # Return the render with the context data
    return render(request, 'reviews/review_list.html', {
        'reviews': reviews,
        'departments': departments,
        'employees': employees,  # Pass the employees to the template
        'employee_name': employee_name,
        'department': department_id,
        'monthly_reviews': monthly_reviews,
        'quarterly_reviews': quarterly_reviews,
        'annually_reviews': annually_reviews,
    })


from django.shortcuts import render, get_object_or_404, redirect
from .forms import PerformanceReviewForm
from .models import PerformanceReview

def edit_review(request, id):
    review = get_object_or_404(PerformanceReview, id=id)
    if request.method == 'POST':
        form = PerformanceReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('review_list')  # Redirect to review list after saving
    else:
        form = PerformanceReviewForm(instance=review)
    return render(request, 'reviews/edit_review.html', {'form': form})
from django.shortcuts import redirect, get_object_or_404
from .models import PerformanceReview

def delete_review(request, id):
    review = get_object_or_404(PerformanceReview, id=id)
    review.delete()  # Delete the review
    return redirect('review_list')  # Redirect to review list after deletion
from django.shortcuts import render, get_object_or_404
from .models import PerformanceReview

def review_detail(request, id):
    # Retrieve the review object by its ID or show a 404 error if not found
    review = get_object_or_404(PerformanceReview, id=id)
    return render(request, 'reviews/review_detail.html', {'review': review})



