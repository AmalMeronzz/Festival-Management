from django.shortcuts import render,redirect
from django.http import HttpResponse
from datetime import datetime,date
from AdminMainApp.models import *
from django.db.models import Q
from django.views.generic.base import View
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
# Create your views here.

# def Home(request):
#     return render(request,"Student/index.html")
#
# def view_festival_master(request):
#     current_date = date.today()
#     matching_data = FestivalMasterChild.objects.select_related('festival_master_header_id').filter(
#         festival_master_header_id__is_active=1
#     ).exclude(
#         Q(festival_master_header_id__to_date__lt=current_date)
#     ).values(
#         'festival_master_header_id__id',
#         'festival_master_header_id__festival_name',
#         'festival_master_header_id__from_date',
#         'festival_master_header_id__to_date',
#         'id',
#         'registration_start_date',
#         'registration_end_date'
#     )
#     return render(request, "Student/z.html", {'data': matching_data})
#
#
# class StudentRegistration(View):
#     def get(self,request):
#         current_date = date.today()
#         festival_master = FestivalMasterHeader.objects.filter(is_active=1,to_date__gte=current_date)
#         participant_type = ParticipantTypeMaster.objects.filter(is_active=1)
#         return render(request,'Student/student_registration.html',{'festival':festival_master,'ParticipantType':participant_type})
#     def post(self,request):
#         if request.method == 'POST':
#             event_master_id = request.POST['event_master_id']
#             # college_id = request.POST['college_id']
#             event_chest_no = request.POST['chest_no']
#             receipt_no = request.POST['receipt_no']
#             participant_type_id = 1
#
#             participant_name = request.POST.getlist('participant_name')
#             participant_phone = request.POST.getlist('participant_phone')
#             participant_id_no = request.POST.getlist('participant_id_no')
#             participant_id_card = request.POST.getlist('participant_id_image')
#
#         if request.method == 'POST':
#             # Assuming you have user authentication or can retrieve user details
#             current_user = request.session['AdminId']  # Fetch current user information
#
#             event_master_id = request.POST['event_master_id']
#             # college_id = request.POST.get('college_id')
#             event_chest_no = request.POST['chest_no']
#             receipt_no = request.POST['receipt_no']
#             participant_type_id = 1
#
#             print("--------------------------------------------------------------------------------------------",request.POST)
#             event_master = EventMaster.objects.get(pk = event_master_id)
#             # Create ParticipantRegistrationHeader instance with user info
#             registration_header = ParticipantRegistrationHeader.objects.create(
#                 event_master_id=event_master,
#                 # college_id=college_id,
#                 event_chest_no=event_chest_no,
#                 receipt_no=receipt_no,
#                 created_by=current_user,  # Store user who created this entry
#                 is_active = 1
#                 # Assign other fields accordingly
#             )
#
#             # Access participant details lists sent from the form
#             participant_names = request.POST.getlist('participant_name')
#             participant_phones = request.POST.getlist('participant_phone')
#             participant_id_nos = request.POST.getlist('participant_id_no')
#             participant_id_images = request.FILES.getlist('participant_id_image')
#
#             # Save participant_id_images using FileSystemStorage
#             file_urls = []
#             for participant_id_card in participant_id_images:
#                 fss = FileSystemStorage()
#                 file = fss.save(participant_id_card.name, participant_id_card)
#                 file_url = fss.url(file)
#                 file_urls.append(file_url)
#
#             # Create ParticipantRegistrationChild instances for each participant detail
#             for i in range(len(participant_names)):
#                 participant_child = ParticipantRegistrationChild.objects.create(
#                     participant_registration_header_id=registration_header,
#                     participant_name=participant_names[i],
#                     participant_phone=participant_phones[i],
#                     participant_id_no=participant_id_nos[i],
#                     participant_id_card=file_urls[i],  # Using file URLs saved previously
#                     created_by="admin"
#                     # Assign other fields accordingly
#                 )
#
#             # Process and create ParticipantRegistrationPayment instance
#             registration_fee = request.POST['registration_fee']
#             payment_type = request.POST['payment_type']
#
#             payment = ParticipantRegistrationPayment.objects.create(
#                 participant_registration_header_id=registration_header,
#                 registration_fee=registration_fee,
#                 payment_type=payment_type,
#                 payment_status=0,
#                 created_by="admin"  # Store user who created this entry
#                 # Assign other fields accordingly
#             )
#         return redirect('ViewParticipantRegistartion')
#
# class GetEventCategoriesView(View):
#     def get(self, request, *args, **kwargs):
#         print("------------------------------------------------------------------")
#         festival_id = request.GET.get('festival_id')
#         if festival_id:
#             event_categories = EventMaster.objects.filter(
#                 festival_master_header_id=festival_id, is_active=1
#             ).values('event_category_id', 'event_category_id__event_category_name')
#
#             # Manually remove duplicates based on 'id'
#             unique_categories = []
#             seen_ids = set()
#
#             for category in event_categories:
#                 category_id = category['event_category_id']
#                 if category_id not in seen_ids:
#                     unique_categories.append(category)
#                     seen_ids.add(category_id)
#             return JsonResponse(unique_categories, safe=False)
#         else:
#             return JsonResponse([], safe=False)
#
# class GetParticipantCategory(View):
#     def get(self, request, *args, **kwargs):
#         event_category_id = request.GET.get('festival_id')
#
#         if event_category_id:
#             particicpant_categories = EventMaster.objects.filter(
#                 event_category_id=event_category_id, is_active=1
#             ).values('participant_category_id', 'participant_category_id__participant_category_name')
#
#             # Manually remove duplicates based on 'id'
#             unique_categories = []
#             seen_ids = set()
#             for category in particicpant_categories:
#                 category_id = category['participant_category_id']
#                 if category_id not in seen_ids:
#                     unique_categories.append(category)
#                     seen_ids.add(category_id)
#             return JsonResponse(unique_categories, safe=False)
#         else:
#             return JsonResponse([], safe=False)
#
# class GetEventMaster(View):
#     def get(self, request, *args, **kwargs):
#         participant_id = request.GET.get('participant_id')
#         event_category_id = request.GET.get('event_category_id')
#
#        # Fetch Event Categories based on the selected Festival ID
#         if participant_id:
#             event_master = EventMaster.objects.filter(
#                 participant_category_id=participant_id, is_active=1,event_category_id = event_category_id
#             ).values('id', 'event_name')
#
#             # Manually remove duplicates based on 'id'
#             unique_categories = []
#             seen_ids = set()
#             for category in event_master:
#                 category_id = category['id']
#                 if category_id not in seen_ids:
#                     unique_categories.append(category)
#                     seen_ids.add(category_id)
#             return JsonResponse(unique_categories, safe=False)
#         else:
#             return JsonResponse([], safe=False)
#
# class GetEventMasterForParticipant(View):
#     def get(self, request, *args, **kwargs):
#         participant_id = request.GET.get('participant_id')
#         event_category_id = request.GET.get('event_category_id')
#
#         # Fetch Event Categories based on the selected Participant ID and Event Category ID
#         if participant_id and event_category_id:
#             participant_category = ParticipantCategoryMaster.objects.get(pk=participant_id)
#
#             # Filter EventMaster based on participant_category and event_category_id
#             event_master = EventMaster.objects.filter(
#                 participant_category_id=participant_id,
#                 event_category_id=event_category_id,
#                 is_active=1
#             ).values('id', 'event_name')
#
#             # If the participant type is 'Single' or 'Group', retrieve scheduled events
#             if participant_category.participant_category_name in ['Single', 'Group']:
#                 scheduled_events = EventScheduler.objects.filter(
#                     event_master_id__in=event_master.values('id'),
#                     is_active=1
#                 ).values_list('event_master_id', flat=True)
#
#                 # Filter out events that are not scheduled
#                 event_master = event_master.filter(id__in=scheduled_events)
#
#             # Manually remove duplicates based on 'id'
#             unique_categories = []
#             seen_ids = set()
#             for category in event_master:
#                 category_id = category['id']
#                 if category_id not in seen_ids:
#                     unique_categories.append(category)
#                     seen_ids.add(category_id)
#
#             return JsonResponse(unique_categories, safe=False)
#         else:
#             return JsonResponse([], safe=False)
#
# class GetRegistrationFee(View):
#     def get(self, request, *args, **kwargs):
#         event_id = request.GET.get('event_id')
#         if event_id:
#             try:
#                 event = get_object_or_404(EventMaster, id=event_id)
#                 registration_fee = event.registration_fee
#                 min_team_size = event.min_team_size
#                 max_team_size = event.max_team_size
#                 return JsonResponse({'registration_fee': registration_fee,'min_team_size': min_team_size,'max_team_size':max_team_size})
#
#             except EventMaster.DoesNotExist:
#                 return JsonResponse({'error': 'Event not found'}, status=404)
#
#             except Exception as e:
#                 return JsonResponse({'error': str(e)}, status=500)
#
#         else:
#             return JsonResponse({'error': 'Invalid event_id'}, status=400)
