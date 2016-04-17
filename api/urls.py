from django.conf.urls import url

# Function based API views
# from api.views import task_list, task_detail

# Class based API views
from api.views import TaskList, TaskDetail

urlpatterns = [
    # Class based URLs,
    url(r'^tasks/$', TaskList.as_view(), name='task_list'),
    url(r'^tasks/(?P<pk>[0-9]+)$', TaskDetail.as_view(), name='task_detail'),
]
