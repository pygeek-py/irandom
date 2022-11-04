from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
	path('', views.home, name="home"),
	path('yourchallenges', views.your, name="your"),
	path('explore/', views.explore, name="explore"),
	path('login/', views.signinview, name="login"),
	path('register/', views.signupview, name="register"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)