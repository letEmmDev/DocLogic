from core.models import CustomUser
from hospital.models import Department
from patient_management.models import Patient
from django.db import IntegrityError
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

departments = list(Department.objects.all())
if not departments:
    logger.error("No departments found. Please run hydrate_db.py first.")
    exit()

patients_data = [
    {'email': 'alice.martin@patients.com', 'name': 'Alice', 'surname': 'Martin', 'age': 28, 'department': 'Cardiology'},
    {'email': 'benjamin.ross@patients.com', 'name': 'Benjamin', 'surname': 'Ross', 'age': 34, 'department': 'Pediatrics'},
    {'email': 'carla.garcia@patients.com', 'name': 'Carla', 'surname': 'Garcia', 'age': 45, 'department': 'Oncology'},
    {'email': 'daniel.kim@patients.com', 'name': 'Daniel', 'surname': 'Kim', 'age': 52, 'department': 'Maternity'},
    {'email': 'emma.dupont@patients.com', 'name': 'Emma', 'surname': 'Dupont', 'age': 23, 'department': 'Neurology'},
    {'email': 'frank.nguyen@patients.com', 'name': 'Frank', 'surname': 'Nguyen', 'age': 39, 'department': 'Cardiology'},
    {'email': 'grace.lee@patients.com', 'name': 'Grace', 'surname': 'Lee', 'age': 31, 'department': 'Pediatrics'},
    {'email': 'henry.schmidt@patients.com', 'name': 'Henry', 'surname': 'Schmidt', 'age': 60, 'department': 'Oncology'},
    {'email': 'isabelle.moreau@patients.com', 'name': 'Isabelle', 'surname': 'Moreau', 'age': 27, 'department': 'Maternity'},
    {'email': 'julien.bernard@patients.com', 'name': 'Julien', 'surname': 'Bernard', 'age': 41, 'department': 'Neurology'},
]

for pdata in patients_data:
    try:
        if CustomUser.objects.filter(email=pdata['email']).exists():
            logger.warning(f"User with email {pdata['email']} already exists, skipping.")
            continue

        user = CustomUser.objects.create_user(
            email=pdata['email'],
            password='SecurePass2025!',
            name=pdata['name'],
            surname=pdata['surname'],
            role='patient',
            is_patient=True
        )
        logger.info(f"Created user: {pdata['email']}")

        dept = Department.objects.get(name=pdata['department'])

        Patient.objects.create(
            user=user,
            age=pdata['age'],
            department=dept
            # All other fields left empty for CRUD
        )
        logger.info(f"Created patient: {pdata['name']} {pdata['surname']}")

    except IntegrityError as e:
        logger.error(f"Failed to create patient {pdata['name']} {pdata['surname']}: {str(e)}")
        continue
    except Department.DoesNotExist:
        logger.error(f"Department {pdata['department']} does not exist for patient {pdata['name']} {pdata['surname']}")
        continue