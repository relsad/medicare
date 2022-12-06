from django.db import models
from django.contrib.auth.models import User

# __________________________________________________________________________________________________________________________________

GENDER = [
    ("Male", "Male"),
    ("Female", "Female"),
    ("Other", "Other"),
]
Time = [
    ("10:00 A.M", "10:00 A.M"),
    ("10:30 A.M", "10:30 A.M"),
    ("11:00 A.M", "11:00 A.M"),
    ("11:30 A.M", "11:30 A.M"),
    ("12:00 P.M", "12:00 P.M"),
    ("12:30 P.M", "12:30 P.M"),
    ("01:00 P.M", "01:00 P.M"),
    ("01:30 P.M", "01:30 P.M"),
    ("05:00 P.M", "05:00 P.M"),
    ("05:30 P.M", "05:30 P.M"),
    ("06:00 P.M", "06:00 P.M"),
    ("06:30 P.M", "06:30 P.M"),
    ("07:00 P.M", "07:00 P.M"),
    ("07:30 P.M", "07:30 P.M"),
    ("08:00 P.M", "08:00 P.M"),
    ("08:30 P.M", "08:30 P.M"),
]

MARTIALSTATUS = [
    ("Married", "Married"),
    ("Single", "Single"),
    ("Divorced", "Divorced"),
    ("Widowed", "Widowed"),
]

BLOODGROUP = [
    ("A", "A"),
    ("AB", "AB"),
    ("B", "B"),
    ("O", "O"),
]


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    IIN = models.CharField(max_length=12, default="")
    ID = models.PositiveIntegerField(null=True)
    Patient_First_Name = models.CharField(max_length=50, default="")
    Patient_Last_Name = models.CharField(max_length=50, default="")
    Patient_Middle_Name = models.CharField(max_length=50, default="")
    contact = models.CharField(max_length=10)
    blood_group = models.CharField(max_length=3, choices=BLOODGROUP)
    emergency_number = models.CharField(max_length=10, default="")
    status = models.CharField(
        max_length=20, choices=MARTIALSTATUS, default="-")
    address = models.CharField(max_length=350)
    symptoms = models.CharField(max_length=500, default="")
    admitDate = models.DateField(auto_now=True)
    assignedDoctorId = models.PositiveIntegerField(null=True)

    gender = models.CharField(max_length=10, choices=GENDER)

    @property
    def get_name(self):
        return self.Patient_First_Name+" "+self.Patient_Last_Name

    @property
    def get_id(self):
        return self.id

    def str(self):
        return self.Patient_First_Name+" "+self.Patient_Last_Name

# __________________________________________________________________________________________________________________________________


departments = [('Cardiologist', 'Cardiologist'),
               ('Dermatologists', 'Dermatologists'),
               ('General Physician', 'General Physician'),
               ('NeuroSurgeon', 'NeuroSurgeon'),
               ('GastroEntologists', 'GastroEntologists'),
               ('Pediatrician', 'Pediatrician'),
               ('Emergency Medicine Specialists',
                'Emergency Medicine Specialists'),
               ('Allergists/Immunologists', 'Allergists/Immunologists'),
               ('Anesthesiologists', 'Anesthesiologists'),
               ('Colon and Rectal Surgeons', 'Colon and Rectal Surgeons')
               ]

doctor_category = [("Highest", "Highest"),
                   ("First", "First"), ("Second", "Second"), ]

degrees = [("Professional Doctorate", "Professional Doctorate"), ("Clinical Doctorate",
                                                                  "Clinical Doctorate"), ("Research Doctorate", "Research Doctorate"), ]


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField(null=True, blank=True)
    IIN = models.CharField(max_length=12, default="")
    ID = models.PositiveIntegerField(null=True)
    Doctor_First_Name = models.CharField(max_length=50, default="")
    Doctor_Last_Name = models.CharField(max_length=50, default="")
    Doctor_Middlename = models.CharField(max_length=50, default="")
    contact = models.CharField(max_length=10, null=True)
    #
    # specialization_details_id = models.CharField(max_length=3)
    #
    department = models.CharField(
        max_length=50, choices=departments, default='')
    exp_years = models.PositiveIntegerField(null=False, default=0)
    photo_URI = models.CharField(max_length=100, default="")
    category = models.CharField(choices=doctor_category,max_length=25, default="-")
    price_of_appointment = models.PositiveIntegerField(null=True)
    # schedule_details = models.CharField(max_length=20, choices=degrees)
    degree = models.CharField(max_length=50, default=" ",choices=degrees)
    rating = models.PositiveIntegerField(null=False, default=0)

    address = models.CharField(max_length=40)

    status = models.BooleanField(default=False)
    gender = models.CharField(max_length=10, choices=GENDER, default="")

    @property
    def get_name(self):
        return self.Doctor_First_Name+" "+self.Doctor_Last_Name

    @property
    def get_id(self):
        return self.id

    def str(self):
        return "{} ({})".format(self.Doctor_First_Name+" "+self.Doctor_Last_Name, self.department)

# __________________________________________________________________________________________________________________________________


class Appointment(models.Model):
    patientId = models.PositiveIntegerField(null=True)
    doctorId = models.PositiveIntegerField(null=True)
    patientName = models.CharField(max_length=40, null=True)
    doctorName = models.CharField(max_length=40, null=True)
    appointmentDate = models.DateField(null=False)
    description = models.TextField(max_length=500)
    status = models.BooleanField(default=False)
    time = models.CharField(max_length=10, choices=Time, default="")

    @property
    def get_docId(self):
        return self.doctorId

    @property
    def get_description(self):
        return self.description

    @property
    def get_status(self):
        return self.status

# __________________________________________________________________________________________________________________________________


class PatientDischarge(models.Model):
    patientId = models.PositiveIntegerField(null=True)
    patientName = models.CharField(max_length=40)
    assignedDoctorName = models.CharField(max_length=40)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20, null=True)
    symptoms = models.CharField(max_length=100, null=True)
    admitDate = models.DateField(null=False)
    releaseDate = models.DateField(null=False)
    daySpent = models.PositiveIntegerField(null=False)
    roomCharge = models.PositiveIntegerField(null=False, default=0)
    medicineCost = models.PositiveIntegerField(null=False, default=0)
    doctorFee = models.PositiveIntegerField(null=False, default=0)
    OtherCharge = models.PositiveIntegerField(null=False, default=0)
    total = models.PositiveIntegerField(null=False)


# __________________________________________________________________________________________________________________________________
# ________________________________________________________________________________________________________________________
