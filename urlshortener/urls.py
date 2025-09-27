from django.contrib import admin
from django.urls import path
from shortener.views import CreateShortURL, RedirectToURL, home
from django.conf import settings
from django.conf.urls.static import static
from imagetopdf.views import ImagesToPdfView, DashboardView


urlpatterns = [
    path('admin/', admin.site.urls),
    path("shortener/", home, name="url_shortener"),
    path('api/shorten/', CreateShortURL.as_view(), name='create_short'),
    path('<str:short_code>/', RedirectToURL.as_view(), name='redirect_short'),
    path('pdf/images-to-pdf/', ImagesToPdfView.as_view(), name='images_to_pdf'),
    path('', DashboardView.as_view(), name='dashboard'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
