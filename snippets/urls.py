from django.urls import path
from snippets.views import SnippetDetail, SnippetList, UserDetail, UserList
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("snippets/", SnippetList.as_view()),
    path("snippets/<int:pk>/", SnippetDetail.as_view()),
    path("users/", UserList.as_view()),
    path("users/<int:pk>/", UserDetail.as_view()),
]

# to allow many type of urls to be handle
urlpatterns = format_suffix_patterns(urlpatterns=urlpatterns)
