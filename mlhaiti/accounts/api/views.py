from django.contrib.auth import get_user_model

from rest_framework import views, generics, permissions, status
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
                'data':[],
                'message':serializer.errors
            },
            status=status.HTTP_400_BAD_REQUEST
        )

