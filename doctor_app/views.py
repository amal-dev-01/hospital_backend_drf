from django.shortcuts import render
from rest_framework.views import APIView
from doctor_app.serializers import UserRegisterSerializer,UserProfileSerializer,DoctorProfileSerializer,AdminSerializer,MyTokenObtainPairSerializer
from doctor_app.models import UserDetails,DoctorProfile
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser,AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.decorators import permission_classes

from .serializers import UserDetailsSerializer



# {
#     "username":"amal","number":"93949494","email":"amal@gmail.com","password":"1234","password2":"1234"
# }

class Register(APIView):

     def post(self,request,format  = None):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data.get('email')
            username = serializer.validated_data.get('username')
            password = serializer.validated_data.get('password')
            is_doctor = serializer.validated_data.get('is_doctor')
            # number = serializer.validated_data.get('number')
            user =  UserDetails.objects.create_user(
                email = email,
                username = username,
                password = password,
                is_doctor=is_doctor,
            )
            if user.is_doctor:
                DoctorProfile.objects.create(user=user)
            return Response({'msg':'data inserted'},status = status.HTTP_201_CREATED)

        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
    

# class Login(APIView):

#     def post(self, request):
#         username = request.data.get('username')
#         # print(username)
#         password = request.data.get('password')
#         # print(password)
#         # serializer = LoginSerializer(data=request.data)
#         user = authenticate(request, username=username, password=password)
#         print(user)
#         if user is not None:
#             refresh = RefreshToken.for_user(user)
#             access_token = str(refresh.access_token)
#             refresh_token = str(refresh)
#             return Response({
#                 'access_token': access_token,
#                 'refresh_token': refresh_token,
#             }, status=status.HTTP_200_OK)
#         else:
#             return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


   
class UserProfileView(APIView):
  
    authentication_classes =[JWTAuthentication]
    permission_classes = [IsAuthenticated]


    def get(self, request):
        user = request.user

        if user.is_doctor:
            try:
                doctor_profile = DoctorProfile.objects.get(user=user)
                doctor_serializer = DoctorProfileSerializer(doctor_profile)
                data = {
                    'doctor_profile': doctor_serializer.data,
                    'username': user.username, 
                    'first_name': user.first_name ,
                    'last_name':user.last_name,
                    'phone':user.phone,
                    'email':user.email
                     }
                return Response(data, status=status.HTTP_200_OK)
            except DoctorProfile.DoesNotExist:
                return Response({'detail': 'Doctor profile not found.'}, status=status.HTTP_404_NOT_FOUND)
        else:
            try:
                user_serializer = UserDetailsSerializer(user)
                return Response(user_serializer.data, status=status.HTTP_200_OK)
            except UserDetails.DoesNotExist:
                return Response({'detail': 'User profile not found.'}, status=status.HTTP_404_NOT_FOUND)

    # def get(self, request):
    #     try:
    #         user = request.user
    #         if user.is_doctor:
    #             doctor_profile = DoctorProfile.objects.get(user=user)
    #             serializer = DoctorProfileSerializer(doctor_profile)
    #         else:
    #             user_profile = UserDetails.objects.get(id=user.id)
    #             serializer = UserProfileSerializer(user_profile)

    #         return Response(serializer.data, status=status.HTTP_200_OK)
    #     except UserDetails.DoesNotExist:
    #         return Response({'detail': 'User profile not found.'}, status=status.HTTP_404_NOT_FOUND)
    #     except DoctorProfile.DoesNotExist:
    #         return Response({'detail': 'Doctor profile not found.'}, status=status.HTTP_404_NOT_FOUND)

    def patch(self, request):
        try:
            user = request.user
            if user.is_doctor:
                doctor_profile = DoctorProfile.objects.get(user=user)
                doctor_serializer = DoctorProfileSerializer(doctor_profile, data=request.data, partial=True)

                if 'first_name' in request.data:
                    user.first_name = request.data['first_name']
                if 'last_name' in request.data:
                    user.last_name = request.data['last_name']
                if 'phone' in request.data:
                    user.phone = request.data['phone']
                user.save()  

                if doctor_serializer.is_valid():
                    doctor_serializer.save()
                    return Response(doctor_serializer.data, status=status.HTTP_200_OK)
                else:
                    return Response(doctor_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                user_profile = UserDetails.objects.get(id=request.user.id)
                serializer = UserDetailsSerializer(user_profile, data=request.data, partial=True)

                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)

                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except UserDetails.DoesNotExist:
            return Response({'detail': 'User profile not found.'}, status=status.HTTP_404_NOT_FOUND)
        except DoctorProfile.DoesNotExist:
            return Response({'detail': 'Doctor profile not found.'}, status=status.HTTP_404_NOT_FOUND)


    def delete(self, request):
        user = request.user

        if user.is_doctor:
            try:
                doctor_profile = DoctorProfile.objects.get(user=user)
                doctor_profile.delete()
                return Response({'detail': 'Doctor profile deleted.'}, status=status.HTTP_204_NO_CONTENT)
            except DoctorProfile.DoesNotExist:
                return Response({'detail': 'Doctor profile not found.'}, status=status.HTTP_404_NOT_FOUND)
        else:
            try:
                user_profile = UserDetails.objects.get(id=user.id)
                user_profile.delete()
                return Response({'detail': 'User profile deleted.'}, status=status.HTTP_204_NO_CONTENT)
            except UserDetails.DoesNotExist:
                return Response({'detail': 'User profile not found.'}, status=status.HTTP_404_NOT_FOUND)



class UserDoctorView(APIView):
    def get(self, request):
        doctors = DoctorProfile.objects.all()  
        serializer = DoctorProfileSerializer(doctors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# {
#     "username": "amal",
#     "password": "1234",
#     "password2": "1234",
#     "email": "amal@gmail.com"
# }
#

# class UserDetailListView(ListAPIView):
#     queryset = UserDetails.objects.all()
#     serializer_class = UserDetailSerializer


class AdminView(APIView):
    permission_classes = [IsAdminUser]
    def get(self,request):
        user = UserDetails.objects.all()
        serializer = AdminSerializer(user,many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def patch(self, request, pk):
        try:
            user = UserDetails.objects.get(id=pk)
            print(user)
            print(user.is_active,'b4')

            user.is_active = not user.is_active 
            print(user.is_active)

            user.save()
            serializer = AdminSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except UserDetails.DoesNotExist:
            return Response({'detail': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)