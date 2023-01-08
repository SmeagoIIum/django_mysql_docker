from user import views as user_views
from django.urls import path, include
from rest_framework import routers

from user.views import UserListView

router = routers.DefaultRouter()


urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('', include('user.urls')),
    path('', UserListView.as_view()),
    path('register/', user_views.register, name="register")
]
