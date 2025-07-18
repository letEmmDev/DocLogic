from django.shortcuts import render
from django.conf import settings
import uuid
import boto3

# Create your views here.

from .models import Doctor, Department

def contact_form(request):
    if request.method == 'POST':
        email = request.POST.get('username')
        message = request.POST.get('message')
        # Connect to DynamoDB
        dynamodb = boto3.resource(
            'dynamodb',
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
            region_name=settings.AWS_REGION
        )
        table = dynamodb.Table('ContactMessages')
        # Put item
        table.put_item(Item={
            'message_id': str(uuid.uuid4()),
            'email': email,
            'message': message,
        })
        return render(request, 'hospital/contact_form.html', {'success': True})
    return render(request, 'hospital/contact_form.html')

def doctor_list(request):
    department_name = request.GET.get('department')
    if department_name and department_name != 'all':
        doctors = Doctor.objects.filter(department__name__iexact=department_name)
    else:
        doctors = Doctor.objects.all()
    departments = Department.objects.all()
    return render(request, "hospital/doctor_cards.html", {
        "doctors": doctors,
        "departments": departments,
        "selected_department": department_name or "all"
    })