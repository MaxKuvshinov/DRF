from rest_framework.serializers import ModelSerializer
from users.models import User, Payments


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class PaymentsSerializer(ModelSerializer):
    class Meta:
        model = Payments
        fields = "__all__"


class UserDetailSerializer(ModelSerializer):
    payment_history = PaymentsSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ["id", "email", "avatar", "phone_number", "city", "payment_history",]
