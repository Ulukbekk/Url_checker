from django.urls import path
from urls.views import ListUrlsAPIView, url_add_view

urlpatterns = [
    # path('urls/add/', AddUrlAPIView.as_view()),
    path('urls/add/', url_add_view),
    path('urls/', ListUrlsAPIView.as_view()),


]