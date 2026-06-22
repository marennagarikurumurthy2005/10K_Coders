from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls,user):
        token=super.get_token(user)


        # adding role and username to token 

        token['role']=user.role
        token['username']=user.username

        return token
    