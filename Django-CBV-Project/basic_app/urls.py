from django.urls import path, re_path
from basic_app.views import School_List_View, School_Detail_View, SchoolCreateView, SchoolUpdateView, SchoolDeleteView
from basic_app import views

app_name = 'basic_app'

urlpatterns = [
    path('create/',views.SchoolCreateView.as_view(), name= 'create'),
    re_path(r'^(?P<pk>\d+)/$', views.School_Detail_View.as_view(), name= 'detail'),
    path('', views.School_List_View.as_view(), name= 'list'),
    re_path(r'^update/(?P<pk>\d+)/$', views.SchoolUpdateView.as_view(), name= 'update'),
    re_path(r'^delete/(?P<pk>\d+)/$', views.SchoolDeleteView.as_view(), name= 'delete')
]