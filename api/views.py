from django.shortcuts import render
from django.http import JsonResponse
from .serializers import CarSerializer, DraftSerializer
import json
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import car, draft

@api_view(["POST"])
@permission_classes((IsAuthenticated, ))
@authentication_classes((JSONWebTokenAuthentication, ))
def add_car(request):
    payload = json.loads(request.body)
    try:
        for data in payload['cars']:
            Car = car.objects.create(
                user=request.user,
                accident=data["accident"],
                repair=data["repair"],
                manufacturer=data["manufacturer"],
                price=data["price"]
            )
        return JsonResponse({'message': 'Success' }, safe=False, status=status.HTTP_201_CREATED)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something is wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["POST"])
@permission_classes((IsAuthenticated, ))
@authentication_classes((JSONWebTokenAuthentication, ))
def draft_car(request):
    payload = json.loads(request.body)
    try:
        for data in payload['cars']:
            Draft = draft.objects.create(
                user=request.user,
                accident=data["accident"],
                repair=data["repair"],
                manufacturer=data["manufacturer"],
                price=data["price"]
            )
        return JsonResponse({'message': 'Success' }, safe=False, status=status.HTTP_201_CREATED)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something is wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
