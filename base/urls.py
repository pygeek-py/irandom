from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import UserView, postadd

urlpatterns = [
	#base function 
	path('', views.listwork, name="list"),
	path('accept/', views.acceptwork, name="acceptwork"),
	path('postadd/', postadd.as_view()),
	path('acceptdel/<str:pk>/', views.acceptdel, name="acceptdel"),
	path('listaccept/', views.listaccept, name="listaccept"),
	path('listpost/', views.getallpost, name="postlists"),
	path('create-work/', views.creatework, name="creatework"),
	#authentication url 
	path('register/', views.RegisterView),
	path('login/', views.LoginView, name="login"),
	path('logout/', views.logoutview),
	path('user/', UserView.as_view()),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)