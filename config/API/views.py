import datetime

from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.response import Response
from .serializers import LinkSerializer
from .models import Link

from rest_framework.views import APIView


@api_view(['POST'])

def visited_links(request, *args, **kwargs):
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
    date = datetime.datetime.now()
    from_date = request.GET.get('from', 0)
    to_date = request.GET.get('to', date)
    try:
        from_date = float(from_date)
        to_date = float(to_date)
    except ValueError as e:
        response = {'status': 'bad GET parameter'}
        return Response(response, 400)

    queryset = []
    for link in Link.objects.all():
        if from_date <= date <= to_date:
            queryset.append(link)
    return Response({"status": "ok", "domains": queryset})







