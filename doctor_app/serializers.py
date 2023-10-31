from rest_framework import serializers
from doctor_app.models import UserDetails,DoctorProfile
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer



class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        token['is_doctor'] = user.is_doctor
        token['is_admin'] = user.is_admin
        return token



class UserRegisterSerializer(serializers.ModelSerializer):

    password2 = serializers.CharField(style={'input_type':'password'}, write_only=True)

    class Meta:
        model = UserDetails
        fields = ['username','email','password','password2','is_doctor']
    


    def validate(self,data):
        password = data.get('password')
        password2 = data.get('password2')
        username = data.get('username')
        # number = data.get('number')
        is_doctor = data.get('is_doctor')


        if password != password2:
            raise serializers.ValidationError("Passwords do not match.")   

        if len(password)<=3:
          raise serializers.ValidationError("password must contain atleast 4 characters") 

        # if len(username)<=4:
        #   raise serializers.ValidationError("username must contain atleast 4 characters")
        return data


    # def validate_username(self,)




class DoctorProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorProfile
        fields = ('hospital', 'department', 'speciality')

class UserDetailsSerializer(serializers.ModelSerializer):
    doctor_profile = DoctorProfileSerializer()  # Nest the DoctorProfile serializer within UserDetails serializer

    class Meta:
        model = UserDetails
        fields = ('username', 'email', 'first_name', 'last_name', 'phone', 'is_admin', 'is_active', 'is_superadmin', 'is_doctor', 'doctor_profile')






class DoctorProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorProfile
        fields = [ 'hospital', 'department', 'speciality']


class UserProfileSerializer(serializers.ModelSerializer):
    doctor = DoctorProfileSerializer() 
    class Meta:
        model = UserDetails
        fields = ['username', 'first_name', 'last_name', 'email', 'phone','doctor   ']


# class UserProfileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserDetails
#         fields = ['username', 'first_name', 'last_name', 'email', 'phone']

# class DoctorProfileSerializer(serializers.ModelSerializer):
#     user = UserProfileSerializer() 

#     class Meta:
#         model = DoctorProfile
#         fields = ['user', 'hospital', 'department', 'speciality']
    

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetails
        fields = ['username', 'email', 'first_name', 'last_name', 'phone','is_doctor']
