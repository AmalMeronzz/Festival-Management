from django.shortcuts import render,redirect
from AdminMainApp.models import *
from django.views.generic.base import View
from django.shortcuts import get_object_or_404
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request,'Committee/index.html')

def view_event_master(request):
    event_master = EventMaster.objects.filter(is_active=1)
    event_info_list = []
    for event in event_master:
        festival_name = event.festival_master_header_id.festival_name if event.festival_master_header_id else None
        event_category_name = event.event_category_id.event_category_name if event.event_category_id else None
        participant_category_name = event.participant_category_id.participant_category_name if event.participant_category_id else None

        event_info_list.append({
            'Festival': festival_name,
            'EventCatgory': event_category_name,
            'Participant': participant_category_name,
            'EventName':event.event_name,
            'RegistrationFee': event.registration_fee,
            'MaxTeamSize': event.max_team_size,
            'MinTeamSize': event.min_team_size,
            'EventDescription':event.event_description,
            'id': event.id,
        })
    return render(request,'Committee/view_event_master.html',{'data':event_info_list})


class CreateEventScheduler(View):
    def get(self,request):
        festival_master = FestivalMasterHeader.objects.filter(is_active=1)
        event_master = EventMaster.objects.filter(is_active=1)
        return render(request,'Committee/EventScheduler/create.html',{'festival':festival_master,'EventMaster':event_master})

    def post(self,request):
        if request.method == 'POST':
            festival_master_header_id = request.POST['festival_master_header_id']
            event_category_id = request.POST['event_category_id']
            participant_category_id = request.POST['participant_category_id']

            event_master_id = request.POST['event_master_id']
            event_start_date = request.POST['event_start_date']
            event_end_date =  request.POST['event_end_date']

            event_id = EventMaster.objects.get(pk=event_master_id)
            try:
                event_master = EventScheduler.objects.get(event_master_id=event_id,is_active=1)
                redirect_url = reverse('CommitteeApp:CommitteeCreateEventScheduler')
                return HttpResponse(f"<script>alert('Event Scheduler already added');window.location='{redirect_url}';</script>")
            except:
                event_master = EventScheduler(
                    event_master_id = event_id,
                    event_start_date = event_start_date,
                    event_end_date = event_end_date,
                    is_active =1,
                    created_on = datetime.now(),
                    created_by = "admin"
                )
                event_master.save()
            return HttpResponse("<script>alert('Event scheduler added successfully');window.location='../ViewEventScheduler';</script>")


def view_event_scheduler(request):
    event_scheduler = EventScheduler.objects.filter(is_active=1,event_master_id__is_active=True)
    event_info_list = []
    for event in event_scheduler:
        festival_category_name = event.event_master_id.festival_master_header_id if event.event_master_id else None
        event_category_name = event.event_master_id.event_category_id if event.event_master_id else None
        participant_category_name = event.event_master_id.participant_category_id if event.event_master_id else None
        event_name = event.event_master_id.event_name if event.event_master_id else None


        event_info_list.append({
            'EventName':event_name,
            'Festival':festival_category_name,
            'Event': event_category_name,
            'Participant':participant_category_name,
            'EventStartDate': event.event_start_date,
            'EventEndDate': event.event_end_date,
            'id': event.id,
        })
    return render(request,'Committee/EventScheduler/view.html',{'data':event_info_list})

class EditEventScheduler(View):
    def get(self,request,*args,**kwargs):
        id = self.kwargs.get('id')
        event_scheduler = get_object_or_404(EventScheduler, id=id)
        event_master = event_scheduler.event_master_id  # Access the EventMaster instance directly

        festival_id = event_master.festival_master_header_id.id if event_master and event_master.festival_master_header_id else None
        festival_name = event_master.festival_master_header_id.festival_name if event_master and event_master.festival_master_header_id else None
        event_category_id = event_master.event_category_id.id if event_master and event_master.event_category_id else None
        event_category_name = event_master.event_category_id.event_category_name if event_master and event_master.event_category_id else None
        participant_category_id = event_master.participant_category_id.id if event_master and event_master.participant_category_id else None
        participant_category_name = event_master.participant_category_id.participant_category_name if event_master and event_master.participant_category_id else None
        event_master_id = event_master.id if event_master else None
        event_name = event_master.event_name if event_master else None

        event_master_info = {
            'FestivalId': festival_id,
            'Festival': festival_name,
            'EventCategoryId': event_category_id,
            'EventCategory': event_category_name,
            'ParticipantCategoryId': participant_category_id,
            'ParticipantCategory': participant_category_name,
            'EventMasterId': event_master_id,
            'EventName': event_name,
            'StartDate': event_scheduler.event_start_date,
            'EndDate': event_scheduler.event_end_date,
            'id': event_scheduler.id,
        }
        return render(request,'Committee/EventScheduler/create.html',{'data':event_master_info})

    def post(self,request,*args,**kwargs):
        id = self.kwargs.get('id')
        if request.method == "POST":
            id = self.kwargs.get('id')
            # event_master_id = request.post['event_master_id']
            event_scheduler = get_object_or_404(EventScheduler, pk=id)

            # Update committee member fields
            event_master_id = request.POST.get('event_master_id')
            event_id = get_object_or_404(EventMaster, pk=event_master_id)

            event_scheduler.event_start_date = request.POST.get('event_start_date')
            event_scheduler.event_end_date = request.POST.get('event_end_date')
            event_scheduler.save()
            return HttpResponse("<script>alert('Event Scheduler updated successfully');window.location='../../Committee/CommitteeViewEventScheduler';</script>")

def delete_event_scheduler(request,id):
    return render(request,'Committee/EventScheduler/delete.html',{'data':id})

def delete_event_scheduler1(request,id):
    EventScheduler.objects.filter(id=id).update(is_active = 0)
    return redirect('ViewEventScheduler')

class GetEventCategoriesView(View):
    def get(self, request, *args, **kwargs):
        festival_id = request.GET.get('festival_id')
        # # Fetch Event Categories based on the selected Festival ID
        # if festival_id:
        #     event_categories = EventMaster.objects.filter(festival_master_header_id=festival_id,is_active=1).values('id','event_category_id__event_category_name')
        #
        #     categories_list = list(event_categories)

       # Fetch Event Categories based on the selected Festival ID
        if festival_id:
            event_categories = EventMaster.objects.filter(
                festival_master_header_id=festival_id, is_active=1
            ).values('event_category_id', 'event_category_id__event_category_name')

            # Manually remove duplicates based on 'id'
            unique_categories = []
            seen_ids = set()

            for category in event_categories:
                category_id = category['event_category_id']
                if category_id not in seen_ids:
                    unique_categories.append(category)
                    seen_ids.add(category_id)
            return JsonResponse(unique_categories, safe=False)
        else:
            return JsonResponse([], safe=False)

class GetParticipantCategory(View):
    def get(self, request, *args, **kwargs):
        event_category_id = request.GET.get('festival_id')

        if event_category_id:
            particicpant_categories = EventMaster.objects.filter(
                event_category_id=event_category_id, is_active=1
            ).values('participant_category_id', 'participant_category_id__participant_category_name')

            # Manually remove duplicates based on 'id'
            unique_categories = []
            seen_ids = set()
            for category in particicpant_categories:
                category_id = category['participant_category_id']
                if category_id not in seen_ids:
                    unique_categories.append(category)
                    seen_ids.add(category_id)
            return JsonResponse(unique_categories, safe=False)
        else:
            return JsonResponse([], safe=False)

class GetEventMaster(View):
    def get(self, request, *args, **kwargs):
        participant_id = request.GET.get('participant_id')
        event_category_id = request.GET.get('event_category_id')

       # Fetch Event Categories based on the selected Festival ID
        if participant_id:
            event_master = EventMaster.objects.filter(
                participant_category_id=participant_id, is_active=1,event_category_id = event_category_id
            ).values('id', 'event_name')

            # Manually remove duplicates based on 'id'
            unique_categories = []
            seen_ids = set()
            for category in event_master:
                category_id = category['id']
                if category_id not in seen_ids:
                    unique_categories.append(category)
                    seen_ids.add(category_id)
            return JsonResponse(unique_categories, safe=False)
        else:
            return JsonResponse([], safe=False)
