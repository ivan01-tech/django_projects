from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from items.models import Item
from items.serializers import ItemsSerializer
from rest_framework import generics


class UpdateItemApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemsSerializer


@api_view(["POST"])
def post_item(
    request,
):
    item = request.data
    serialize = ItemsSerializer(item)

    if serialize.is_valid():
        serialize.save()
        return Response(data=serialize.data, status=status.HTTP_201_CREATED)


class DeleteAllItems(APIView):
    def delete(self, request):
        Item.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ListItems(APIView):
    def get(sefl, request):
        items = Item.objects.all()
        serializer = ItemsSerializer(items, many=True)
        if serializer.is_valid():
            return Response(data=serializer.data, status=status.HTTP_200_OK)
