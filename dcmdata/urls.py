from django.urls import path
from . import views
#from rest_framework_simplejwt.views import TokenObtainPairview, TokenRefreshView


urlpatterns = [
    path('QueryObject',views.QueryObjectView.as_view())
]