from core.models import CustomUser
from hospital.models import Department, Specialization, Doctor
from django.db import IntegrityError
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Realistic department data
departments_data = [
    {'name': 'Cardiology', 'description': 'Specialized care for heart and cardiovascular conditions.'},
    {'name': 'Pediatrics', 'description': 'Comprehensive healthcare for infants, children, and adolescents.'},
    {'name': 'Oncology', 'description': 'Advanced cancer treatment and supportive care services.'},
    {'name': 'Maternity', 'description': 'Complete maternity and neonatal care for mothers and newborns.'},
    {'name': 'Neurology', 'description': 'Diagnosis and treatment of disorders of the nervous system.'},
]

# Realistic specialization data
specializations_data = [
    {'name': 'Cardiologist', 'description': 'Expert in heart and blood vessel conditions.'},
    {'name': 'Pediatrician', 'description': 'Specialist in medical care for children.'},
    {'name': 'Oncologist', 'description': 'Specialist in cancer diagnosis and treatment.'},
    {'name': 'Obstetrician', 'description': 'Expert in pregnancy, childbirth, and postpartum care.'},
    {'name': 'Neurologist', 'description': 'Specialist in disorders of the brain and nerves.'},
    {'name': 'Radiologist', 'description': 'Expert in medical imaging techniques.'},
    {'name': 'Dermatologist', 'description': 'Specialist in skin, hair, and nail conditions.'},
    {'name': 'Orthopedist', 'description': 'Expert in musculoskeletal system.'},
    {'name': 'Psychiatrist', 'description': 'Specialist in mental health disorders.'},
    {'name': 'General Practitioner', 'description': 'Primary care provider for general health.'},
]

# Realistic doctor data
doctors_data = [
    {'email': 'jane.smith@hospital.com', 'name': 'Jane', 'surname': 'Smith', 'department': 'Cardiology', 'specialization': 'Cardiologist'},
    {'email': 'michael.chen@hospital.com', 'name': 'Michael', 'surname': 'Chen', 'department': 'Pediatrics', 'specialization': 'Pediatrician'},
    {'email': 'emily.jones@hospital.com', 'name': 'Emily', 'surname': 'Jones', 'department': 'Oncology', 'specialization': 'Oncologist'},
    {'email': 'david.wilson@hospital.com', 'name': 'David', 'surname': 'Wilson', 'department': 'Maternity', 'specialization': 'Obstetrician'},
    {'email': 'sarah.brown@hospital.com', 'name': 'Sarah', 'surname': 'Brown', 'department': 'Neurology', 'specialization': 'Neurologist'},
    {'email': 'robert.taylor@hospital.com', 'name': 'Robert', 'surname': 'Taylor', 'department': 'Cardiology', 'specialization': 'Radiologist'},
    {'email': 'laura.martin@hospital.com', 'name': 'Laura', 'surname': 'Martin', 'department': 'Pediatrics', 'specialization': 'Dermatologist'},
    {'email': 'james.white@hospital.com', 'name': 'James', 'surname': 'White', 'department': 'Oncology', 'specialization': 'Orthopedist'},
    {'email': 'amanda.lee@hospital.com', 'name': 'Amanda', 'surname': 'Lee', 'department': 'Maternity', 'specialization': 'Psychiatrist'},
    {'email': 'thomas.moore@hospital.com', 'name': 'Thomas', 'surname': 'Moore', 'department': 'Neurology', 'specialization': 'General Practitioner'},
]

try:
    # Create or get departments
    departments = {}
    for dept_data in departments_data:
        dept, created = Department.objects.get_or_create(
            name=dept_data['name'],
            defaults={'description': dept_data['description']}
        )
        departments[dept_data['name']] = dept
        logger.info(f"{'Created' if created else 'Retrieved'} department: {dept_data['name']}")

    # Create or get specializations
    specializations = {}
    for spec_data in specializations_data:
        spec, created = Specialization.objects.get_or_create(
            name=spec_data['name'],
            defaults={'description': spec_data['description']}
        )
        specializations[spec_data['name']] = spec
        logger.info(f"{'Created' if created else 'Retrieved'} specialization: {spec_data['name']}")

    # Create users and doctors
    for doc_data in doctors_data:
        try:
            # Check if user already exists
            if CustomUser.objects.filter(email=doc_data['email']).exists():
                logger.warning(f"User with email {doc_data['email']} already exists, skipping.")
                continue

            # Create user
            user = CustomUser.objects.create_user(
                email=doc_data['email'],
                password='SecurePass2025!',
                name=doc_data['name'],
                surname=doc_data['surname'],
                role='staff',
                is_staff=True
            )
            logger.info(f"Created user: {doc_data['email']}")

            # Create doctor
            Doctor.objects.create(
                department=departments[doc_data['department']],
                specialization=specializations[doc_data['specialization']],
                user=user
            )
            logger.info(f"Created doctor: {doc_data['name']} {doc_data['surname']}")

        except IntegrityError as e:
            logger.error(f"Failed to create doctor {doc_data['name']} {doc_data['surname']}: {str(e)}")
            continue

except Exception as e:
    logger.error(f"An error occurred during data population: {str(e)}")
    raise