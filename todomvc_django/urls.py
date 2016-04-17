from django.conf.urls import include, url

# Import main view
from todomvc_django.views import Home

urlpatterns = [

    # Main page
    url(r'^$', Home.as_view()),

    # Include API URLs
    url(r'^api/', include('api.urls')),
]
