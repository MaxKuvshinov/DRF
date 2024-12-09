from users.apps import UsersConfig
from rest_framework.routers import SimpleRouter
from users.views import UserViewSet, PaymentsViewSet

app_name = UsersConfig.name

router = SimpleRouter()
router.register(r"payments", PaymentsViewSet, basename="payments")
router.register("users", UserViewSet, basename="users")

urlpatterns = [
]
