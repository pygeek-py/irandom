from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authentication import get_authorization_header
from django.http import HttpResponseRedirect
from django.urls import reverse
from .serializers import userserializer, workserializer, acceptserializer, boxserializer
from .models import work, accept, box
from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.models import User
import jwt, datetime
from rest_framework.authtoken.models import Token
from rest_framework import viewsets, filters, generics, permissions
from rest_framework.parsers import MultiPartParser, FormParser

# Create your views here.

#authentication api

@api_view(['POST'])
def RegisterView(request):
		serializer = userserializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		return Response(serializer.data)

@api_view(['POST'])
def LoginView(request):
		username = request.data['username']
		password = request.data['password']

		print(username)
		print(password)

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			serializer = userserializer(user)

		#user = User.objects.filter(username=username).first()

		if user is None:
			raise AuthenticationFailed('User not found')
		if not user.check_password(password):
			raise AuthenticationFailed('Incorrect password')

		payload = {
			'id': user.id,
			'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
			'iat': datetime.datetime.utcnow()
		}

		token = jwt.encode(payload, 'secret', algorithm='HS256')

		response = Response()

		response.set_cookie(key='jwt', value=token, httponly=True)
		response.data = {
			'jwt': token
			}

		return response

class UserView(APIView):

	def get(self, request):
		token = request.COOKIES.get('jwt')

		if not token:
			raise AuthenticationFailed('Unauthenticated')

		try:
			payload = jwt.decode(token, 'secret', algorithms=['HS256'])
		except jwt.ExpiredSignatureError:
			raise AuthenticationFailed('Unauthenticated')

		user = User.objects.filter(id=payload['id']).first()
		serializer = userserializer(user)
		return Response(serializer.data)



@api_view(['GET'])
def logoutview(request):
	logout(request)
	response = Response()
	response.data = {
		'message': 'success'
	}
	return response

@api_view(['GET'])
def listwork(request):
	random = work.objects.all()
	serializer = workserializer(random, many=True)
	return Response(serializer.data)


@api_view(['POST'])
def creatework(request):
	serializer = workserializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)

@api_view(['POST'])
def acceptwork(request):
	auth = get_authorization_header(request).split()
	token = auth[1].decode('utf-8')
	#token = request.COOKIES.get('jwt')
	if not token:
		raise AuthenticationFailed('Unauthenticateds')

	try:
		payload = jwt.decode(token, 'secret', algorithms=['HS256'])
	except jwt.ExpiredSignatureError:
		raise AuthenticationFailed('Unauthenticated')

	user = User.objects.filter(id=payload['id']).first()
	serializer = userserializer(user)
	users = user
	serializer = acceptserializer(data=request.data)
	if serializer.is_valid():
		serializer.save(user=users)
	return Response(serializer.data)

@api_view(['GET'])
def listaccept(request):
	#auth = get_authorization_header(request).split()
	#token = auth[1].decode('utf-8')
	token = request.COOKIES.get('jwt')
	if not token:
		raise AuthenticationFailed('Unauthenticateds')

	try:
		payload = jwt.decode(token, 'secret', algorithms=['HS256'])
	except jwt.ExpiredSignatureError:
		raise AuthenticationFailed('Unauthenticated')

	user = User.objects.filter(id=payload['id']).first()
	serializer = userserializer(user)
	users = user
	random = accept.objects.filter(user=users)
	serializer = acceptserializer(random, many=True)
	return Response(serializer.data)

@api_view(['DELETE'])
def acceptdel(request, pk):
	item = accept.objects.get(id=pk)
	item.delete()
	return Response('Item Successfully delete')

class postadd(APIView):
	parser_classes = [MultiPartParser, FormParser]

	def post(self, request, format=None):
		#auth = get_authorization_header(request).split()
		#token = auth[1].decode('utf-8')
		token = request.COOKIES.get('jwt')
		if not token:
			raise AuthenticationFailed('Unauthenticateds')		

		try:
			payload = jwt.decode(token, 'secret', algorithms=['HS256'])
		except jwt.ExpiredSignatureError:
			raise AuthenticationFailed('Unauthenticated')

		user = User.objects.filter(id=payload['id']).first()
		serializer = userserializer(user)
		users = user
		print(users)
		serializer = boxserializer(data=request.data)
		if serializer.is_valid():
			serializer.save(user=users)
			print("nice")
		return Response(serializer.data)

@api_view(['GET'])
def getallpost(request):
	pat = box.objects.all()
	serializer = boxserializer(pat, many=True)
	return Response(serializer.data)