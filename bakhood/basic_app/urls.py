from django.conf.urls import url
from basic_app import views

app_name = 'app'

urlpatterns = [
    url(r'^$',views.BakListView.as_view(),name='baklist'),
    url(r'^(?P<pk>\d+)/$',views.BakDetailView.as_view(),name='bakdetail'),
    url(r'^create/$',views.BakCreateView.as_view(),name='bakcreate'),
    url(r'^update/(?P<pk>\d+)/$',views.BakUpdateView.as_view(),name='bakupdate'),
    url(r'^delete/(?P<pk>\d+)/$',views.BakDeleteView.as_view(),name='bakdelete'),
    url(r'^createson/$',views.SonCreateView.as_view(),name='soncreate'),
    url(r'^updateson/(?P<pk>\d+)/$',views.SonUpdateView.as_view(),name='sonupdate'),
    url(r'^deleteson/(?P<pk>\d+)/$',views.SonDeleteView.as_view(),name='sondelete'),
    url(r'^listson/$',views.SonListView.as_view(),name='sonlist'),
    url(r'^listson/(?P<pk>\d+)/$',views.SonDetailView.as_view(),name='sondetail'),
    
    
]
