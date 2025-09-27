from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404, redirect, render
from .models import ShortURL
from .serializers import ShortURLSerializer


class CreateShortURL(APIView):
    def post(self, request):
        serializer = ShortURLSerializer(data=request.data)
        if serializer.is_valid():
            short_url = serializer.save()
            print(short_url)
            return Response({
                "short_url": request.build_absolute_uri('/' + short_url.short_code),
                "original_url": short_url.original_url
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RedirectToURL(APIView):
    def get(self, request, short_code):
        short_url = get_object_or_404(ShortURL, short_code=short_code)
        return redirect(short_url.original_url)


def home(request):
    short_url = None
    if request.method == "POST":
        original = request.POST.get("original_url")
        if original:
            obj = ShortURL.objects.create(original_url=original)
            short_url = request.build_absolute_uri('/' + obj.short_code)
    return render(request, "shortener/index.html", {"short_url": short_url})
