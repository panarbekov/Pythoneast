from django.urls import path
from .views import *


urlpatterns = [
    path("all/", all_publications, name='all-publications'),
    path("<int:pk>", PublicationDetailView.as_view(), name='publication'),
    path("create/", create_publication, name='create-publication'),
    path("createform/", create_form, name="create-form"),
    path("createcbv/", PublicationCreateView.as_view(), name="create-cbv"),
]
