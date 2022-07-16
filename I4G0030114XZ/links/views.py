from django.shortcuts import render
from django.utils import timezone
from links.serializers import LinkSerializer
from links.models import Link
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, CreateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
import datetime


# Create your views here.
class PostListApi(ListAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer

class PostDetailApi(RetrieveAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer

class PostUpdateApi(UpdateAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer

class PostCreateApi(CreateAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer

class PostDeleteApi(DestroyAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer


class ActiveLinkView(APIView):
    """
    Returns a list of all active (publicly accessible links)
    """

    def get(self, request):
        """
        Invokdes whenever a http GET requestis made to this view
        """

        qs = Link.public.all()
        data = LinkSerializer(qs, many=True).data

        return Response(data, status=status.HTTP_200_OK)


class RecentLinkView(APIView):
    """
    Returns a list of recently active links
    """

    def get(self, request):
        """
        Invoked whenever a GET rewuwest is made to this view
        """

        seven_Days_ago = timezone.now() - datetime.timedelta(days=7)
        qs = Link.public.filter(created_date__gte=seven_Days_ago)
        data = LinkSerializer(qs, many=True).data

        return Response(data, status=status.HTTP_200_OK)
