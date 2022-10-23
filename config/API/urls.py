
from django.urls import path
from .views import visited_domains, visited_links
urlpatterns = [
    path('api/v1/visited_links', visited_links, name='create_obj'),
    path('api/v1/visited_domains', visited_domains),
]