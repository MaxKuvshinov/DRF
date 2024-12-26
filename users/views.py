from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, viewsets
from rest_framework.filters import OrderingFilter
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from lms.models import Course
from users.models import Payments, User
from users.serializers import (PaymentsSerializer, UserDetailSerializer,
                               UserSerializer)
from users.services import (create_price_stripe, create_product_stripe,
                            create_sessions_stripe)


class PaymentsViewSet(viewsets.ModelViewSet):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = (
        "paid_course",
        "paid_lesson",
        "payment_method",
    )
    ordering_fields = ("payment_date",)

    def create(self, request, *args, **kwargs):
        """Создает новый платеж и взаимодействует с Stripe."""
        course_id = request.data.get("course_id")
        amount = request.data.get("amount")

        if not course_id or not amount:
            return Response(
                {"error": "Amount and Course ID are required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            course = Course.objects.get(id=course_id)
        except Course.DoesNotExist:
            return Response(
                {"error": "Course not found"}, status=status.HTTP_404_NOT_FOUND
            )

        try:
            product = create_product_stripe(course)
            price = create_price_stripe(amount, product.id)
            session_id, session_url = create_sessions_stripe(price.id)

            payment = Payments.objects.create(
                user=request.user,
                payment_amount=amount,
                payment_method="Stripe",
                paid_course=course,
            )

            return Response(
                {
                    "session_id": session_id,
                    "payment_id": payment.id,
                    "url": session_url,
                },
                status=status.HTTP_201_CREATED,
            )
        except Exception as e:
            return Response(
                {"error": "An error occurred: " + str(e)},
                status=status.HTTP_400_BAD_REQUEST,
            )


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()
