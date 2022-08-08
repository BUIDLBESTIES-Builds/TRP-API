from bdb import set_trace
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
# from .serializers import UserSerializer,RegisterSerializer
from .models import User

from api.serializers import UserSerializer, ReimbursementSerializer, ReimbursementDetailSerializer
from api.models import User, Reimbursement

# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer


class ReimbursementViewSet(viewsets.ModelViewSet):
   queryset = Reimbursement.objects.all()
   serializer_class = ReimbursementSerializer
   

class ReimbursementDetailViewSet(viewsets.ModelViewSet):
   serializer_class = ReimbursementDetailSerializer
   lookup_field = 'user__fullname'

   def get_queryset(self):
      queryset = Reimbursement.objects.filter(user__fullname=self.kwargs['user__fullname'])
      return queryset

   def retrieve(self, request, *args, **kwargs):
      serializer = self.get_serializer(self.get_queryset(), many=True)
      return Response(data=serializer.data)

      
