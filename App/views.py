from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.parsers import JSONParser
from .serializers import UserSerializer

from App.models import User

# Create your views here.

def test(request):
    return HttpResponse("Hello, world. You're Working Fine. Go Ahead!")


@csrf_exempt
def signup(request):
    if request.method == 'POST':
        try:
            input_data = JSONParser().parse(request)
            serializer_data=UserSerializer(data=input_data)

            if serializer_data.is_valid():
                serializer_data.save()
                return JsonResponse(serializer_data.data, safe=False, status = 201)
            else:
                return JsonResponse(serializer_data.errors, safe=False,status = 400)

        except Exception as e:
            print(e)
            data={'errors':e}
            return JsonResponse(data,status = 400)
        
        
def allUserDetails(request):
    if request.method == 'GET':
        try:
            users = User.objects.all()
            serializer = UserSerializer(users, many=True)
            return JsonResponse(serializer.data, safe=False, status = 200)
        
        except Exception as e:
            print(e)
            data = {
                   "success": False,
                   "message": "Error Getting user",
               }
            return JsonResponse(data, status=400)


def userDetails(request,username):
    if request.method == 'GET':
        try:
            user = User.objects.get(pk=username)
            serializer = UserSerializer(user)
            return JsonResponse(serializer.data, safe=False, status = 200)
        except Exception as e:
            print(e)
            data = {
                   "success": False,
                   "message": "Error Getting user",
               }
            return JsonResponse(data, status=400)


@csrf_exempt 
def editUserDetails(request,username):
    if request.method == 'PUT':
        try:
            input_data = JSONParser().parse(request)
            user = User.objects.get(pk=username)
            serializer_data=UserSerializer(user,data=input_data)

            if serializer_data.is_valid():
                serializer_data.save()
                return JsonResponse(serializer_data.data, safe=False, status = 201)
            else:
                return JsonResponse(serializer_data.errors, safe=False,status = 400)
        except Exception as e:
            print(e)
            data = {
                    "success": False,
                    "message": "Error Updating user",
                }
            return JsonResponse(data, status=400)


@csrf_exempt  
def deleteUserDetails(request,username):
        if request.method == 'DELETE':     
            try:
                user = User.objects.get(pk=username)
                user.delete()
                data={
                    "success": True,
                    "message": f"User {username} Deleted Successfully",
                }
                return JsonResponse(data,status=200)
            except Exception as e:
                print(e)
                data = {
                    "success": False,
                    "message": "Error deleting user",
                }
                return JsonResponse(data, status=400)
        else:
            return JsonResponse({"message": "Method not allowed"},status=405)