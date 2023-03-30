from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Room, Message, Topic
from .serializers import RoomSerializer, TopicSerializer, MessageSerializer
from base.api import serializers


@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /api',
        'GET /api/rooms',
        'GET /api/rooms/:id',
        'GET /api/topic',
        'GET /api/messages'
    ]
    return Response(routes)


@api_view(['GET'])
def getRooms(request):
    rooms = Room.objects.all()
    serializer = RoomSerializer(rooms, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getRoom(request, pk):
    room = Room.objects.get(id=pk)
    serializer = RoomSerializer(room, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def getTopic(request):
    topic = Topic.objects.all()
    serializer = TopicSerializer(topic, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getMessage(request):
    messages = Message.objects.all()
    serializer = MessageSerializer(messages, many=True)
    return Response(serializer.data)