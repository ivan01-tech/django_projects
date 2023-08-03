from django.urls import path, include

# from .views import SnippetDetail, SnippetList, UserDetail, UserList
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter

# Create a router and register our viewsets with it.

router = DefaultRouter()
router.register(r"snippets", views.SnippetViewSet, basename="snippet")
router.register(r"users", views.UserViewSets, basename="user")

"""
snippet_list = SnippetViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
snippet_detail = SnippetViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
snippet_highlight = SnippetViewSet.as_view({
    'get': 'highlight'
}, renderer_classes=[renderers.StaticHTMLRenderer])
user_list = UserViewSet.as_view({
    'get': 'list'
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})
"""

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path("", include(router.urls)),
]


# urlpatterns = [
#     path("snippets/", SnippetList.as_view()),
#     path("snippets/<int:pk>/", SnippetDetail.as_view()),
#     path("users/", UserList.as_view()),
#     path("users/<int:pk>/", UserDetail.as_view()),
# ]

# # to allow many type of urls to be handle
# urlpatterns = format_suffix_patterns(urlpatterns=urlpatterns)
