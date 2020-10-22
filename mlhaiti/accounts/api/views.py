from django.contrib.auth import get_user_model, authenticate
from rest_framework import views, generics, permissions, status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response 

from mlhaiti.accounts.api.serializers import UserSerializer

User = get_user_model()

class UserCreateView(generics.CreateAPIView):
    """
        User Registration
    """    
    permission_classes = []
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    'status':201,
                    'error':False,
                    'data':serializer.data,
                    'message':'user registred successfully'
                },
                status=status.HTTP_201_CREATED
            )

        return Response(
            {
                'status':400,
                'error':True,
                'data':{},
                'message':serializer.errors
            },
            status=status.HTTP_400_BAD_REQUEST
        )

class UserLoginView(views.APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self,request):
        username = request.data.get('username')
        password = request.data.get('password')
        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                token = Token.objects.get_or_create(user=user)[0]
                data = UserSerializer(user).data
                data['token'] = token.key 
                return Response({'error':False, "message": "User Login Successfully", "data":data, "status": 200}, status=status.HTTP_200_OK)
            message = "Unable to login with given credentials"
            return Response({'error':True, "error_message": message , 'data': {}, 'status':401}, status=status.HTTP_401_UNAUTHORIZED)
        message = "Invalid Credentials"
        return Response({'error':True, "error_message": message , 'data': {}, 'status':401}, status=status.HTTP_401_UNAUTHORIZED)
