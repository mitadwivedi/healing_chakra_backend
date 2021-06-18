from django.core import serializers
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework.views import APIView

# Create your views here.
from healing_chakra_app.models import LoginCredentials, SignUpCredentials, MedicineDonation, EquipmentDonation


class LoginRequest(APIView):
    @staticmethod
    def post(request):
        username = request.data.pop('username')
        password = request.data.pop('password')

        user = LoginCredentials.objects.filter(username=username, password=password)

        if len(user) == 1:
            return Response({
                "Login": "Successful"
            })
        else:
            return Response({
                "Login": "Failed"
            })


class GetUser(APIView):
    @staticmethod
    def post(request):
        username = request.data.pop('username')
        user = SignUpCredentials.objects.filter(username=username)

        user_data = {'dataAvailable': "TRUE", 'username': user[0].username, 'name': user[0].name,
                     'mobile': user[0].mobile,
                     'aadhaar': user[0].aadhaar, 'location': user[0].location}

        return Response({
            'user_data': user_data
        })


class SignUpRequest(APIView):
    def post(self, request):
        username = request.data.pop('username')
        password = request.data.pop('password')
        name = request.data.pop('name')
        email = request.data.pop('email')
        mobile = request.data.pop('mobile')
        aadhaar = request.data.pop('aadhaar')
        location = request.data.pop('location')

        user = SignUpCredentials.objects.filter(username=username)
        if len(user) > 0:
            return Response({
                "signUp": "Username Already Exists"
            })
        else:
            new_user = SignUpCredentials.objects.create(
                username=username, password=password, name=name, email=email, mobile=mobile,
                aadhaar=aadhaar, location=location)

            new_login_creds = LoginCredentials.objects.create(username=username, password=password)

            return Response({
                "signUp": "Successful"
            })


class SaveMedicieneDonation(APIView):
    def post(self, request):
        username = request.data.pop('username')
        name = request.data.pop('name')
        mobile = request.data.pop('mobile')
        aadhaar = request.data.pop('aadhaar')
        location = request.data.pop('location')
        medicine_name = request.data.pop('medicinename')
        manufacture_date = request.data.pop('manufacturedate')
        expiry_date = request.data.pop('expirydate')

        new_donation = MedicineDonation.objects.create(
            username=username, name=name, mobile=mobile, aadhaar=aadhaar, location=location,
            medicine_name=medicine_name, manufacture_date=manufacture_date, expiry_date=expiry_date)

        return Response({
            "donateStatus": "Successful"
        })


class SaveEquipmentDonation(APIView):
    def post(self, request):
        username = request.data.pop('username')
        name = request.data.pop('name')
        mobile = request.data.pop('mobile')
        aadhaar = request.data.pop('aadhaar')
        location = request.data.pop('location')
        equipment_name = request.data.pop('equipmentname')
        manufacture_date = request.data.pop('manufacturedate')

        new_donation = EquipmentDonation.objects.create(
            username=username, name=name, mobile=mobile, aadhaar=aadhaar, location=location,
            equipment_name=equipment_name, manufacture_date=manufacture_date)

        return Response({
            "donateStatus": "Successful"
        })


class GetDonatedMedicine(APIView):
    def post(self, request):
        all_donations = MedicineDonation.objects.all()

        donations = json.loads(serializers.serialize("json", all_donations))

        return Response({
            "all_donations": donations
        })


class GetDonatedEquipment(APIView):
    def post(self, request):
        all_donations = EquipmentDonation.objects.all()

        donations = json.loads(serializers.serialize("json", all_donations))

        return Response({
            "all_donations": donations
        })