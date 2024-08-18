from django.shortcuts import render
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from Event.models import Events
from .serializers import EventsSerializer
from random import choice
from User_App.models import CustomUser

# Create your views here.

class CreateGetEvent(APIView):
    def get(self, request):
        user = request.CustomUser
        Events = Events.objects.all()

        return Response(data ={
            "data": EventsSerializer(Events, many=True).data,
            "message":"Event retrieved"
        },
        status=status.HTTP_200_OK
        )
        
class DeleteRetrievedEvent(APIView):
    def get(self, request, id):
        Event = Events.objects.filter(id=id)
        if not Event.exists():
            return Response(data={"message":"Event with this ID does not exist"}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(data={
            "message":"Event retrived",
            "data": EventsSerializer(Event[0]).data
        })


    def delete(self, request, id):
        try:
            Events.objects.get(id=id).delete()
        except:
            pass
        return Response(data={
            "message":"Event deleted",
        },
        status= status.HTTP_201_CREATED
        )

class JoinEvent(APIView):
    def post(self, request):
        Events_id = request.data.get("Events_id")
        user_id = request.data.get("CustomUser_id")
        try:
            Event = Events.objects.get(id = Events_id)
        except:
            return Response(
                data={
                    "message":"Event with this ID does not exist",
                },
                status= status.HTTP_400_BAD_REQUEST
            )
        


        try:
            user = CustomUser.objects.get(id = user_id)
        except:
            return Response(
                data={
                    "message":"User with this ID does not exist",
                },
                status= status.HTTP_400_BAD_REQUEST
            )
        
        if user.id == Events.Created_by.id:
            return Response(data={
                "message":"Event leader not allowed"
            },
            status=status.HTTP_406_NOT_ACCEPTABLE
            )

      
        try:
            Events.Events_members.get(id = user.id)
            return Response(
                data={
                    "message":"User is already a member"
                },
                status= status.HTTP_400_BAD_REQUEST
            )
        except:
            pass
            
        Events.Events_members.add(user)
        Events.save()
        return Response(data={
            "message":"User joined Event",
            "data":EventsSerializer(Events).data
        })
        
