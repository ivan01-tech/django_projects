from rest_framework.viewsets import ModelViewSet
from user_profile.models import UserProfile
from user_profile.serializers import UserProfileSerializer


# creating the user profile views using serializers
class UserProfileModelViewSet(ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
