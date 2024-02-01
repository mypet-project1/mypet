from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from django.shortcuts import get_object_or_404

from .serializers import HospitalSerializer, ReviewSerializer
from .models import Hospital, Review


class HospitalsAPIView(APIView):
    def get(self, reqeust):
        hospitals = Hospital.objects.all()
        serializer = HospitalSerializer(hospitals, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        request.data["user"] = 2  # request.user.id로 교체
        serializer = HospitalSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(status=status.HTTP_201_CREATED)

        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class OnehospitalAPIView(APIView):
    def get(self, request, id):
        hospital = get_object_or_404(Hospital, id=id)

        serializer = HospitalSerializer(hospital)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request, id):
        request.data["user"] = 2  # request.user.id로 교체
        hospital = get_object_or_404(Hospital, id=id)
        serializer = HospitalSerializer(hospital, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(status=status.HTTP_200_OK)

        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
