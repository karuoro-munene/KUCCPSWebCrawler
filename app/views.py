import json

from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView


class APIRoot(APIView):

    def get(self, request):
        current_site = get_current_site(request)
        if current_site.name != 'localhost':
            ext = 's'
        else:
            ext = ''
        paths = {
            "Institutions List": f"http{ext}://{current_site}/api/v1/institutions",
            "Programme Details": f"http{ext}://{current_site}/api/v1/programme/details",
        }
        return Response(paths)


@api_view(['GET'])
def institutions(request):
    """
    Institutions List crawled from KUCCPS website
    """
    # load institutions from scrapy
    data = settings.BASE_DIR / 'kuccps/institutions.json'
    json_file = open(data)
    institutions = json.load(json_file)
    json_file.close()
    return Response(institutions)


@api_view(['GET'])
def programme_details(response):
    """
    Degree Programme Details crawled from KUCCPS website
    """
    # load programme details from scrapy
    data = settings.BASE_DIR / 'kuccps/programme_details.json'
    json_file = open(data)
    programmes = json.load(json_file)
    json_file.close()
    return Response(programmes)


