from .utils import decrypt_weight
from .models import Patient


def query_patients_by_weight_range(min_weight, max_weight):
    patients = Patient.objects.all()
    patients = [patient for patient in patients if min_weight <=
                decrypt_weight(patient.weight) <= max_weight]
    return patients
