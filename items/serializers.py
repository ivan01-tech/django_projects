from items.models import Item
from rest_framework import serializers


class ItemsSerializer(serializers.ModelSerializer):
    fake_field = serializers.CharField(validators=[])

    class Meta:
        model = Item
        fields = ["id", "name", "done", "fake_field"]

    def get_fake_field(self, instance):
        return "{instance.name} - {instance.id}"
    def validate_name(self, value):
        if value != "John Doe":
            raise serializers.ValidationError("the name is different than John Doe")
        return value

    def validate(self, attrs):
        print("to data additional data before they get deserialized !")
        if len(attrs["name"]) < len(attrs["id"]):
            raise serializers.ValidationError(
                "id's length cannot be grather than than name's length"
            )
        return attrs

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["name_id"] = instance.name + instance.id

        return representation

    def to_internal_value(self, data):
        print("to remove some unuse data before they get serialized !")
        return super().to_internal_value(data)
