from django.conf.urls import url
from . import views
urlpatterns = [
        url(r'^$', views.display),
        url(r'^add$', views.addbook),
        url(r'^processing$', views.processing),
        url(r'^(?P<bookid>\d+)$', views.books),
        url(r'^(?P<bookid>\d+)/update$', views.update),
        url(r'^user/(?P<userid>\d+)$', views.user),
        # url(r'^remove/(?P<itemid>\d+)$', views.removefave),
        # url(r'^favorites/(?P<itemid>\d+)$', views.addfave),
        url(r'^clear', views.clear),
]
# books