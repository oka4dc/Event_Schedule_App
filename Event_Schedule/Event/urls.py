
from django.urls import path
from .views import CreateGetEvent, DeleteRetrievedEvent, JoinEvent



urlpatterns =[
    path("createEvent_get/", CreateGetEvent.as_view(), name="create_get_Event"),
    path("join_Event/", JoinEvent.as_view(), name="join_event"),
    path("delete_retrieve_Event/<int:id>/", DeleteRetrievedEvent.as_view(), name="retrieve_delete_event"),

]