from django.core.exceptions import ValidationError
from rest_framework import serializers
# from django.contrib.auth.models import User
from .models import Manager, Employee



class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=65, min_length=8, write_only=True,
        required=True,
        style={'input_type': 'password',}
    )


    class Meta:
        model = Manager
        fields = ['email', 'firstname', 'lastname', 'password', 'address', 'dob', 'company'
                  ]

    def validate(self, attrs):
        email = attrs.get('email', '')
        if Manager.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                {'email': ('Email is already in use')})
        return super().validate(attrs)

    def create(self, validated_data):
        return Manager.objects.create(**validated_data)


class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=65, min_length=8, write_only=True,
        required=True,
        style={'input_type': 'password', }
    )
    class Meta:
        model=Manager
        fields=('email','password')


class EmplyeeSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=65, min_length=8, write_only=True,
        required=True,
        style={'input_type': 'password', }
    )
    class Meta:
        model=Employee
        fields="__all__"


# class UserLogoutSerializer(serializers.ModelSerializer):
#     token = serializers.CharField()
#     status = serializers.CharField(required=False, read_only=True)
#
#     def validate(self, data):
#         token = data.get("token", None)
#         print(token)
#         user = None
#         try:
#             user = Manager.objects.get(token=token)
#             if not user.ifLogged:
#                 raise ValidationError("User is not logged in.")
#         except Exception as e:
#             raise ValidationError(str(e))
#         user.ifLogged = False
#         user.token = ""
#         user.save()
#         data['status'] = "User is logged out."
#         return data
#
#     class Meta:
#         model = Manager
#         fields = (
#             'token',
#             'status',
#         )