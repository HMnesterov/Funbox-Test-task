import datetime

from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.response import Response
from .serializers import LinkSerializer
from .models import Link

from rest_framework.views import APIView


@api_view(['POST'])

def visited_links(self, request, *args, **kwargs):
    try:
        for link in request.data.get('links'):
            try:
                Link.objects.create(link=link)
            except:
                continue
        return Response({"status": "ok"})
    except Exception as error:
        return Response({"status": "Error"})

@api_view(["GET"])
def visited_domains(request, *args, **kwargs):
    date = datetime.datetime.now().timestamp()
    print(date)
    return Response({"Биля": "Блия1"})




