from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token,refresh_jwt_token, verify_jwt_token
from soapbox.views import IndexView
from users.views import LoginView, LogoutView, UserViewSet

router = routers.SimpleRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/v1/', include(router.urls)),

    url(r'^$',  IndexView.as_view(), name='index'),

    url(r'^api/v1/auth/login/$', LoginView.as_view(), name='login'),
    url(r'^api/v1/auth/logout/$', LogoutView.as_view(), name='logout'),

    url(r'^api/v1/auth/token/', obtain_jwt_token),
    url(r'^api/v1/auth/refresh/', refresh_jwt_token),
    url(r'^api/v1/auth/verify/', verify_jwt_token),

    # url(r'^password_reset/$', views.password_reset, name='password_reset'),
    # url(r'^password_reset/done/$', views.password_reset_done, name='password_reset_done'),
    # url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    #     views.password_reset_confirm, name='password_reset_confirm'),
    # url(r'^reset/done/$', views.password_reset_complete, name='password_reset_complete'),
]