from django import forms
from django.contrib.auth.models import User
from MyApp.models import Patient, Doctor, Appointment


class DateInput(forms.DateInput):
    input_type = 'date'

#_____________________________________________________________________________________________________________________

GENDER =(
    ("Male", "Male"),
    ("Female", "Female"),
    ("Other", "Other"),
)
Time = [
    ("10:00 A.M","10:00 A.M"),
    ("10:30 A.M","10:30 A.M"),
    ("11:00 A.M","11:00 A.M"),
    ("11:30 A.M","11:30 A.M"),
    ("12:00 P.M","12:00 P.M"),
    ("12:30 P.M","12:30 P.M"),
    ("01:00 P.M","01:00 P.M"),
    ("01:30 P.M","01:30 P.M"),
    ("05:00 P.M","05:00 P.M"),
    ("05:30 P.M","05:30 P.M"),
    ("06:00 P.M","06:00 P.M"),
    ("06:30 P.M","06:30 P.M"),
    ("07:00 P.M","07:00 P.M"),
    ("07:30 P.M","07:30 P.M"),
    ("08:00 P.M","08:00 P.M"),
    ("08:30 P.M","08:30 P.M"),
]
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


class PatientUserInfo(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput()) #hash out the password
    
    class Meta():
        model = User
        fields = ('username','email','password')

class PatientSignUpForm(forms.ModelForm):
    class Meta():
        model = Patient
        fields = ('IIN','Patient_First_Name','Patient_Last_Name','Patient_Middle_Name', 'address', 'contact','emergency_number','blood_group','martial_status', 'gender')        
#_____________________________________________________________________________________________________________________

class DoctorUserInfo(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput()) #hash out the password
    
    class Meta():
        model = User
        fields = ('username','password')

class DoctorSignUpForm(forms.ModelForm):
    class Meta():
        model = Doctor
        fields = ('date_of_birth','IIN', 'ID','Doctor_First_Name','Doctor_Last_Name','Doctor_Middlename','photo_URI', 'contact', 'department','exp_years','category','price_of_appointment',
        'degree','rating','address','gender')
        
#_____________________________________________________________________________________________________________________
class AdminUserInfo(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput()) #hash out the password
    
    class Meta():
        model = User
        fields = ('username','password')

class AdminSignUpForm(forms.ModelForm):
    class Meta():
        model = User
        fields = ('first_name','last_name','username','password')
#_____________________________________________________________________________________________________________________

class AppointmentForm(forms.ModelForm):
    doctorId=forms.ModelChoiceField(queryset=Doctor.objects.all().filter(status=True),empty_label="Doctor Name and Department", to_field_name="user_id")
    patientId=forms.ModelChoiceField(queryset=Patient.objects.all().filter(status=True),empty_label="Patient Name", to_field_name="user_id")
    appointmentDate = forms.DateField(widget = forms.SelectDateWidget())
    class Meta:
        model=Appointment
        fields=['appointmentDate','time','description']

class PatientAppointmentForm(forms.ModelForm):
    doctorId=forms.ModelChoiceField(queryset=Doctor.objects.all().filter(status=True),empty_label="Doctor and Department", to_field_name="user_id")
    
    appointmentDate = forms.DateField(widget = forms.SelectDateWidget())
    class Meta:
        model=Appointment
        fields=['appointmentDate','time','description']


# class PatientAppointmentDateForm(forms.ModelForm):
    
#     appointmentDate = forms.DateField(widget = forms.SelectDateWidget())
#_____________________________________________________________________________________________________________________
