from django import forms
from .models import Employee, PerformanceReview

from django import forms
from .models import PerformanceReview, Employee

class PerformanceReviewForm(forms.ModelForm):
    class Meta:
        model = PerformanceReview
        fields = ['employee', 'review_title', 'review_date', 'reviewed_by', 'review_period', 'rating', 'comments']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add subordinates dynamically to the employee dropdown field
        if 'subordinates' in kwargs:
            self.fields['employee'].queryset = kwargs['subordinates']
