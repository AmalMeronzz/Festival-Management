from . import views
from django.urls import path
from .views import GetEventCategoriesView,GetParticipantCategory,GetEventMaster


urlpatterns = [
    path('home',views.home,name="home"),
    path('CommitteeViewEventMaster', views.view_event_master, name='CommitteeViewEventMaster'),
    path('CommitteeCreateEventScheduler',views.CreateEventScheduler.as_view(),name="CommitteeCreateEventScheduler"),
    path("CommitteeViewEventScheduler",views.view_event_scheduler,name="CommitteeViewEventScheduler"),
    path("CommitteeEditEventScheduler/<str:id>",views.EditEventScheduler.as_view(),name="CommitteeEditEventScheduler"),
    path("CommitteeDeleteEventScheduler/<str:id>",views.delete_event_scheduler,name="CommitteeDeleteEventScheduler"),
    path("CommitteeDeleteEventScheduler1/<str:id>",views.delete_event_scheduler1,name="CommitteeDeleteEventScheduler1"),
    path('get_event_categories/', GetEventCategoriesView.as_view(), name='get_event_categories'),
    path('get_participant_categories/', GetParticipantCategory.as_view(), name='get_participant_categories'),
    path('get_event_master/', GetEventMaster.as_view(), name='get_event_master'),
]
