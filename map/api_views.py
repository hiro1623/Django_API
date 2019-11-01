from .models import PostData,Account
from .serializers import PostDataSerializer,AccountSerializer
from rest_framework import viewsets,status,generics,permissions
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from django.db import transaction

class PostDataViewSet(APIView):
    parser_classes = (MultiPartParser, FormParser)
    def get(self, request, *args, **kwargs):
        posts = PostData.objects.all()
        serializer = PostDataSerializer(posts, many=True)
        return Response(serializer.data)
    def post(self, request, *args, **kwargs):
        posts_serializer = PostDataSerializer(data=request.data)
        if posts_serializer.is_valid():
            posts_serializer.save()
            return Response(posts_serializer.data, status=status.HTTP_201_CREATED)
        else:
            print('error', posts_serializer.errors)
            return Response(posts_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ユーザ作成のView(POST)
class AuthRegister(generics.CreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = (permissions.AllowAny,)
    @transaction.atomic
    def post(self, request, format=None):
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ユーザの取得View(GET)
class AuthGet(generics.ListAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    def get(self, request, format=None):
        return Response(data={'id': request.user.id,'username':request.user.username}, status=status.HTTP_200_OK)