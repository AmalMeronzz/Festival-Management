from django.middleware.csrf import get_token
from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponse
from AdminMainApp.models import *
from datetime import datetime,date
from django.views.generic import DetailView,ListView
from django.contrib import messages
from django.shortcuts import redirect
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from django.db import connection
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.utils import timezone
from decimal import Decimal
from django.core.serializers import serialize
from django.forms.models import model_to_dict
from django.db.models import Q
from django.urls import reverse
import razorpay
from django.conf import settings
import uuid
from django.http import HttpResponseRedirect
import random
import hmac
import hashlib
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
import requests
import json
from django.db.models import Count
from django.db.models.functions import TruncDate
from django.db.models import Sum
from itertools import groupby
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


razorpay_key_id = 'rzp_live_b4v7afItWNEooX'
razorpay_key_secret = 'hn7LUdPn03v9pD7NvogpclFV'

# razorpay_key_id = 'rzp_test_kTUx8LbK9nmHY3'
# razorpay_key_secret = 'uUuxFMuzKpPKLOFLRzveDDUa'
# Create your views here.

# @login_required(login_url='login')
def home(request):
    # menu_headers = MenuHeader.objects.filter(is_active=1)
    # return render(request,'AdminMain/Festival.html', {'menu_headers': menu_headers})
    return render(request,'AdminMain/Festival.html')

def login(request):
    if request.method == 'POST':
        loginId = request.POST['loginid'].strip()
        password = request.POST['password'].strip()
        user = UserMaster.objects.filter(login_id=loginId, login_password=password, is_active=1)
        if user.exists():
            user_type = UserMaster.objects.get(login_id=loginId,login_password = password, is_active=1).user_type_id.usertype
            print(type(user_type))
            if (user_type == "Admin"):
                request.session['AdminId'] = user_type
                return redirect(home)
            elif(user_type == "Committee"):
                request.session['CommitteeId'] = user_type
                return redirect('CommitteeApp:home')
            else:
                return HttpResponse("<script>alert('No Such User');window.location='../login';</script>")
        else:
            return HttpResponse("<script>alert('No Such User');window.location='../login';</script>")
    return render(request,'AdminMain/login.html')


# ---------------------------------------------------------User Master----------------------------------------------------

# @method_decorator(login_required, name='dispatch')
class CreateUserMaster(View):
    def get(self,request):
        user_type = UserType.objects.filter(is_active=1)
        return render(request,'AdminMain/UserMaster/user_master.html',{'data':user_type})

class CreateUserMaster1(View):
    def get(self, request):
        current_date = date.today()
        user_type = UserType.objects.filter(is_active=1)
        festival = FestivalMasterHeader.objects.filter(is_active=1,to_date__gte=current_date)
        return render(request, 'AdminMain/UserMaster/create.html', {'data': user_type, 'festival': festival})

    def post(self, request):
        if request.method == 'POST':
            login_id = request.POST.get('loginId', '').strip()
            password = request.POST.get('password', '').strip()
            user_type_id = request.POST.get('user_type_id', '')
            organizing_committee_id = request.POST.get('organizingc_ommittee_id', '')
            user_master = None
            if len(login_id) > 0 and len(password) > 0:
                user_type_ID = UserType.objects.filter(pk=user_type_id, is_active=1).first()

                try:
                    print("-----------------------------------------1")
                    UserMaster.objects.get(user_type_id = user_type_ID,login_id=login_id, login_password=password)
                    return HttpResponse("<script>alert('User master already added');window.location='../CreateUserMaster';</script>")
                except:
                    if user_type_ID.usertype == 'Admin':
                        try:
                            UserMaster.objects.get(user_type_id = user_type_ID,login_id =login_id ,login_password = password ,is_active = 1)
                            return HttpResponse("<script>alert('already added ');window.location='../CreateUserMaster';</script>")
                        except:
                            user_master = UserMaster(
                                login_id=login_id,
                                login_password=password,
                                user_type_id=user_type_ID,
                                is_active=1,
                                created_on=datetime.now(),
                                created_by="admin",
                            )
                            if user_master:
                                user_master.save()
                                return HttpResponse("<script>alert('User Master added successfully');window.location='../CreateUserMaster';</script>")
                            else:
                                return HttpResponse("<script>alert('Failed to add User Master');window.location='../CreateUserMaster1';</script>")
                    elif user_type_ID.usertype == 'Committee':
                        try:
                            organizing_committee_instance = OrganizingCommitteMaster.objects.get(pk=organizing_committee_id, is_active=1)
                            UserMaster.objects.get(organizing_committe_master_id = organizing_committee_instance,is_active = 1)
                            return HttpResponse("<script>alert('already added ');window.location='../CreateUserMaster';</script>")

                        except:
                            user_master = UserMaster(
                            organizing_committe_master_id=organizing_committee_instance,
                            login_id=login_id,
                            login_password=password,
                            user_type_id=user_type_ID,
                            is_active=1,
                            created_on=datetime.now(),
                            created_by="admin",
                            )
                            if user_master:
                                user_master.save()
                                return HttpResponse("<script>alert('User Master added successfully');window.location='../CreateUserMaster';</script>")
                            else:
                                return HttpResponse("<script>alert('Failed to add User Master');window.location='../CreateUserMaster1';</script>")
                        # if not organizing_committee_instance:
                        #     return HttpResponse("<script>alert('Invalid Organizing Committee');window.location='../CreateUserMaster';</script>")
                        #
            return HttpResponse("<script>alert('Failed to add User Master');window.location='../CreateUserMaster1';</script>")


# class CreateUserMaster1(View):
#     def get(self,request):
#         user_type = UserType.objects.filter(is_active=1)
#         festival = FestivalMasterHeader.objects.filter(is_active=1)
#         return render(request,'AdminMain/UserMaster/create.html',{'data':user_type,'festival':festival})
#     def post(self,request):
#         if request.method == 'POST':
#             login_id = request.POST['loginId'].strip()
#             password = request.POST['password'].strip()
#             user_type_id = request.POST['user_type_id']
#             organizing_committee_id = request.POST['organizingc_ommittee_id']
#
#             if len(login_id)> 0 and len(password)>0 :
#                 user_type_ID = UserType.objects.get(pk=user_type_id)
#                 user_master = None
#                 try:
#                     UserMaster.objects.get(login_id = login_id,login_password = password)
#                     print("----------------------------------------------")
#                     return HttpResponse("<script>alert('User master already added');window.location='../CreateUserMaster1'</script>")
#                 except:
#                      if user_type_ID.usertype == 'admin':
#                         user_master = UserMaster(
#                             login_id=login_id,
#                             login_password=password,
#                             user_type_id=user_type_ID,
#                             is_active=1,
#                             created_on=datetime.now(),
#                             created_by="admin",
#                         )
#                      elif user_type_ID.usertype == 'committee':
#                          try:
#                             organizing_committee_instance = OrganizingCommitteMaster.objects.get(pk=organizing_committee_id)
#                             user_master = UserMaster.objects.get(organizing_committe_master_id = organizing_committee_instance)
#                          except:
#                             user_master = UserMaster(
#                                 organizing_committe_master_id=organizing_committee_instance,
#                                 login_id=login_id,
#                                 login_password=password,
#                                 user_type_id=user_type_ID,
#                                 is_active=1,
#                                 created_on=datetime.now(),
#                                 created_by="admin",
#                             )
#                      if user_master:
#                          try:
#                              user_master.save()
#                              return HttpResponse("<script>alert('User Master added successfully');window.location='../CreateUserMaster';</script>")
#                          except:
#                              return HttpResponse("<script>alert('Failed to add User Master');</script>")
#             return HttpResponse("<script>alert('Failed to add User Master');window.location='../CreateUserMaster';</script>")


def view_user_master(request,id):
    user = UserMaster.objects.filter(user_type_id=id,is_active=1)
    return render(request,'AdminMain/UserMaster/view_user_master.html',{'data':user})

class EditUserMaster(DetailView):
    def get(self,request, *args, **kwargs):
        id = self.kwargs.get('id')
        user_master = UserMaster.objects.get(id=id)
        user_type = UserType.objects.filter(is_active=1)
        return render(request,'AdminMain/UserMaster/edit.html',{'data':user_master,'UserType':user_type})

    def post(self,request, *args, **kwargs):
        if request.method == 'POST':
            login_id = request.POST['name']
            password = request.POST['password']
            # user_type_id = request.POST['user_type_id']

            LoginId = login_id.strip()
            LoginPassword = password.strip()
            if len(login_id) > 0 and len(LoginPassword) > 0 :
                id = self.kwargs.get('id')
                # user_type_ID = UserType.objects.get(pk=user_type_id)

                UserMaster.objects.filter(id=id).update(
                    login_id= LoginId,
                    login_password = LoginPassword,
                    modified_on = datetime.now(),
                    # user_type_id = user_type_ID
                )
                return HttpResponse("<script>alert('updated successfully');window.location='../CreateUserMaster';</script>")


def delete_user_master(request,id):
    return render(request,'AdminMain/UserMaster/delete.html',{'data':id})

def delete_user_master1(request,id):
    UserMaster.objects.filter(id=id).update(is_active = 0)
    return redirect('CreateUserMaster')

class GetCommitteMember(View):
    def get(self, request, *args, **kwargs):
        festival_id = request.GET.get('festival_id')
        if festival_id:
            committe_members = OrganizingCommitteMaster.objects.filter(
                festival_master_header_id=festival_id, is_active=1, festival_master_header_id__is_active=True
            ).values('id', 'committe_member_name')

            committe_members_list = list(committe_members)

            return JsonResponse(committe_members_list, safe=False)
        else:
            return JsonResponse([], safe=False)

# ----------------------------------------------------------Department Master--------------------------------------------------------

def create_department(request):
    if request.method == 'POST':
        name = request.POST['name']
        trimmed_string = name.strip()
        if len(trimmed_string) > 0:
            try:
                department_name = DepartmentMaster.objects.get(department_name=trimmed_string, is_active=1)
                return HttpResponse("<script>alert('Department already added');window.location='../viewdepartment';</script>")
            except:
                department = DepartmentMaster(
                   department_name = trimmed_string,
                   is_active = 1,
                   created_on = datetime.now(),
                   created_by = "admin",
                )
                department.save()
                return HttpResponse("<script>alert('Department added successfully');window.location='../viewdepartment';</script>")
            # else:
            #     return HttpResponse("<script>alert('Department already added');window.location='../viewdepartment';</script>")

        else:
            return HttpResponse("<script>alert('Please avoid whitespace in starting and ending');window.location='../viewdepartment';</script>")
    return render(request,'AdminMain/DepartmentMaster/view_department.html')

def view_department(request):
    department = DepartmentMaster.objects.filter(is_active=1)
    return render(request,'AdminMain/DepartmentMaster/view_department.html',{'data': department})

def update_department(request,id):
    if request.method == 'POST':
        department_name = request.POST['name']
        trimmed_string = department_name.strip()
        if len(trimmed_string) > 0:
            try:
                department_name = DepartmentMaster.objects.get(department_name=trimmed_string, is_active=1)
                return HttpResponse("<script>alert('Department already existed');window.location='../viewdepartment';</script>")
            except:
                DepartmentMaster.objects.filter(id=id).update(department_name=trimmed_string)
                return HttpResponse("<script>alert('Department Name updated successfully');window.location='../viewdepartment';</script>")
    department = DepartmentMaster.objects.get(id=id)
    return render(request,'AdminMain/DepartmentMaster/update_department.html',{'data': department})

def delete_department(request,id):
    return render(request,'AdminMain/DepartmentMaster/delete_department.html',{'data':id})

def delete_department1(request,id):
    DepartmentMaster.objects.filter(id=id).update(is_active=0)
    return redirect('viewdepartment')

# ----------------------------------------------------------event Category--------------------------------------------------------

def Create_Event_Category(request):
    if request.method == 'POST':
        name = request.POST['name']
        trimmed_string = name.strip()
        if len(trimmed_string) > 0:
            try:
                Event_name = EventCategoryMaster.objects.get(event_category_name=trimmed_string,is_active=1)
                return HttpResponse("<script>alert('Event Category already added');window.location='../vieweventcategory';</script>")
            except:
                event = EventCategoryMaster(
                   event_category_name = trimmed_string,
                   is_active = 1,
                   created_on = datetime.now(),
                   created_by = "admin",
                )
                event.save()
                return HttpResponse("<script>alert('Event Category added successfully');window.location='../vieweventcategory';</script>")
            else:
                return HttpResponse("<script>alert('Event Category already added');window.location='../vieweventcategory';</script>")
        else:
            return HttpResponse("<script>alert('Please avoid whitespace in starting and ending');window.location='../vieweventcategory';</script>")
    return render(request,'AdminMain/EventCategory/view_department.html')

def view_event_category(request):
    event = EventCategoryMaster.objects.filter(is_active=1)
    return render(request,"AdminMain/EventCategory/event_category.html",{'data':event})

def edit_event_category(request,id):
    if request.method == 'POST':
        event_category_name = request.POST['name']
        trimmed_string = event_category_name.strip()
        if len(trimmed_string) > 0:
             try:
                Event_name = EventCategoryMaster.objects.get(event_category_name=trimmed_string,is_active=1)
                return HttpResponse("<script>alert('Event Category already existed');window.location='../vieweventcategory';</script>")
             except:
                 EventCategoryMaster.objects.filter(id=id).update(event_category_name=trimmed_string)
                 return HttpResponse("<script>alert('Event Category Name updated successfully');window.location='../vieweventcategory';</script>")
    event = EventCategoryMaster.objects.get(id=id)
    return render(request,"AdminMain/EventCategory/update_event_category.html",{'data':event})

def delete_event_category(request,id):
    return render(request,'AdminMain/EventCategory/delete.html',{'data':id})

def delete_event_category1(request,id):
    EventCategoryMaster.objects.filter(id=id).update(is_active=0)
    return redirect('vieweventcategory')
# ---------------------------------------------------UserType---------------------------------------------------

class CreateUserType(View):
    def get(self,request):
        user_type = UserType.objects.filter(is_active=1)
        return render(request,'AdminMain/UserType/user_type.html',{'data':user_type})

    def post(self, request):
        if request.method == 'POST':
            name = request.POST.get('name', '').strip()

            if name:
                existing_user_type = UserType.objects.filter(usertype=name, is_active=1)

                if existing_user_type.exists():
                    return HttpResponse("<script>alert('UserType already added');window.location='../CreateUserType';</script>")
                else:
                    try:
                        user_type = UserType(usertype=name, is_active=1)
                        user_type.save()
                        return HttpResponse("<script>alert('UserType added successfully');window.location='../CreateUserType';</script>")
                    except Exception as e:
                        # Handle exceptions here, if necessary
                        print(str(e))
                        return HttpResponse("<script>alert('Error adding UserType');window.location='../CreateUserType';</script>")
        return HttpResponse("<script>alert('Invalid data');window.location='../CreateUserType';</script>")

    # def post(self,request):
    #     if request.method == 'POST':
    #         name = request.POST['name']
    #         trimmed_string = name.strip()
    #         if len(trimmed_string) > 0:
    #             try:
    #                 user_type = UserType.objects.filter(usertype=trimmed_string, is_active=1)
    #                 print("----------------------------------------------------",user_type)
    #                 return HttpResponse("<script>alert('UserType already added');window.location='../CreateUserType';</script>")
    #             except:
    #                 user_type = UserType(
    #                    usertype = trimmed_string,
    #                    is_active = 1
    #                 )
    #                 user_type.save()
    #                 return HttpResponse("<script>alert('UserType added successfully');window.location='../CreateUserType';</script>")

class EditUserType(DetailView):
    def get(self, request, *args, **kwargs):
        id = self.kwargs.get('id')
        user_type = UserType.objects.get(id=id)
        return render(request,'AdminMain/UserType/edit_user_type.html',{'data':user_type})

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            name = request.POST['name']
            trimmed_string = name.strip()
            if len(trimmed_string) > 0:
                id = self.kwargs.get('id')
                UserType.objects.filter(id=id).update(usertype=trimmed_string)
                return HttpResponse("<script>alert('UserType Name updated successfully');window.location='../CreateUserType';</script>")

class DeleteUserType(DetailView):
    def get(self, request, *args, **kwargs):
        id = self.kwargs.get('id')
        return render(request,'AdminMain/UserType/delete_user_type.html',{'data':id})

def DeleteUserType1(request,id):
    UserType.objects.filter(id=id).update(is_active=0)
    return redirect('CreateUserType')
# ------------------------------------------------ Committe Member Type Master--------------------------------------------
class CreateCommitteMasterType(View):
    def get(self,request):
        Committee_type = CommitteMemberTypeMaster.objects.filter(is_active=1)
        return render(request,'AdminMain/CommitteeMaster/committee_master_type.html',{'data':Committee_type})
    def post(self,request):
        if request.method == 'POST':
            name = request.POST['name']
            trimmed_string = name.strip()
            if len(trimmed_string) > 0:
                existing_committe = CommitteMemberTypeMaster.objects.filter(committe_member_type=trimmed_string, is_active=1)
                if existing_committe.exists():
                    return HttpResponse("<script>alert('Committe member type already added');window.location='../CreateCommitteMasterType';</script>")
                else:
                    try:
                        committe = CommitteMemberTypeMaster(
                            committe_member_type=trimmed_string,
                            is_active=1,
                            created_on=datetime.now(),
                            created_by="admin"
                        )
                        committe.save()
                        return HttpResponse("<script>alert('Committe member type added successfully');window.location='../CreateCommitteMasterType';</script>")
                    except Exception as e:
                        print(e)  # Print the exception for debugging purposes
                        return HttpResponse("<script>alert('Error occurred while adding Committe member type');window.location='../CreateCommitteMasterType';</script>")
            else:
                return HttpResponse("<script>alert('Please avoid whitespace in starting and ending');window.location='../CreateCommitteMasterType';</script>")

        # if request.method == 'POST':
        #     name = request.POST['name']
        #     trimmed_string = name.strip()
        #     if len(trimmed_string) > 0:
        #         try:
        #             CommitteMemberTypeMaster.objects.filter(committe_member_type=trimmed_string,is_active=1)
        #             return HttpResponse("<script>alert('already added Committe member type');window.location='../CreateCommitteMasterType';</script>")
        #         except:
        #             committe = CommitteMemberTypeMaster(
        #                committe_member_type = trimmed_string,
        #                is_active = 1,
        #                created_on = datetime.now(),
        #                created_by = "admin"
        #             )
        #             committe.save()
        #             return HttpResponse("<script>alert('Committe member type added successfully');window.location='../CreateCommitteMasterType';</script>")
        # else:
        #     return HttpResponse("<script>alert('Please avoid whitespace in starting and ending');window.location='../CreateCommitteMasterType';</script>")

def edit_committe_master_type(request,id):
    if request.method == 'POST':
        name = request.POST['name']
        trimmed_string = name.strip()
        if len(trimmed_string) > 0:
            CommitteMemberTypeMaster.objects.filter(id=id).update(committe_member_type=trimmed_string)
            return HttpResponse("<script>alert('Committe type updated successfully');window.location='../CreateCommitteMasterType';</script>")
    else:
        committe_type = CommitteMemberTypeMaster.objects.get(id=id)
        return render(request,'AdminMain/CommitteeMaster/edit_committe_master_type.html',{'data':committe_type})

def delete_committe_master_type(request,id):
    return render(request,'AdminMain/CommitteeMaster/delete_committe_master_type.html',{'data':id})

def delete_committe_master_type1(request,id):
    CommitteMemberTypeMaster.objects.filter(id=id).update(is_active=0)
    return redirect('CreateCommitteMasterType')

# --------------------------------------------------Institution Master--------------------------------------------

class CreateInstitution(View):
    def get(self,request):
        return render(request,'AdminMain/InstitutionMaster/create_institution_master.html')
    def post(self,request):
        if request.method == 'POST':
            institution_name = request.POST['institution_name']
            institution_address = request.POST['institution_address']
            institution_phone_no = request.POST['institution_phone_no']
            institution_icon = request.FILES['institution_icon']
            institution_banner = request.FILES['institution_banner']
            fss = FileSystemStorage()
            file = fss.save(institution_icon.name, institution_icon)
            file_url = fss.url(file)
            file1 = fss.save(institution_banner.name, institution_banner)
            file_url1 = fss.url(file1)
            created_on = datetime.now()

            institution_name = institution_name.strip()
            institution_address = institution_address.strip()
            if len(institution_name) > 0 and len(institution_address) > 0:
                institution = InstitutionMaster(
                    institution_name = institution_name,
                    institution_address = institution_address,
                    institution_phone_no = institution_phone_no,
                    institution_icon = institution_icon,
                    institution_banner = institution_banner,
                    is_active = 1,
                    created_on = created_on,
                    # created_by = "admin"
                )
                institution.save()
                return HttpResponse("<script>alert('Institution Added successfully');window.location='../ViewInstitution';</script>")

def view_institution(request):
    institution = InstitutionMaster.objects.filter(is_active=1)
    return render(request,'AdminMain/InstitutionMaster/institution_master.html',{'data':institution})

class EditInstitution(DetailView):
    def get(self,request, *args, **kwargs):
        id = self.kwargs.get('id')
        institution = InstitutionMaster.objects.get(id=id)
        return render(request,'AdminMain/InstitutionMaster/create_institution_master.html',{'data':institution})

    def post(self,request, *args, **kwargs):
        if request.method == 'POST':
            name = request.POST['name']
            id = self.kwargs.get('id')
            return 0

def delete_institution(request,id):
    institutionId = id
    return render(request,'AdminMain/InstitutionMaster/delete_institution.html',{'data':institutionId})

def delete_institution1(request,id):
    InstitutionMaster.objects.filter(id=id).update(is_active = 0)
    return redirect('ViewInstitution')

# ----------------------------------------------------------Participant Category Master -----------------------------------

def view_participant_category(request):
    category = ParticipantCategoryMaster.objects.filter(is_active=1)
    return render(request,'AdminMain/ParticipantCategoryMaster/view.html',{'data':category})

def create_participant_category(request):
    if request.method == 'POST':
        name = request.POST['name']
        trimmed_string = name.strip()
        if len(trimmed_string) > 0:
            existing_category = ParticipantCategoryMaster.objects.filter(participant_category_name=trimmed_string, is_active=1)
            if existing_category.exists():
                return HttpResponse("<script>alert('Participant Category already added');window.location='../ParticipantCategoryMaster';</script>")
            else:
                try:
                    participant_category = ParticipantCategoryMaster(
                        participant_category_name=trimmed_string,
                        is_active=1,
                        created_on=datetime.now(),
                        created_by="admin"
                    )
                    participant_category.save()
                    return HttpResponse("<script>alert('Participant category Added successfully');window.location='../ParticipantCategoryMaster';</script>")
                except Exception as e:
                    print(e)  # Print the exception for debugging purposes
                    return HttpResponse("<script>alert('Error occurred while adding participant category');window.location='../ParticipantCategoryMaster';</script>")

    return HttpResponse("<script>alert('error');window.location='../ParticipantCategoryMaster';</script>")

    # if request.method == 'POST':
    #     name = request.POST['name']
    #     trimmed_string = name.strip()
    #     if len(trimmed_string) > 0:
    #          try:
    #             department_name = ParticipantCategoryMaster.objects.filter(participant_category_name=trimmed_string, is_active=1)
    #             return HttpResponse("<script>alert('Participant Category already added');window.location='../ParticipantCategoryMaster';</script>")
    #          except:
    #              participant_category = ParticipantCategoryMaster(
    #                 participant_category_name = trimmed_string,
    #                 is_active = 1,
    #                 created_on = datetime.now(),
    #                 created_by = "admin"
    #              )
    #              participant_category.save()
    #              return HttpResponse("<script>alert('Participant category Added successfully');window.location='../ParticipantCategoryMaster';</script>")
    #
    # return HttpResponse("<script>alert('error');window.location='../ParticipantCategoryMaster';</script>")

class EditParticipantCategory(DetailView):
    def get(self,request, *args, **kwargs):
        id = self.kwargs.get('id')
        category = ParticipantCategoryMaster.objects.get(id=id)
        return render(request,'AdminMain/ParticipantCategoryMaster/Edit.html',{'data':category})
    def post(self,request,*args,**kwargs):
        id = self.kwargs.get('id')
        name = request.POST['name']
        trimmed_string = name.strip()
        if len(trimmed_string) > 0:
            ParticipantCategoryMaster.objects.filter(id=id).update(
                participant_category_name = trimmed_string,
                modified_on = datetime.now(),
            )
            return redirect('ParticipantCategoryMaster')

def delete_participant_category(request,id):
    Id = id
    return render(request,'AdminMain/ParticipantCategoryMaster/delete.html',{'data':Id})

def delete_participant_category1(request,id):
    Id = id
    ParticipantCategoryMaster.objects.filter(id=id).update(is_active = 0)
    return redirect('ParticipantCategoryMaster')
#----------------------------------------------------Participant Type Master------------------------------------------

class ViewParticipantTypeMaster(View):
    def get(self,request):
        participant = ParticipantTypeMaster.objects.filter(is_active = 1)
        return render(request,'AdminMain/ParticipantTypeMaster/view.html',{'data':participant})

    def post(self,request):
        if request.method == 'POST':
            name = request.POST['name']
            trimmed_string = name.strip()
            if len(name) > 0:
                try:
                    participant_type = ParticipantTypeMaster.objects.get(participant_type=name,is_active=1)
                    return HttpResponse("<script>alert('Participant type already added');window.location='../ViewParticipantTypeMaster';</script>")
                except:
                    participant = ParticipantTypeMaster(
                        participant_type = name,
                        is_active = 1,
                        created_on = datetime.now(),
                        created_by = "admin"
                    )
                    participant.save()
                    return HttpResponse("<script>alert('Participant type Added successfully');window.location='../ViewParticipantTypeMaster';</script>")

class EditParticipantType(DetailView):
    def get(self,request, *args, **kwargs):
        id = self.kwargs.get('id')
        participant = ParticipantTypeMaster.objects.get(id=id)
        return render(request,'AdminMain/ParticipantTypeMaster/Edit.html',{'data':participant})
    def post(self,request,*args,**kwargs):
        id = self.kwargs.get('id')
        name = request.POST['name']
        trimmed_string = name.strip()
        if len(trimmed_string) > 0:
            ParticipantTypeMaster.objects.filter(id=id).update(
                participant_type = trimmed_string,
                modified_on = datetime.now(),
            )
            return redirect('ViewParticipantTypeMaster')

def delete_participant_type(request,id):
    Id = id
    return render(request,'AdminMain/ParticipantTypeMaster/delete.html',{'data':Id})

def delete_participant_type1(request,id):
    Id = id
    ParticipantTypeMaster.objects.filter(id=id).update(is_active = 0)
    return redirect('ViewParticipantTypeMaster')


# ---------------------------------------------------Winner Position--------------------------------------------------

def view_winner_position(request):
        winner = WinnerPositionMasterModel.objects.filter(is_active=1)
        return render(request,'AdminMain/WinnerPosition/view.html',{'data':winner})

# class WinnerPositionMaster(View):
#     def post(self,request):
#         if request.method == 'POST':
#             name = request.POST['name']
#             trimmed_string = name.strip()
#             if len(trimmed_string) > 0:
#                 try:
#                     WinnerPositionMasterModel.objects.filter(winner_position=trimmed_string,is_active=1)
#                     return HttpResponse("<script>alert('Winner position already Added');window.location='../ViewWinnerPosition';</script>")
#                 except:
#                     winner = WinnerPositionMasterModel(
#                         winner_position = trimmed_string,
#                         is_active = 1,
#                         created_on = datetime.now(),
#                         created_by = "admin"
#                     )
#                     winner.save()
#                     return HttpResponse("<script>alert('Winner position Added successfully');window.location='../ViewWinnerPosition';</script>")

class WinnerPositionMaster(View):
    def post(self, request):
        if request.method == 'POST':
            name = request.POST.get('name', '').strip()

            if name:
                try:
                    winner_position, created = WinnerPositionMasterModel.objects.get_or_create(
                        winner_position=name,
                        is_active=1,
                        defaults={
                            'created_on': datetime.now(),
                            'created_by': 'admin'
                        }
                    )

                    if not created:
                        return HttpResponse("<script>alert('Winner position already added');window.location='../ViewWinnerPosition';</script>")
                    else:
                        return HttpResponse("<script>alert('Winner position added successfully');window.location='../ViewWinnerPosition';</script>")
                except Exception as e:
                    # Handle exceptions here, if necessary
                    print(str(e))
                    return HttpResponse("<script>alert('Error adding winner position');window.location='../ViewWinnerPosition';</script>")
        # Redirect to the page where you came from in case of a GET request or invalid data
        return HttpResponseRedirect(reverse('ViewWinnerPosition'))

class EditWinnerPosition(DetailView):
    def get(self,request, *args, **kwargs):
        id = self.kwargs.get('id')
        category = WinnerPositionMasterModel.objects.get(id=id)
        return render(request,'AdminMain/WinnerPosition/edit.html',{'data':category})
    def post(self,request,*args,**kwargs):
        id = self.kwargs.get('id')
        name = request.POST['name']
        trimmed_string = name.strip()
        if len(trimmed_string) > 0:
            WinnerPositionMasterModel.objects.filter(id=id).update(
                winner_position=trimmed_string,
                modified_on=datetime.now(),
            )
            return redirect('ViewWinnerPosition')

def delete_winner_position(request,id):
    Id = id
    return render(request,'AdminMain/WinnerPosition/delete.html',{'data':Id})

def delete_winner_position1(request,id):
    Id = id
    WinnerPositionMasterModel.objects.filter(id=id).update(is_active = 0)
    return redirect('ViewWinnerPosition')

# ---------------------------------------------------Prize Type Master--------------------------------------------------

class ViewPrizeTypeMaster(View):
    def get(self,request):
        prize = PrizeTypeMasterModel.objects.filter(is_active = 1)
        return render(request,'AdminMain/PrizeTypeMaster/view.html',{'data':prize})
    def post(self,request):
        if request.method == 'POST':
            name = request.POST['name']
            trimmed_string = name.strip()
            if len(trimmed_string) > 0:
                try:
                    event_master = PrizeTypeMasterModel.objects.get(prize_type=trimmed_string,is_active=1)
                    return HttpResponse("<script>alert('Prize type already added');window.location='../ViewPrizeTypeMaster';</script>")
                except:
                    prize = PrizeTypeMasterModel(
                        prize_type = trimmed_string,
                        is_active = 1,
                        created_on = datetime.now(),
                        created_by = "admin"
                    )
                    prize.save()
                    return HttpResponse("<script>alert('Prize type Added successfully');window.location='../ViewPrizeTypeMaster';</script>")

class EditPrizeType(DetailView):
    def get(self,request, *args, **kwargs):
        id = self.kwargs.get('id')
        prize = PrizeTypeMasterModel.objects.get(id=id)
        return render(request,'AdminMain/PrizeTypeMaster/edit.html',{'data':prize})
    def post(self,request,*args,**kwargs):
        id = self.kwargs.get('id')
        name = request.POST['name']
        trimmed_string = name.strip()
        if len(trimmed_string) > 0:
            PrizeTypeMasterModel.objects.filter(id=id).update(
                prize_type = trimmed_string,
                modified_on = datetime.now(),
            )
            return redirect('ViewPrizeTypeMaster')

def delete_prize_type(request,id):
    Id = id
    return render(request,'AdminMain/PrizeTypeMaster/delete.html',{'data':Id})

def delete_prize_type1(request,id):
    Id = id
    PrizeTypeMasterModel.objects.filter(id=id).update(is_active = 0)
    return redirect('ViewPrizeTypeMaster')

#----------------------------------------------------Sponsor Master------------------------------------------

class ViewSponsorMaster(View):
    def get(self,request):
        current_date = date.today()
        sponsor = SponsorMaster.objects.filter(is_active = 1,festival_master_header_id__is_active=1,festival_master_header_id__to_date__gte=current_date)
        festival_master = FestivalMasterHeader.objects.filter(is_active=1, to_date__gte=current_date)
        return render(request,'AdminMain/SponsorMaster/view.html',{'data':sponsor,'festival':festival_master})
    def post(self,request):
        if request.method == 'POST':
            festival_id = request.POST['festival_master_header_id']
            event_id = request.POST['event_master_id']
            sponsor_type = request.POST['sponsor_type']
            name = request.POST['name']
            logo = request.FILES['logo']
            fss = FileSystemStorage()
            file = fss.save(logo.name, logo)
            file_url = fss.url(file)
            trimmed_string = name.strip()

            festival_Id = FestivalMasterHeader.objects.get(pk=festival_id)

            if event_id:
                event_Id = EventMaster.objects.get(pk=event_id)
            else:
                event_Id = None

            if len(trimmed_string) > 0:
                try:
                    SponsorMaster.objects.get(sponsor_name=trimmed_string,sponsor_type=sponsor_type,event_master_id=event_Id,is_active=1)
                    return HttpResponse("<script>alert('Sponsor already Added');window.location='../ViewSponsorMaster';</script>")
                except:
                    if event_Id:
                        sponsor = SponsorMaster(
                            festival_master_header_id = festival_Id,
                            sponsor_type = sponsor_type,
                            event_master_id = event_Id,
                            sponsor_name = trimmed_string,
                            sponsor_logo = logo,
                            is_active = 1,
                            created_on = datetime.now(),
                            created_by = "admin"
                        )
                    else:
                        sponsor = SponsorMaster(
                            festival_master_header_id=festival_Id,
                            sponsor_type=sponsor_type,
                            sponsor_name=trimmed_string,
                            sponsor_logo=logo,
                            is_active=1,
                            created_on=datetime.now(),
                            created_by="admin"
                        )
                    sponsor.save()
                    return HttpResponse("<script>alert('Sponsor Added successfully');window.location='../ViewSponsorMaster';</script>")

class EditSponsorMaster(DetailView):
    def get(self,request, *args, **kwargs):
        id = self.kwargs.get('id')
        current_date = date.today()

        sponsor = SponsorMaster.objects.get(id=id)
        FestivalId =sponsor.festival_master_header_id.id
        Festival = sponsor.festival_master_header_id.festival_name
        sponsor_type = sponsor.sponsor_type
        Sponsor = sponsor.sponsor_name
        Image = sponsor.sponsor_logo
        Id = sponsor.id

        EventMasterId =sponsor.event_master_id

        festival_master_header = FestivalMasterHeader.objects.filter(is_active=1, to_date__gte=current_date)
        if EventMasterId == None:
            return render(request,'AdminMain/SponsorMaster/edit.html',{
                'FestivalId':FestivalId,
                'Festival':Festival,
                'Sponsor':Sponsor,
                'sponsor_type':sponsor_type,
                'Image':Image,
                'Id':Id,
                'festival':festival_master_header
            })
        else:
            event_id = EventMasterId.id
            EventName = EventMasterId.event_name
            return render(request,'AdminMain/SponsorMaster/edit.html',{
                'FestivalId':FestivalId,
                'Festival':Festival,
                'EventMasterId':event_id,
                'EventName':EventName,
                'Sponsor':Sponsor,
                'sponsor_type':sponsor_type,
                'Image':Image,
                'Id':Id,
                'festival':festival_master_header
            })

    def post(self,request,*args,**kwargs):
        id = self.kwargs.get('id')
        sponsor = SponsorMaster.objects.get(id=id)
        festival_id = request.POST['festival_master_header_id']
        event_id = request.POST['event_master_id']
        sponsor_type = request.POST['sponsor_type']
        name = request.POST['name']
        logo = request.FILES.get('logo')  # Using get to handle the case when logo is not provided

        # Existing sponsor details
        sponsor.festival_master_header_id = FestivalMasterHeader.objects.get(pk=festival_id)
        sponsor.sponsor_type = sponsor_type
        sponsor.sponsor_name = name

        # Check if event_id is provided
        if event_id:
            sponsor.event_master_id = EventMaster.objects.get(pk=event_id)
        else:
            sponsor.event_master_id = None

        # Check if a new logo is provided
        if logo:
            fss = FileSystemStorage()
            file = fss.save(logo.name, logo)
            file_url = fss.url(file)
            sponsor.sponsor_logo = logo

        try:
            # Save the updated sponsor details
            sponsor.save()
            return HttpResponse("<script>alert('Sponsor updated successfully');window.location='../ViewSponsorMaster';</script>")
        except:
            return HttpResponse("<script>alert('Failed to update sponsor');window.location='../ViewSponsorMaster';</script>")
        # id = self.kwargs.get('id')
        # name = request.POST['name']
        # logo = request.FILES.get('logo')
        #
        # trimmed_string = name.strip()
        # if len(trimmed_string) > 0:
        #     sponsor = SponsorMaster.objects.get(id=id)
        #     if logo:  # Check if logo file is provided
        #         fss = FileSystemStorage()
        #         file = fss.save(logo.name, logo)
        #         file_url = fss.url(file)
        #         sponsor.sponsor_logo = logo  # Update logo only if a new file is provided
        #
        #     sponsor.sponsor_name = trimmed_string
        #     sponsor.save()
        #     return redirect('ViewSponsorMaster')

def delete_sponsor_master(request,id):
    Id = id
    return render(request,'AdminMain/SponsorMaster/delete.html',{'data':Id})

def delete_sponsor_master1(request,id):
    SponsorMaster.objects.filter(id=id).update(is_active = 0)
    return redirect('ViewSponsorMaster')

class get_festival_event(View):
    def get(self, request, *args, **kwargs):
        if request.method == 'GET':
            festival_id = request.GET.get('festival_id')
            event_master = EventMaster.objects.filter(
                festival_master_header_id=festival_id,
                is_active=1
            ).values('id', 'event_name')
            return JsonResponse(list(event_master), safe=False)
        else:
            return JsonResponse({'error': 'Invalid request method'})


# -----------------------------------------------------Festival Master---------------------------------------------

class CreateFestivalMaster(View):
    def get(self,request):
        return render(request,"AdminMain/FestivalMaster/create.html")
    def post(self,request):
        if request.method == 'POST':
            festival_name = request.POST['festival_name']
            festival_icon = request.FILES['festival_icon']
            festival_banner = request.FILES['festival_banner']
            video_file = request.FILES.get('video_file')
            from_date = request.POST['from_date']
            from_date_obj = datetime.fromisoformat(from_date)
            to_date = request.POST['to_date']
            to_date_obj = datetime.fromisoformat(to_date)
            registration_start_date = request.POST['registration_start_date']
            registration_start_obj = datetime.fromisoformat(registration_start_date)
            registration_end_date = request.POST['registration_end_date']
            registration_end_obj = datetime.fromisoformat(registration_end_date)
            fss = FileSystemStorage()
            file = fss.save(festival_icon.name, festival_icon)
            file_url = fss.url(file)
            fss = FileSystemStorage()
            file1 = fss.save(festival_banner.name, festival_banner)
            file_url1 = fss.url(file1)

            trimmed_string = festival_name.strip()

            current_date = date.today()

            if len(trimmed_string) > 0:
                festival_exists = FestivalMasterHeader.objects.filter(festival_name=trimmed_string, is_active=1,to_date__lt=current_date).exists()
                if festival_exists:
                    return HttpResponse("<script>alert('Already added the festival');window.location='../CreateFestivalMaster';</script>")
                else:
                    try:
                        festival_header = FestivalMasterHeader(
                            festival_name=trimmed_string,
                            festival_icon=festival_icon,
                            festival_banner=festival_banner,
                            # video_file = video_file,
                            from_date=from_date_obj,
                            to_date=to_date_obj,
                            is_active=1,
                            created_on=datetime.now(),
                            created_by="admin"
                        )
                        if video_file:
                            fss2 = FileSystemStorage()
                            file = fss2.save(video_file.name, video_file)
                            file_url1 = fss2.url(file)
                            festival_header.video_file = video_file

                        festival_header.save()
                        festival_header_id = festival_header.id
                        festival_header_ID = FestivalMasterHeader.objects.get(pk=festival_header_id)

                        festival_child = FestivalMasterChild(
                            festival_master_header_id=festival_header_ID,
                            registration_start_date=registration_start_obj,
                            registration_end_date=registration_end_obj,
                            is_active=1,
                            created_on=datetime.now(),
                            created_by="admin",
                        )
                        festival_child.save()
                        return HttpResponse("<script>alert('Festival Added successfully');window.location='../ViewFestivalMaster';</script>")
                    except Exception as e:
                        print(e)  # Print the exception for debugging purposes
                        return HttpResponse("<script>alert('Error occurred while adding festival');window.location='../CreateFestivalMaster';</script>")

            # if len(trimmed_string) > 0:
            #     try:
            #         FestivalMasterHeader.objects.filter(festival_name=trimmed_string,is_active=1)
            #         return HttpResponse("<script>alert('already added the festival');window.location='../CreateFestivalMaster';</script>")
            #     except:
            #         festival_header = FestivalMasterHeader(
            #             festival_name = trimmed_string,
            #             festival_icon = festival_icon,
            #             festival_banner = festival_banner,
            #             from_date = from_date_obj,
            #             to_date = to_date_obj,
            #             is_active =1,
            #             created_on = datetime.now(),
            #             created_by = "admin"
            #         )
            #         festival_header.save()
            #         festival_header_id = festival_header.id
            #         festival_header_ID = FestivalMasterHeader.objects.get(pk=festival_header_id)
            #
            #         festival_child = FestivalMasterChild(
            #             festival_master_header_id = festival_header_ID,
            #             registration_start_date = registration_start_obj,
            #             registration_end_date = registration_end_obj,
            #             is_active = 1,
            #             created_on = datetime.now(),
            #             created_by = "admin",
            #         )
            #         festival_child.save()
            #         return HttpResponse("<script>alert('Festival Added successfully');window.location='../ViewFestivalMaster';</script>")

def view_festival_master(request):
    current_date = date.today()
    matching_data = FestivalMasterChild.objects.select_related('festival_master_header_id').filter(
        festival_master_header_id__is_active=1
        ).exclude(
        Q(festival_master_header_id__to_date__lt=current_date)
        ).values(
        'festival_master_header_id__id',
        'festival_master_header_id__festival_name',
        'festival_master_header_id__festival_icon',
        'festival_master_header_id__festival_banner',
        'festival_master_header_id__from_date',
        'festival_master_header_id__to_date',
        'festival_master_header_id__video_file',
        'id',
        'registration_start_date',
        'registration_end_date'
    )
    return render(request, "AdminMain/FestivalMaster/view.html", {'data': matching_data})

class EditFestivalMaster(DetailView):
    def get(self,request, *args, **kwargs):
        id = self.kwargs.get('id')

        matching_data = FestivalMasterChild.objects.filter(festival_master_header_id=id).select_related(
            'id').values(
            'festival_master_header_id__id',
            'festival_master_header_id__festival_name',
            'festival_master_header_id__festival_icon',
            'festival_master_header_id__festival_banner',
            'festival_master_header_id__from_date',
            'festival_master_header_id__to_date',
            'id',
            'registration_start_date',
            'registration_end_date'
        )
        return render(request,'AdminMain/FestivalMaster/edit.html',{'data':matching_data})

    def post(self,request,*args,**kwargs):
        id = self.kwargs.get('id')
        # name = request.POST['name']
        # logo = request.FILES['logo']
        # banner = request.FILES['banner']
        # start_date = request.POST['start_date']
        # end_date = request.POST['end_date']
        # registartion_start_date = request.POST['end_date']
        # registartion_end_date = request.POST['end_date']
        #
        # fss = FileSystemStorage()
        # file = fss.save(logo.name, logo)
        # file_url = fss.url(file)
        # file1 = fss.save(banner.name, banner)
        # file_url1 = fss.url(file1)
        # trimmed_string = name.strip()
        # if len(trimmed_string) > 0:
        #     SponsorMaster.objects.filter(id=id).update(
        #         sponsor_name = trimmed_string,
        #         sponsor_logo = logo,
        #     )
        #     return redirect('ViewSponsorMaster')
         # Get FestivalMasterHeader instance
        festival_header = get_object_or_404(FestivalMasterHeader, pk=id)

        logo = request.FILES.get('festival_icon')
        banner = request.FILES.get('festival_banner')
        video_file = request.FILES.get('video_file')

        if logo is not None:
            fss = FileSystemStorage()
            file = fss.save(logo.name, logo)
            file_url = fss.url(file)
        else:
           logo = festival_header.festival_icon  # If logo is not provided, use the existing value

        if banner is not None:
            fss = FileSystemStorage()
            file1 = fss.save(banner.name, banner)
            file_url1 = fss.url(file1)
        else:
            banner = festival_header.festival_banner  # If banner is not provided, use the existing value

        if video_file is not None:
            fss = FileSystemStorage()
            file = fss.save(video_file.name, video_file)
            file_url = fss.url(file)
        else:
            video_file = festival_header.video_file

        # Update FestivalMasterHeader fields
        festival_header.festival_name = request.POST.get('festival_name')
        festival_header.from_date = request.POST.get('from_date')
        festival_header.to_date = request.POST.get('to_date')
        festival_header.festival_icon = logo
        festival_header.festival_banner = banner
        festival_header.video_file = video_file
        # Update other fields as needed

        # Save FestivalMasterHeader changes
        festival_header.save()

        # Get FestivalMasterChild instance related to FestivalMasterHeader
        festival_child = get_object_or_404(FestivalMasterChild, festival_master_header_id=festival_header)

        # Update FestivalMasterChild fields
        festival_child.registration_start_date = request.POST.get('registration_start_date')
        festival_child.registration_end_date = request.POST.get('registration_end_date')
        # Update other fields as needed

        # Save FestivalMasterChild changes
        festival_child.save()
        alert_message = f"Updated successfully: {festival_header.festival_name}"
        return HttpResponse(f"<script>alert('{alert_message}');window.location='../ViewFestivalMaster';</script>")

def delete_festival_master(request,id):
    return render(request,'AdminMain/FestivalMaster/delete.html',{'data':id})

def delete_festival_master1(request,id):
    festival_header = get_object_or_404(FestivalMasterHeader, pk=id)
    festival_header.is_active = 0
    festival_header.save()
    return redirect('ViewFestivalMaster')

# ----------------------------------------------------------Organizing Committe Master--------------------------------------

class CreateOrganizingCommitte(View):
    def get(self,request):
        current_date = date.today()
        festival_master_header = FestivalMasterHeader.objects.filter(is_active=1, to_date__gte=current_date)
        Department = DepartmentMaster.objects.filter(is_active=1)
        committe_type = CommitteMemberTypeMaster.objects.filter(is_active=1)
        return render(request,'AdminMain/OrganizingCommitte/organizing_committee_create.html',{'FestivalMaster':festival_master_header,'Department':Department,'CommitteType':committe_type})

    def post(self,request):
        if request.method == 'POST':
            festival_master_header_id = request.POST['festival_master_header_id']
            department_master_id = request.POST['department_master_id']
            committe_member_type_id = request.POST['committe_member_type_id']

            committe_member_name = request.POST['committe_member_name']
            committe_member_phone =  request.POST['committe_member_phone']
            committe_member_photo = request.FILES['committe_member_photo']

            if OrganizingCommitteMaster.objects.filter(committe_member_phone=committe_member_phone,is_active=1).exists():
                # Show alert message that the phone number is already existed
                return HttpResponse("<script>alert('Error: The phone number is already in use.');window.location='../ViewOrganizingCommitte';</script>")

            fss = FileSystemStorage()
            file = fss.save(committe_member_photo.name, committe_member_photo)
            file_url = fss.url(file)

            trimmed_string = committe_member_name.strip()

            if len(trimmed_string) > 0:

                 # user_type_ID = UserType.objects.get(pk=user_type_id)
                festival_id = FestivalMasterHeader.objects.get(pk=festival_master_header_id)
                department_id = DepartmentMaster.objects.get(pk=department_master_id)
                committe_id = CommitteMemberTypeMaster.objects.get(pk=committe_member_type_id)

                organizing_committe = OrganizingCommitteMaster(
                    festival_master_header_id = festival_id,
                    department_master_id = department_id,
                    committe_member_type_id = committe_id,
                    committe_member_name = trimmed_string,
                    committe_member_phone = committe_member_phone,
                    committe_member_photo = committe_member_photo,
                    is_active =1,
                    created_on = datetime.now(),
                    created_by = "admin"
                )
                organizing_committe.save()
                return HttpResponse("<script>alert('Organizing committe member  Added successfully');window.location='../ViewOrganizingCommitte';</script>")


def view_organizing_committe(request):
    current_date = date.today()
    committee_members = OrganizingCommitteMaster.objects.filter(
        is_active=1,
        festival_master_header_id__is_active=True,
        department_master_id__is_active=True,
        committe_member_type_id__is_active=True,
    ).exclude(
    Q(festival_master_header_id__to_date__lt=current_date)
    )
    committee_info_list = []
    for member in committee_members:
        department_name = member.department_master_id.department_name if member.department_master_id else None
        festival_name = member.festival_master_header_id.festival_name if member.festival_master_header_id else None
        committee_member_type = member.committe_member_type_id.committe_member_type if member.committe_member_type_id else None

        committee_info_list.append({
            'Department': department_name,
            'Festival': festival_name,
            'Committee_Member_Type': committee_member_type,
            'Committee_Member_Name': member.committe_member_name,
            'Committee_Member_Phone': member.committe_member_phone,
            'Committee_Member_Photo': member.committe_member_photo,
            'id': member.id,
        })

    return render(request,'AdminMain/OrganizingCommitte/view.html',{'data':committee_info_list})

class EditOrganizingCommitte(View):
    def get(self, request, *args, **kwargs):
        id = self.kwargs.get('id')
        committee_member = get_object_or_404(OrganizingCommitteMaster, id=id)
        festivals = FestivalMasterHeader.objects.filter(is_active=1)
        departments = DepartmentMaster.objects.filter(is_active=1)
        committee_types = CommitteMemberTypeMaster.objects.filter(is_active=1)

        festival_id = committee_member.festival_master_header_id.id if committee_member.festival_master_header_id else None
        festival_name = committee_member.festival_master_header_id.festival_name if committee_member.festival_master_header_id else None
        department_id = committee_member.department_master_id.id if committee_member.department_master_id else None
        department_name = committee_member.department_master_id.department_name if committee_member.department_master_id else None
        committee_member_type_id = committee_member.committe_member_type_id.id if committee_member.committe_member_type_id else None
        committee_member_type = committee_member.committe_member_type_id.committe_member_type if committee_member.committe_member_type_id else None

        committee_info = {
            'FestivalId':festival_id,
            'Festival': festival_name,
            'DepartmentId':department_id,
            'Department': department_name,
            'Committee_Member_Type_Id':committee_member_type_id,
            'Committee_Member_Type': committee_member_type,
            'Committee_Member_Name': committee_member.committe_member_name,
            'Committee_Member_Phone': committee_member.committe_member_phone,
            'Committee_Member_Photo': committee_member.committe_member_photo,
            'id': committee_member.id,
        }

        return render(request, 'AdminMain/OrganizingCommitte/edit.html', {'data': committee_info,'FestivalMaster':festivals,'Department':departments,'CommitteType':committee_types})

    def post(self,request,*args,**kwargs):
        id = self.kwargs.get('id')
        if request.method == 'POST':
            festival_master_header_id = request.POST['festival_master_header_id']
            department_master_id = request.POST['department_master_id']
            committe_member_type_id = request.POST['committe_member_type_id']

            # Fetch objects using IDs
            festival_id = FestivalMasterHeader.objects.get(id=festival_master_header_id)
            department_id = get_object_or_404(DepartmentMaster, pk=department_master_id)
            committe_id = get_object_or_404(CommitteMemberTypeMaster, pk=committe_member_type_id)

            # Fetch the committee member
            committee_member = get_object_or_404(OrganizingCommitteMaster, pk=id)

            # Update committee member fields
            committee_member.festival_master_header_id = festival_id
            committee_member.department_master_id = department_id
            committee_member.committe_member_type_id = committe_id

            committee_member.committe_member_name = request.POST.get('committe_member_name')
            committee_member.committe_member_phone = request.POST.get('committe_member_phone')
            if 'photo' in request.FILES:
                # Update with the uploaded file
                uploaded_photo = request.FILES['photo']
                committee_member.committe_member_photo = uploaded_photo
                fss = FileSystemStorage()
                file = fss.save(uploaded_photo.name, uploaded_photo)
                file_url = fss.url(file)
            else:
                # Update with the default data
                committee_member.committe_member_photo = request.POST.get('committe_member_photo')

            committee_member.save()
            return redirect('ViewOrganizingCommitte')

def delete_organizing_committe(request,id):
    return render(request,'AdminMain/OrganizingCommitte/delete.html',{'data':id})

def delete_organizing_committe1(request,id):
    organizing_committe = get_object_or_404(OrganizingCommitteMaster, pk=id)
    organizing_committe.is_active = 0
    organizing_committe.save()
    return redirect('ViewOrganizingCommitte')

# ----------------------------------------------------Event Master--------------------------------------------------------



class CreateEventMaster(View):
    def get(self,request):
        current_date = date.today()
        festival_master_header = FestivalMasterHeader.objects.filter(is_active=1, to_date__gte=current_date)
        event_category = EventCategoryMaster.objects.filter(is_active=1)
        participant_category = ParticipantCategoryMaster.objects.filter(is_active=1)
        return render(request,'AdminMain/EventMaster/create.html',{'festival':festival_master_header,'EventCategory':event_category,'ParticipantCategory':participant_category})

    def post(self,request):
        if request.method == 'POST':
            festival_master_header_id = request.POST['festival_master_header_id']
            event_category_id = request.POST['event_category_id']
            participant_category_id = request.POST['participant_category_id']

            event_name = request.POST['event_name'].strip()
            registration_fee = request.POST['registration_fee'].strip()
            # event_type = request.POST['event_type']
            max_team_size =  request.POST['max_team_size'].strip()
            min_team_size = request.POST['min_team_size'].strip()
            abbreviation = request.POST['abbreviation'].strip()
            max_registration = request.POST['max_registration'].strip()
            event_description = request.POST['event_description'].strip()
            event_document = request.FILES['event_document']
            video_file = request.FILES.get('video_file')
            fss = FileSystemStorage()
            file = fss.save(event_document.name, event_document)
            file_url = fss.url(file)


            if len(registration_fee) > 0 and  len(event_description) > 0 and len(event_name):

                festival_id = FestivalMasterHeader.objects.get(pk=festival_master_header_id)
                event_id = EventCategoryMaster.objects.get(pk=event_category_id)
                participant_id = ParticipantCategoryMaster.objects.get(pk=participant_category_id)
                try:
                    event_master = EventMaster.objects.get(festival_master_header_id=festival_id,event_category_id=event_id,participant_category_id=participant_id,event_name=event_name,is_active=1)
                    return HttpResponse("<script>alert('Event Master already added');window.location='../ViewEventMaster';</script>")
                except:
                    event_master = EventMaster(
                        festival_master_header_id=festival_id,
                        event_category_id=event_id,
                        participant_category_id=participant_id,
                        event_name=event_name,
                        registration_fee=registration_fee,
                        event_document=event_document,
                        # event_type=event_type,
                        abbreviation=abbreviation,
                        event_description=event_description,
                        max_registration=max_registration,
                        is_active=1,
                        created_on=datetime.now(),
                        created_by="admin"
                    )
                    if participant_id.participant_category_name != 'Single':
                        if max_team_size is not None and min_team_size is not None:
                            event_master.max_team_size = max_team_size
                            event_master.min_team_size = min_team_size
                    else:
                        event_master.max_team_size = 1
                        event_master.min_team_size = 1

                    if video_file:
                        fss1 = FileSystemStorage()
                        file = fss1.save(video_file.name, video_file)
                        file_url1 = fss1.url(file)
                        event_master.video_file = video_file

                    event_master.save()
                    return HttpResponse("<script>alert('Event Master Added successfully');window.location='../ViewEventMaster';</script>")
        # return HttpResponse("<script>alert('Error: Invalid form data');window.location='../ViewEventMaster';</script>")


def view_event_master(request):
    current_date = date.today()
    event_master = EventMaster.objects.filter(
        is_active=1,
        festival_master_header_id__is_active=True,
    ).exclude(
        Q(festival_master_header_id__to_date__lt=current_date)
        )
    event_info_list = []
    print("-------------------------------------------------------------------------",event_master)
    for event in event_master:
        festival_name = event.festival_master_header_id.festival_name if event.festival_master_header_id else None
        event_category_name = event.event_category_id.event_category_name if event.event_category_id else None
        participant_category_name = event.participant_category_id.participant_category_name if event.participant_category_id else None

        event_info_list.append({
            'Festival': festival_name,
            'EventCatgory': event_category_name,
            'Participant': participant_category_name,
            'EventName': event.event_name,
            'RegistrationFee': event.registration_fee,
            'EventDocument': event.event_document,
            # 'EventType': event.event_type,
            'MaxTeamSize': event.max_team_size,
            'MinTeamSize': event.min_team_size,
            'MaxRegistration':event.max_registration,
            'Abbreviation':event.abbreviation,
            'EventDescription':event.event_description,
            'VideoFile':event.video_file,
            'id': event.id,
        })
    return render(request,'AdminMain/EventMaster/view.html',{'data':event_info_list})

class EditEventMaster(View):
    def get(self, request, *args, **kwargs):
        id = self.kwargs.get('id')
        event_master = get_object_or_404(EventMaster, id=id)
        festivals = FestivalMasterHeader.objects.filter(is_active=1)
        event_category = EventCategoryMaster.objects.filter(is_active=1)
        participant_category = ParticipantCategoryMaster.objects.filter(is_active=1)

        festival_id = event_master.festival_master_header_id.id if event_master.festival_master_header_id else None
        festival_name = event_master.festival_master_header_id.festival_name if event_master.festival_master_header_id else None
        event_category_id = event_master.event_category_id.id if event_master.event_category_id else None
        event_category_name = event_master.event_category_id.event_category_name if event_master.event_category_id else None
        participant_category_id = event_master.participant_category_id.id if event_master.participant_category_id else None
        participant_category_name = event_master.participant_category_id.participant_category_name if event_master.participant_category_id else None


        event_master_info = {
            'FestivalId': festival_id,
            'Festival': festival_name,
            'EventCategoyrId': event_category_id,
            'EventCategory': event_category_name,
            'ParticipantCategoryId': participant_category_id,
            'ParticipantCategory': participant_category_name,
            'EventType': event_master.event_type,
            'EventName': event_master.event_name,
            'Registration': event_master.registration_fee,
            'EventDocument': event_master.event_document,
            'MinTeamSize': event_master.min_team_size,
            'MaxTeamSize': event_master.max_team_size,
            'MaxRegistration':event_master.max_registration,
            'Abbreviation':event_master.abbreviation,
            'Description': event_master.event_description,
            'id': event_master.id,
        }
        return render(request,'AdminMain/EventMaster/edit.html',{'data':event_master_info,'FestivalMaster':festivals,'EventCategory':event_category,'ParticipantCategory':participant_category})

    def post(self,request,*args,**kwargs):
        id = self.kwargs.get('id')
        if request.method == 'POST':
            festival_master_header_id = request.POST['festival_master_header_id']
            event_category_id = request.POST['event_category_id']
            participant_category_id = request.POST['participant_category_id']

            # Fetch objects using IDs
            festival_id = FestivalMasterHeader.objects.get(id=festival_master_header_id)
            event_id = get_object_or_404(EventCategoryMaster, pk=event_category_id)
            participant_id = get_object_or_404(ParticipantCategoryMaster, pk=participant_category_id)

            # Fetch the committee member
            event_master = get_object_or_404(EventMaster, pk=id)

            # Update committee member fields
            event_master.festival_master_header_id = festival_id
            event_master.event_category_id = event_id
            event_master.participant_category_id = participant_id

            event_master.event_name = request.POST.get('event_name')
            event_master.registration_fee = request.POST.get('registration_fee')
            event_master.event_type = request.POST.get('event_type')
            event_master.min_team_size = request.POST.get('min_team_size')
            event_master.max_team_size = request.POST.get('max_team_size')
            event_master.max_registration = request.POST.get('max_registration')
            event_master.abbreviation = request.POST.get('abbreviation')
            event_master.event_description = request.POST.get('event_description')

            # event_document = request.FILES['event_document']
            event_document = request.FILES.get('event_document')
            video_file = request.FILES.get('video_file')
            if event_document:
                fss = FileSystemStorage()
                file = fss.save(event_document.name, event_document)
                file_url = fss.url(file)
                event_master.event_document = event_document

            if video_file:
                print("--------------------video file :",video_file)
                fss = FileSystemStorage()
                file = fss.save(video_file.name, video_file)
                file_url = fss.url(file)
                event_master.video_file = video_file

            event_master.save()
            return HttpResponse("<script>alert('Event Master Edited successfully');window.location='../ViewEventMaster';</script>")

def delete_event_master(request,id):
    return render(request,'AdminMain/EventMaster/delete.html',{'data':id})

def delete_event_master1(request,id):
    EventMaster.objects.filter(id=id).update(is_active = 0)
    return redirect('ViewEventMaster')

# -----------------------------------------------------------------Event Schedular----------------------------------------

class CreateEventScheduler(View):
    def get(self,request):
        current_date = date.today()
        festival_master = FestivalMasterHeader.objects.filter(is_active=1, to_date__gte=current_date)
        event_master = EventMaster.objects.filter(is_active=1)
        return render(request,'AdminMain/EventScheduler/create.html',{'festival':festival_master,'EventMaster':event_master})

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
                return HttpResponse("<script>alert('already scheduled ');window.location='../CreateEventScheduler';</script>")
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
    current_date = date.today()
    event_scheduler = EventScheduler.objects.filter(
    is_active=True,
    event_master_id__is_active=True,
    event_master_id__festival_master_header_id__is_active=True
    ).exclude(
    Q(event_master_id__festival_master_header_id__to_date__lt=current_date)
    )
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
    return render(request,'AdminMain/EventScheduler/view.html',{'data':event_info_list})

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
        return render(request,'AdminMain/EventScheduler/create.html',{'data':event_master_info})

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
            return HttpResponse("<script>alert('Event Scheduler updated successfully');window.location='../ViewEventScheduler';</script>")

def delete_event_scheduler(request,id):
    return render(request,'AdminMain/EventScheduler/delete.html',{'data':id})

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
        festival_id = request.GET.get('festival_id')
        print("-------------------------------------------------------------------",participant_id,event_category_id,festival_id)
        festival = FestivalMasterHeader.objects.get(pk = festival_id)
       # Fetch Event Categories based on the selected Festival ID
        if participant_id:
            event_master = EventMaster.objects.filter(
                participant_category_id=participant_id,
                event_category_id = event_category_id,
                festival_master_header_id = festival,
                is_active=1
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


# ------------------------------------------------------- Event Prize Master --------------------------------------

class CreateEventPrize(View):
    def get(self,request):
        current_date = date.today()
        festival_master = FestivalMasterHeader.objects.filter(is_active=1,to_date__gte=current_date)
        WinnerPosition = WinnerPositionMasterModel.objects.filter(is_active=1)
        PrizeType = PrizeTypeMasterModel.objects.filter(is_active=1)
        return render(request,'AdminMain/EventPrize/create.html',{'festival':festival_master,'WinnerPosition':WinnerPosition,'PrizeType':PrizeType})

    def post(self,request):
        if request.method == 'POST':
            event_master_id = request.POST['event_master_id']
            winner_id = request.POST['winner_position_id']
            prize_id = request.POST['prize_type_id']
            cash_amount = request.POST['cash_amount']
            event_score = request.POST['event_score']

            winner_position_id = WinnerPositionMasterModel.objects.get(pk=winner_id)
            prize_type_id = PrizeTypeMasterModel.objects.get(pk=prize_id)
            event_master = get_object_or_404(EventMaster, pk=event_master_id)
            try:
                EventPrizeMaster.objects.get(event_master_id=event_master,winner_position_id=winner_position_id, is_active=1)
                return HttpResponse("<script>alert('Event prize already added');window.location='../CreateEventPrize';</script>")

            except:
                event_prize = EventPrizeMaster(
                    event_master_id = event_master,
                    winner_position_id = winner_position_id,
                    prize_type_id = prize_type_id,
                    event_cash_prize = cash_amount,
                    event_scores = event_score,
                    is_active = 1,
                    created_on = datetime.now(),
                    created_by = "admin",
                )
                event_prize.save()
                return HttpResponse("<script>alert('Event prize added successfully');window.location='../ViewEventPrize';</script>")


def view_event_prize(request):
    current_date = date.today()
    event_prize = EventPrizeMaster.objects.filter(
        is_active=1,
        event_master_id__is_active=True,
        event_master_id__festival_master_header_id__is_active=True
    ).exclude(
    Q(event_master_id__festival_master_header_id__to_date__lt=current_date)
    ).order_by('event_master_id__event_name')  # Order by event_name
    event_info_list = []
    for event in event_prize:
        festival_category_name = event.event_master_id.festival_master_header_id if event.event_master_id else None
        event_category_name = event.event_master_id.event_category_id if event.event_master_id else None
        event_name = event.event_master_id.event_name if event.event_master_id else None
        # participant_category = event.event_master_id.
        event_info_list.append({
            'Festival':festival_category_name,
            'EventName':event_name,
            'EventCategory': event_category_name,
            'Winner': event.winner_position_id,
            'PrizeType': event.prize_type_id,
            'CashAmount': event.event_cash_prize,
            'EventScore':event.event_scores,
            'id': event.id,
        })
    return render(request,'AdminMain/EventPrize/view.html',{'data':event_info_list})

class EditEventPrize(View):
    def get(self,request,*args,**kwargs):
        id = self.kwargs.get('id')
        event_prize = get_object_or_404(EventPrizeMaster, id=id)  # Fetch the EventPrizeMaster instance first
        event_master = event_prize.event_master_id
        print("------------------------------------------------EventMaster",event_master)
        festival_id = event_master.festival_master_header_id.id if event_master and event_master.festival_master_header_id else None
        festival_name = event_master.festival_master_header_id.festival_name if event_master and event_master.festival_master_header_id else None
        event_category_id = event_master.event_category_id.id if event_master and event_master.event_category_id else None
        event_category_name = event_master.event_category_id.event_category_name if event_master and event_master.event_category_id else None
        participant_category_id = event_master.participant_category_id.id if event_master and event_master.participant_category_id else None
        participant_category_name = event_master.participant_category_id.participant_category_name if event_master and event_master.participant_category_id else None
        event_master_id = event_master.id if event_master else None
        event_name = event_master.event_name if event_master else None

        event_prize_info = {
            'FestivalId': festival_id,
            'Festival': festival_name,
            'EventCategoryId': event_category_id,
            'EventCategory': event_category_name,
            'ParticipantCategoryId': participant_category_id,
            'ParticipantCategory': participant_category_name,
            'EventMasterId': event_master_id,
            'EventName': event_name,
            # 'WinnerPosition': event_prize.winner_position_id,
            # 'PrizeType': event_prize.prize_type_id,
            'WinnerPositionId': event_prize.winner_position_id.id if event_prize.winner_position_id else None,
            'WinnerPosition': event_prize.winner_position_id.winner_position if event_prize.winner_position_id else None,
            'PrizeTypeId': event_prize.prize_type_id.id if event_prize.prize_type_id else None,
            'PrizeType': event_prize.prize_type_id.prize_type if event_prize.prize_type_id else None,
            'CashPrize':event_prize.event_cash_prize,
            'EventScore':event_prize.event_scores,
            'id': event_prize.id,
        }
        print("-----------------------------------------------------event_prize_info",event_prize_info)
        WinnerPosition = WinnerPositionMasterModel.objects.filter(is_active=1)
        PrizeType = PrizeTypeMasterModel.objects.filter(is_active=1)
        return render(request,'AdminMain/EventPrize/edit.html',{'data':event_prize_info,'WinnerPosition':WinnerPosition,'PrizeType':PrizeType})

    def post(self,request,*args,**kwargs):
        id = self.kwargs.get('id')
        event_prize = get_object_or_404(EventPrizeMaster, id=id)

        # Extract the form data
        festival_id = request.POST.get('festival_master_header_id')
        event_category_id = request.POST.get('event_category_id')
        participant_category_id = request.POST.get('participant_category_id')
        event_master_id = request.POST.get('event_master_id')
        winner_position_id = request.POST.get('winner_position_id')
        prize_type_id = request.POST.get('prize_type_id')
        cash_amount = request.POST.get('cash_amount')
        event_score = request.POST.get('event_score')

        event_master = get_object_or_404(EventMaster, id=event_master_id)

        event_prize.event_scores = event_score

        try:
            existing_instance = EventPrizeMaster.objects.exclude(id=event_prize.id).get(
            event_master_id=event_master,
            winner_position_id=winner_position_id,
            is_active=1
            )
            return HttpResponse("<script>alert('This combination already exists.');window.location='ViewEventPrize';</script>")
        except:
            event_master = get_object_or_404(EventMaster, id=event_master_id)
            winner_position = get_object_or_404(WinnerPositionMasterModel, id=winner_position_id)
            prize_type = get_object_or_404(PrizeTypeMasterModel, id=prize_type_id)

            # Update the EventPrizeMaster instance with the new data
            event_prize.event_master_id = event_master
            event_prize.winner_position_id = winner_position
            event_prize.prize_type_id = prize_type
            event_prize.event_cash_prize = cash_amount
            event_prize.event_scores = event_score

            # Save the changes to the database
            event_prize.save()
            return HttpResponse("<script>alert('Event Prize Successfully updated');window.location='../ViewEventPrize';</script>")

def delete_event_prize(request,id):
    return render(request,'AdminMain/EventPrize/delete.html',{'data':id})

def delete_event_prize1(request,id):
    EventPrizeMaster.objects.filter(id=id).update(is_active = 0)
    return redirect('ViewEventPrize')

# -------------------------------------------------Participant Registration Header--------------------------------------


class CreateParticipantRegistartion(View):
    def get(self,request):
        current_date = date.today()
        festival_master = FestivalMasterHeader.objects.filter(is_active=1,to_date__gte=current_date)
        participant_type = ParticipantTypeMaster.objects.filter(is_active=1)
        return render(request,'AdminMain/ParticipantRegistration/create.html',{'festival':festival_master,'ParticipantType':participant_type})

    def post(self, request):
        if request.method == 'POST':
            event_master_id = request.POST['event_master_id']
            college_name = request.POST['college_name']
            reference_by = request.POST['reference_by']
            event_master = EventMaster.objects.get(pk=event_master_id)
            festival_id = event_master.festival_master_header_id

            if event_master.max_registration and ParticipantRegistrationHeader.objects.filter(event_master_id=event_master,participantregistrationpayment__payment_status=1).count() >= event_master.max_registration:
                return HttpResponse("<script>alert('Registration limit reached maximum.');window.location='../CreateParticipantRegistartion';</script>")

            abbreviation = event_master.abbreviation
            # chest_number = f"{abbreviation}{ParticipantRegistrationHeader.objects.filter(event_master_id__abbreviation=abbreviation).count() + 1:02d}"

            latest_registration = ParticipantRegistrationHeader.objects.filter(
            event_master_id=event_master
            ).order_by('-created_on').first()

            if latest_registration:
                # Extract the numeric part of the chest_number and increment it
                latest_chest_number = latest_registration.event_chest_no
                latest_chest_number_numeric = int(latest_chest_number[-2:])
                next_chest_number_numeric = latest_chest_number_numeric + 1
                next_chest_number = f"{abbreviation}{next_chest_number_numeric:02d}"
            else:
                # If there are no existing registrations, set chest_number to the initial value
                next_chest_number = f"{abbreviation}01"

            # Create ParticipantRegistrationHeader instance with user info
            registration_header = ParticipantRegistrationHeader.objects.create(
                event_master_id=event_master,
                college_name=college_name,
                reference_by = reference_by,
                event_chest_no=next_chest_number,
                created_by="admin",
                is_active=1
            )

            # Access participant details lists sent from the form
            participant_category = request.POST['participant_category_id']
            participant_category_name = ParticipantCategoryMaster.objects.get(pk=participant_category).participant_category_name
            participant_type = request.POST.getlist('participant_type')
            participant_names = request.POST.getlist('participant_name')
            participant_phones = request.POST.getlist('participant_phone')
            participant_email = request.POST.getlist('participant_email')
            participant_id_nos = request.POST.getlist('participant_id_no')
            participant_id_images = request.FILES.getlist('participant_id_image')


            # Save participant_id_images using FileSystemStorage
            file_urls = []
            for participant_id_card in participant_id_images:
                fss = FileSystemStorage()
                file = fss.save(participant_id_card.name, participant_id_card)
                file_url = fss.url(file)
                file_urls.append(file_url)

             # Check if participants with the same details already exist for the given EventMaster
            existing_participants = ParticipantRegistrationChild.objects.filter(
                # participant_registration_header_id__event_master_id=event_master,
                participant_phone__in=participant_phones,
                participant_email__in=participant_email,
                participant_id_no__in=participant_id_nos,
                participant_registration_header_id__event_master_id__festival_master_header_id=festival_id
            )
            if existing_participants:
                return HttpResponse("<script>alert('Already registered ');window.location='../CreateParticipantRegistartion';</script>")

            # Get the correct ParticipantTypeMaster ID based on participant_category_name
            if participant_category_name == 'Group':
                team_leader_type_name = 'Team Leader'
                team_leader_type = ParticipantTypeMaster.objects.filter(participant_type=team_leader_type_name, is_active=1).first()
                if team_leader_type:
                    team_leader_type_id = team_leader_type.id
                else:
                    # Create a new ParticipantTypeMaster for Team Leader if not exists
                    team_leader_type = ParticipantTypeMaster.objects.create(
                        participant_type=team_leader_type_name,
                        created_by="admin",
                        is_active=1
                    )
                    team_leader_type_id = team_leader_type.id
            else:
                team_leader_type_id = None  # Set to None for Single participants

            # Create ParticipantRegistrationChild instances for each participant detail
            for i in range(len(participant_names)):
                # Determine the correct participant_type_id based on the role (Team Leader or Team Member)
                if i == 0 and participant_category_name == 'Group':
                    participant_type_instance = team_leader_type
                else:
                    # Check if the ParticipantTypeMaster with the given name and is_active=1 exists
                    existing_participant_type = ParticipantTypeMaster.objects.filter(participant_type=participant_type[i], is_active=1).first()
                    if existing_participant_type:
                        participant_type_instance = existing_participant_type
                    else:
                        # Create a new ParticipantTypeMaster if not exists
                        new_participant_type = ParticipantTypeMaster.objects.create(
                            participant_type=participant_type[i],
                            created_by="admin",
                            is_active=1
                        )
                        participant_type_instance = new_participant_type

                participant_child = ParticipantRegistrationChild.objects.create(
                    participant_registration_header_id=registration_header,
                    participant_name=participant_names[i],
                    participant_phone=participant_phones[i],
                    participant_email=participant_email[i],
                    participant_id_no=participant_id_nos[i],
                    participant_id_card=file_urls[i],
                    participant_type_id=participant_type_instance,  # Assign the instance, not the ID
                    created_by="admin"
                    # Assign other fields accordingly
                )

            total_amount = request.POST['total_amount']
            payment_type = request.POST['payment_type']

            payment = ParticipantRegistrationPayment.objects.create(
                participant_registration_header_id=registration_header,
                registration_fee=total_amount,
                payment_type=payment_type,
                registration = "spot",
                payment_status=1,
                created_by="admin"
                # Assign other fields accordingly
            )
            payment.save()
            print("----------------------------------------------------------",payment.id)
            request.session["PaymentID"] = payment.id
            return HttpResponse("<script>alert('successfully registered');window.location='../GeneratePaymentReceipt_Admin';</script>")



    # def post(self,request):
    #     if request.method == 'POST':
    #         # Assuming you have user authentication or can retrieve user details
    #         # current_user = request.session['AdminId']  # Fetch current user information
    #
    #         event_master_id = request.POST['event_master_id']
    #         college_name = request.POST['college_name']
    #         # event_chest_no = request.POST['chest_no']
    #         # receipt_no = request.POST['receipt_no']
    #
    #         event_master = EventMaster.objects.get(pk=event_master_id)
    #         abbreviation = event_master.abbreviation
    #         print("----------------------------------------------------",event_master,abbreviation)
    #         chest_number = f"{abbreviation}{ParticipantRegistrationHeader.objects.filter(event_master_id__abbreviation=abbreviation).count() + 1:02d}"
    #
    #         # Create ParticipantRegistrationHeader instance with user info
    #         registration_header = ParticipantRegistrationHeader.objects.create(
    #             event_master_id=event_master,
    #             college_name=college_name,
    #             event_chest_no=chest_number,
    #             # receipt_no=receipt_no,
    #             created_by="admin",  # Store user who created this entry
    #             is_active=1
    #             # Assign other fields accordingly
    #         )
    #
    #         # Access participant details lists sent from the form
    #         participant_category = request.POST['participant_category_id']
    #         participant_category_name =  ParticipantCategoryMaster.objects.filter(pk=participant_category).values('participant_category_name')
    #         participant_type = request.POST.getlist('participant_type')
    #         participant_names = request.POST.getlist('participant_name')
    #         participant_phones = request.POST.getlist('participant_phone')
    #         participant_email = request.POST.getlist('participant_email')
    #         participant_id_nos = request.POST.getlist('participant_id_no')
    #         participant_id_images = request.FILES.getlist('participant_id_image')
    #
    #         # Save participant_id_images using FileSystemStorage
    #         file_urls = []
    #         for participant_id_card in participant_id_images:
    #             fss = FileSystemStorage()
    #             file = fss.save(participant_id_card.name, participant_id_card)
    #             file_url = fss.url(file)
    #             file_urls.append(file_url)
    #
    #         # Create ParticipantRegistrationChild instances for each participant detail
    #         for i in range(len(participant_names)):
    #             participant_child = ParticipantRegistrationChild.objects.create(
    #                 participant_registration_header_id=registration_header,
    #                 participant_name=participant_names[i],
    #                 participant_phone=participant_phones[i],
    #                 participant_email=participant_email[i],
    #                 participant_id_no=participant_id_nos[i],
    #                 participant_id_card=file_urls[i],  # Using file URLs saved previously
    #                 created_by="admin"
    #                 # Assign other fields accordingly
    #             )
    #
    #         # Process and create ParticipantRegistrationPayment instance
    #         # registration_fee = request.POST['registration_fee']
    #         total_amount = request.POST['total_amount']
    #         payment_type = request.POST['payment_type']
    #
    #         payment = ParticipantRegistrationPayment.objects.create(
    #             participant_registration_header_id=registration_header,
    #             registration_fee=total_amount,
    #             payment_type=payment_type,
    #             payment_status=0,
    #             created_by="admin"  # Store user who created this entry
    #             # Assign other fields accordingly
    #         )
    #         payment.save()
    #         return HttpResponse("<script>alert('successfully registered');window.location='../ViewParticipantRegistration';</script>")


class GetEventMasterForParticipant(View):
    def get(self, request, *args, **kwargs):
        participant_id = request.GET.get('participant_id')
        event_category_id = request.GET.get('event_category_id')
        festival_id = request.GET.get('festival_id')
        # Fetch Event Categories based on the selected Participant ID and Event Category ID
        if participant_id and event_category_id and festival_id:
            participant_category = ParticipantCategoryMaster.objects.get(pk=participant_id)
            festival = FestivalMasterHeader.objects.filter(pk = festival_id)
            # Filter EventMaster based on participant_category and event_category_id
            event_master = EventMaster.objects.filter(
                participant_category_id=participant_id,
                event_category_id = event_category_id,
                festival_master_header_id = festival_id,
                is_active=1
            ).values('id', 'event_name')
            print("-----------------------------------------------------------------",event_master)

            # If the participant type is 'Single' or 'Group', retrieve scheduled events
            if participant_category.participant_category_name in ['Single', 'Group']:
                scheduled_events = EventScheduler.objects.filter(
                    event_master_id__in=event_master.values('id'),
                    is_active=1
                ).values_list('event_master_id', flat=True)

                # Filter out events that are not scheduled
                event_master = event_master.filter(id__in=scheduled_events)

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

class GetRegistrationFee(View):
    def get(self, request, *args, **kwargs):
        event_id = request.GET.get('event_id')
        if event_id:
            try:
                event = get_object_or_404(EventMaster, id=event_id)
                registration_fee = event.registration_fee
                min_team_size = event.min_team_size
                max_team_size = event.max_team_size
                return JsonResponse({'registration_fee': registration_fee,'min_team_size': min_team_size,'max_team_size':max_team_size})

            except EventMaster.DoesNotExist:
                return JsonResponse({'error': 'Event not found'}, status=404)

            except Exception as e:
                return JsonResponse({'error': str(e)}, status=500)

        else:
            return JsonResponse({'error': 'Invalid event_id'}, status=400)

def view_participant_registration(request):
    current_date = date.today()
     # Query participant registration data
    participant_data = ParticipantRegistrationChild.objects.select_related(
        'participant_type_id',
        'participant_registration_header_id__event_master_id__festival_master_header_id',
        'participant_registration_header_id__event_master_id__event_category_id'
    ).filter(is_active=1,
             participant_registration_header_id__event_master_id__festival_master_header_id__is_active=1,
             participant_registration_header_id__event_master_id__festival_master_header_id__to_date__gte=current_date
            )

    participant_data = participant_data.filter(
        participant_registration_header_id__participantregistrationpayment__payment_status=1,
        # participant_registration_header_id__participantregistrationpayment__registration="spot"

    )

    participant_data = participant_data.order_by('-participant_registration_header_id__created_on')

    # Prepare data for rendering in the HTML table
    table_data = []
    for participant in participant_data:
        participant_type = participant.participant_type_id.participant_type if participant.participant_type_id else None

        table_data.append({
            'festival_name': participant.participant_registration_header_id.event_master_id.festival_master_header_id.festival_name,
            'event_name': participant.participant_registration_header_id.event_master_id.event_name,
            'event_category': participant.participant_registration_header_id.event_master_id.event_category_id.event_category_name,
            'participant_category': participant.participant_registration_header_id.event_master_id.participant_category_id.participant_category_name,
            'participant_type': participant_type,
            'event_chest_no': participant.participant_registration_header_id.event_chest_no,
            'participant_name': participant.participant_name,
            'participant_phone': participant.participant_phone,
            'participant_email': participant.participant_email,
            'participant_id_no': participant.participant_id_no,
            'participant_id_card':participant.participant_id_card,
            'Participant_college': participant.participant_registration_header_id.college_name,
            'child_id': participant.id
        })

    return render(request,'AdminMain/ParticipantRegistration/view.html', {'table_data': table_data})

def GeneratePaymentReceipt(request):
    participant_registration_payment_id = request.session["PaymentID"]
    receipt = ParticipantRegistrationPayment.objects.get(id=participant_registration_payment_id)
    # payment_status = receipt.payment_status
    # if payment_status == 0:
    #     receipt.payment_status = 1
    #     receipt.save()

    # Fetch related data
    participant_registration_header = receipt.participant_registration_header_id
    participant_registration_child = ParticipantRegistrationChild.objects.filter(
        participant_registration_header_id=participant_registration_header.id
    ).first()

    event_master = EventMaster.objects.get(id=participant_registration_header.event_master_id.id)
    festival_master_header = FestivalMasterHeader.objects.get(id=event_master.festival_master_header_id.id)
    event_scheduler = EventScheduler.objects.get(event_master_id=event_master.id)

    context = {
        'receipt': receipt,
        'college_name': participant_registration_header.college_name,
        'Chest_number':participant_registration_header.event_chest_no,
        'event_chest_no': participant_registration_header.event_chest_no,
        'participant_name': participant_registration_child.participant_name,
        'participant_phone': participant_registration_child.participant_phone,
        'event_name': event_master.event_name,
        'registration_fee': receipt.registration_fee,
        'festival_name': festival_master_header.festival_name,
        'event_start_date': event_scheduler.event_start_date,
        'event_end_date': event_scheduler.event_end_date,
    }
    return render(request, 'AdminMain/ParticipantRegistration/pay_slip.html', context)


def GeneratePaymentReceipt_Admin(request):
    participant_registration_payment_id = request.session["PaymentID"]
    receipt = ParticipantRegistrationPayment.objects.get(id=participant_registration_payment_id)
    # payment_status = receipt.payment_status
    # if payment_status == 0:
    #     receipt.payment_status = 1
    #     receipt.save()

    # Fetch related data
    participant_registration_header = receipt.participant_registration_header_id
    participant_registration_child = ParticipantRegistrationChild.objects.filter(
        participant_registration_header_id=participant_registration_header.id
    ).first()

    event_master = EventMaster.objects.get(id=participant_registration_header.event_master_id.id)
    festival_master_header = FestivalMasterHeader.objects.get(id=event_master.festival_master_header_id.id)
    event_scheduler = EventScheduler.objects.get(event_master_id=event_master.id)

    context = {
        'receipt': receipt,
        'college_name': participant_registration_header.college_name,
        'Chest_number':participant_registration_header.event_chest_no,
        'event_chest_no': participant_registration_header.event_chest_no,
        'participant_name': participant_registration_child.participant_name,
        'participant_phone': participant_registration_child.participant_phone,
        'event_name': event_master.event_name,
        'registration_fee': receipt.registration_fee,
        'festival_name': festival_master_header.festival_name,
        'event_start_date': event_scheduler.event_start_date,
        'event_end_date': event_scheduler.event_end_date,
    }
    return render(request, 'AdminMain/ParticipantRegistration/pay_slip_admin.html', context)

class ParticipantListEdit1(View):
    def get(self,request,*args,**kwargs):
        id = self.kwargs.get('id')

        Participants = ParticipantRegistrationChild.objects.filter(pk=id)
        response_data = []
        for participant in Participants:
            participant_info = {
                'participant_chest_no':participant.participant_registration_header_id.event_chest_no,
                'participant_name': participant.participant_name,
                'college_name': participant.participant_registration_header_id.college_name,
                'participant_phone': participant.participant_phone,
                'participant_email': participant.participant_email,
                'reference_by': participant.participant_registration_header_id.reference_by,
                'participant_id_card': participant.participant_id_no,
                'id':participant.id
                # Include other fields as needed
            }
            response_data.append(participant_info)
        return render(request,'AdminMain/ParticipantRegistration/participant_list_edit.html',{'data':response_data})

    def post(self,request,*args,**kwargs):
        id = self.kwargs.get('id')
        Participants = ParticipantRegistrationChild.objects.get(pk=id)
        participant_header = Participants.participant_registration_header_id

        # participant_chest_no = request.POST['participant_chest_no']
        participant_name = request.POST['participant_name']
        college_name = request.POST['college_name']
        participant_phone = request.POST['participant_phone']
        participant_email = request.POST['participant_email']
        reference_by = request.POST['reference_by']
        participant_id_no = request.POST['participant_id_no']
        print("-----------------------------participant child :",participant_name,participant_phone,participant_email,participant_id_no,reference_by)
        participant_header.college_name = college_name
        participant_header.reference_by = reference_by
        participant_header.save()

        Participants.participant_name = participant_name
        Participants.participant_phone = participant_phone
        Participants.participant_email = participant_email
        Participants.participant_id_no = participant_id_no
        Participants.modified_on = datetime.now()
        # Save the changes to the database
        Participants.save()
        return HttpResponse("<script>alert('Participant details updated.');window.location='../ViewParticipantRegistration';</script>")

def participant_list_delete(request,id):
    return render(request,'AdminMain/ParticipantRegistration/delete.html',{'data':id})

def participant_list_delete1(request,id):
    participant_child = ParticipantRegistrationChild.objects.get(pk=id)
    participant_child.is_active = 0
    participant_child.save()
    return redirect('ViewParticipantRegistration')


#-------------------------------------------------------------Event Result ----------------------------------------------------------

class CreateEventResult(View):
    def get(self,request):
        current_date = date.today()
        festival = FestivalMasterHeader.objects.filter(is_active=1,to_date__gte=current_date)
        winner = WinnerPositionMasterModel.objects.filter(is_active=1)
        participants = ParticipantRegistrationChild.objects.all()
        return render(request,"AdminMain/EventResult/create.html",{'festival':festival,'WinnerPosition':winner,'participants': participants})

    def post(self, request):
        event_master_id = request.POST['event_master_id']
        winner_position_id = request.POST['winner_position_id']
        participant_id = request.POST['ParticipantHeaderId']
        college_name = request.POST['college_name']
        participant_name = request.POST['participant_name']
        participant_registration_header = ParticipantRegistrationHeader.objects.get(pk=participant_id)
        participant_header_id = participant_registration_header.id

        # Check if the entry already exists
        existing_result = EventResult.objects.filter(
            event_master_id=event_master_id,
            # winner_position_id=winner_position_id,
            participant_registration_header_id=participant_header_id,
            is_active=1
        ).exists()

        if existing_result:
            print("---------------------",existing_result)
            # If the entry exists, return a message or handle it as needed
            return HttpResponse("<script>alert('This event result already exists.');window.location='../CreateEventResult';</script>")
        else:
            # If the entry doesn't exist, create a new EventResult object and save it
            event_master = EventMaster.objects.get(pk=event_master_id)
            winner_position = WinnerPositionMasterModel.objects.get(pk=winner_position_id)
            participant_header = ParticipantRegistrationHeader.objects.get(pk=participant_header_id)

            event_result = EventResult(
                event_master_id=event_master,
                winner_position_id=winner_position,
                participant_registration_header_id=participant_header,
                is_active=1,
                created_on=datetime.now(),
                created_by="admin",
            )
            event_result.save()
            if college_name:
                participant_registration_header.college_name=college_name
                participant_registration_header.save()

            if participant_name:
                participant_child = ParticipantRegistrationChild.objects.filter(participant_registration_header_id=participant_header.id).first()
                participant_child.participant_name = participant_name
                participant_child.save()
                print("-----------------------------------participant name saved",participant_name)

        return HttpResponse("<script>alert('Successfully added event result');window.location='../CreateEventResult';</script>")


def view_event_result(request):
    current_date = date.today()
    event_results = EventResult.objects.select_related(
        'event_master_id', 'winner_position_id', 'participant_registration_header_id'
    ).filter(is_active=1,event_master_id__festival_master_header_id__to_date__gte=current_date).order_by('event_master_id__event_name')  # Order by event_name

    table_data = []

    for index, result in enumerate(event_results, start=1):
        winner_position = result.winner_position_id.winner_position if result.winner_position_id else None

        # Fetch related EventPrizeMaster for additional details
        event_prize = EventPrizeMaster.objects.filter(
            event_master_id=result.event_master_id,
            winner_position_id=result.winner_position_id
        ).first()

        prize_type = event_prize.prize_type_id.prize_type if event_prize and event_prize.prize_type_id else None
        cash_amount = event_prize.event_cash_prize if event_prize else None

        # Check if ParticipantRegistrationHeader has related ParticipantRegistrationChild
        participant_registration_header = result.participant_registration_header_id
        participant_name = None

        # Get the related ParticipantRegistrationChild data based on the header ID
        participant_registration_child = ParticipantRegistrationChild.objects.filter(
            participant_registration_header_id=participant_registration_header.id
        ).first()

        if participant_registration_child:
            participant_name = participant_registration_child.participant_name

        table_data.append({
            'SlNo': index,
            'Festival': result.event_master_id.festival_master_header_id.festival_name if result.event_master_id else None,
            'EventName': result.event_master_id.event_name if result.event_master_id else None,
            'EventCategory': result.event_master_id.event_category_id.event_category_name if result.event_master_id and result.event_master_id.event_category_id else None,
            'WinnerPosition': winner_position,
            'PrizeType': prize_type,
            'EventScore': event_prize.event_scores if event_prize else None,
            'CollegeName': participant_registration_header.college_name if participant_registration_header else None,
            'ChestNumber': participant_registration_header.event_chest_no if participant_registration_header else None,
            'CashAmount': cash_amount,
            'ParticipantName': participant_name,
            'ID': result.id,
        })
    return render(request, "AdminMain/EventResult/view.html", {'data': table_data})

class EditEventResult(View):
    def get(self,request, *args, **kwargs):
        id = self.kwargs.get('id')
        event_result = EventResult.objects.get(pk=id)
        event_master = event_result.event_master_id  # Access the EventMaster instance directly
        winner = WinnerPositionMasterModel.objects.filter(is_active=1)

        festival_id = event_master.festival_master_header_id.id if event_master and event_master.festival_master_header_id else None
        festival_name = event_master.festival_master_header_id.festival_name if event_master and event_master.festival_master_header_id else None
        event_category_id = event_master.event_category_id.id if event_master and event_master.event_category_id else None
        event_category_name = event_master.event_category_id.event_category_name if event_master and event_master.event_category_id else None
        participant_category_id = event_master.participant_category_id.id if event_master and event_master.participant_category_id else None
        participant_category_name = event_master.participant_category_id.participant_category_name if event_master and event_master.participant_category_id else None
        event_master_id = event_master.id if event_master else None
        event_name = event_master.event_name if event_master else None

        event_result_info = {
            'FestivalId': festival_id,
            'Festival': festival_name,
            'EventCategoryId': event_category_id,
            'EventCategory': event_category_name,
            'ParticipantCategoryId': participant_category_id,
            'ParticipantCategory': participant_category_name,
            'EventMasterId': event_master_id,
            'EventName': event_name,
            'WinnerPositionId': event_result.winner_position_id.id if event_result.winner_position_id else None,
            'WinnerPosition': event_result.winner_position_id.winner_position if event_result.winner_position_id else None,
            'ParticipantHeaderId':event_result.participant_registration_header_id_id,
            'ParticipantName': event_result.participant_registration_header_id.participantregistrationchild_set.first().participant_name,
            'ChestNumber':event_result.participant_registration_header_id.event_chest_no,
            'CollegeName':event_result.participant_registration_header_id.college_name,
            'id': event_result.id,
        }
        print("--------------------------------------------------------event_result_info",event_result_info)
        return render(request,'AdminMain/EventResult/edit.html',{'data':event_result_info,'WinnerPosition':winner})

    def post(self,request, *args, **kwargs):
        id = self.kwargs.get('id')
        event_master_id = request.POST['event_master_id']
        winner_position_id = request.POST['winner_position_id']
        participant_id = request.POST['ParticipantHeaderId']
        chest_number = request.POST['chest_number']
        college_name = request.POST['college_name']
        participant_name = request.POST['participant_name']
        participant_registration_header = ParticipantRegistrationHeader.objects.get(pk=participant_id)
        participant_header_id = participant_registration_header.id

        event_result = EventResult.objects.get(pk=id)

        try:
            existing_instance = EventResult.objects.exclude(id=id).get(
            event_master_id=event_master_id,
            winner_position_id=winner_position_id,
            participant_registration_header_id=participant_header_id,
            is_active=1
            )
            print("-------------------------- existing_instance:",existing_instance)
            return HttpResponse("<script>alert('This combination already exists.');window.location='../ViewEventResult';</script>")
        except:
            event_master = get_object_or_404(EventMaster, id=event_master_id)
            winner_position = get_object_or_404(WinnerPositionMasterModel, id=winner_position_id)
            participant_registration_header = get_object_or_404(ParticipantRegistrationHeader,id=participant_header_id)

            event_result.event_master_id=event_master
            event_result.winner_position_id=winner_position
            event_result.participant_registration_header_id=participant_registration_header
            event_result.save()

            if college_name:
                participant_registration_header.college_name=college_name
                participant_registration_header.save()

            if participant_name:
                participant_child = ParticipantRegistrationChild.objects.filter(participant_registration_header_id=participant_registration_header.id).first()
                participant_child.participant_name = participant_name
                participant_child.save()

            if chest_number:
                participant_registration_header.college_name=college_name
                participant_registration_header.save()

        return HttpResponse("<script>alert('updated event result');window.location='../ViewEventResult';</script>")


def delete_event_result(request,id):
    return render(request,"AdminMain/EventResult/delete.html",{'data':id})

def delete_event_result1(request,id):
    EventResult.objects.filter(id=id).update(is_active=0)
    return redirect("ViewEventResult")

def get_participant_names(request):
    if request.method == 'GET':
        event_id = request.GET.get('event_id')  # Assuming the event ID is passed through GET request parameter

        # Fetch participant names based on the provided event ID
        participants = ParticipantRegistrationChild.objects.filter(
            participant_registration_header_id__event_master_id_id=event_id
        ).values('id', 'participant_name')  # Replace 'participant_name' with the actual field name

        # Construct a list of participants with their IDs and names
        participant_list = list(participants)

        # Return participant names as JSON response
        return JsonResponse(participant_list, safe=False)
    else:
        return JsonResponse({'error': 'Invalid request method'})

def get_participant_names1(request):
    if request.method == 'GET':
        event_id = request.GET.get('event_id')
        filter_text = request.GET.get('filter', '')

        participants = ParticipantRegistrationChild.objects.filter(
            participant_registration_header_id__event_master_id_id=event_id,
            participant_name__icontains=filter_text
        ).values('id', 'participant_name')

        participant_list = list(participants)

        return JsonResponse(participant_list, safe=False)
    else:
        return JsonResponse({'error': 'Invalid request method'})


def participant_name(request):
    print("Hello, it's me, participant_name function")

    if request.method == 'GET':
        print("Hello, it's me, participant_name function GET method")

        # Use get_object_or_404 to retrieve the EventMaster instance
        event_id = request.GET.get('event_id')
        event_master = get_object_or_404(EventMaster, pk=event_id)

        # Retrieve the EventId and ParticipantHeader using the EventMaster instance
        EventId = event_master.id
        chest_no = request.GET.get('chest_no')
        participant_header = get_object_or_404(ParticipantRegistrationHeader, event_master_id=EventId, event_chest_no=chest_no)
        college_name = participant_header.college_name
        participant_header_id = participant_header.id
        # Retrieve the ParticipantChild using the ParticipantRegistrationHeader instance
        participant_child = ParticipantRegistrationChild.objects.filter(participant_registration_header_id=participant_header.id).first()

        if participant_child:
            participant_name = participant_child.participant_name
            return JsonResponse({'participant_name': participant_name,'participant_header_id':participant_header_id,'college_name':college_name})
        else:
            return JsonResponse({'error': 'Participant not found for the given chest number and event.'}, status=404)
    else:
        print("Error: Invalid request method")
        return JsonResponse({'error': 'Invalid request method'}, status=400)


def initiate_payment(request):
    amount = 1000  # Amount in paise (Example: 50000 paise = ₹500)
    amount_in_rupees = amount / 100  # Calculate amount in rupees
    client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
    data = { "amount": amount, "currency": "INR", "receipt": "001" }
    payment = client.order.create(data=data)
    return render(request, 'AdminMain/p/test_payment.html', {'payment': payment})

    # payment = client.order.create({'amount': amount, 'currency': 'INR', 'payment_capture': '1'})
    # unique_order_id = str(uuid.uuid4())
    # your_MerchantID_variable = "JCuSrXyhqOW5W8"
    # your_TransactionDesc_variable = "Transaction Description"  # Replace with your actual description
    # your_OnlineTrackId_variable = "Online Tracking ID"  # Replace with your actual tracking ID
    # your_Returnurl_variable = "Your_Return_URL"  # Replace with your return URL
    # your_Name_variable = "John Doe"  # Replace with the name
    # your_Email_variable = "john@example.com"  # Replace with the email
    # your_MobileNumber_variable = "1234567890"  # Replace with the mobile number

    # return render(request, 'AdminMain/p/test_payment.html', {'payment': payment, 'amount_in_rupees': amount_in_rupees, 'unique_order_id': unique_order_id,'your_MerchantID_variable':your_MerchantID_variable,'your_TransactionDesc_variable': your_TransactionDesc_variable,
    #     'your_OnlineTrackId_variable': your_OnlineTrackId_variable,
    #     'your_Returnurl_variable': your_Returnurl_variable,
    #     'your_Name_variable': your_Name_variable,
    #     'your_Email_variable': your_Email_variable,
    #     'your_MobileNumber_variable': your_MobileNumber_variable})

def payment_success(request):
    return render(request, 'AdminMain/p/p_s.html')

class CreateGalleryMaster(View):
    def get(self,request,*args, **kwargs):
        current_date = date.today()
        festival_master = FestivalMasterHeader.objects.filter(is_active=1, to_date__gte=current_date)
        event_master = EventMaster.objects.filter(is_active=1)
        return render(request,'AdminMain/GalleryMaster/create.html',{'festival':festival_master,'EventMaster':event_master})

    def post(self,request,*args, **kwargs):
        return HttpResponse("<script>alert('Successfully added event result gallery');window.location='../ViewGalleryMaster';</script>")

def view_gallery_master(request):
    return render(request,'AdminMain/GalleryMaster/view.html')

class EditGalleryMaster(View):
    def get(self,request,*args, **kwargs):
        return render(request,'AdminMain/GalleryMaster/Edit.html')
    def post(self,request,*args, **kwargs):
        return HttpResponse("<script>alert('Successfully added event result gallery');window.location='../ViewGalleryMaster';</script>")

def delete_gallery_master(request):
    return render(request,'AdminMain/GalleryMaster/delete.html')

def delete_gallery_master1(request):
   return redirect('ViewGalleryMaster')


def student_home(request):
    current_date = date.today()
    matching_data = FestivalMasterChild.objects.select_related('festival_master_header_id').filter(
        festival_master_header_id__is_active=1
        ).exclude(
        Q(festival_master_header_id__to_date__lt=current_date)
        ).values(
        'festival_master_header_id__id',
        'festival_master_header_id__festival_name',
        'festival_master_header_id__festival_icon',
        'festival_master_header_id__festival_banner',
        'festival_master_header_id__from_date',
        'festival_master_header_id__to_date',
        'festival_master_header_id__video_file',
        'id',
        'registration_start_date',
        'registration_end_date'
    )

    sponsor = SponsorMaster.objects.filter(is_active=1, event_master_id__isnull=True).exclude(
        Q(festival_master_header_id__to_date__lt=current_date)
        )
    return render(request,"AdminMain/Student/index.html",{'programs': matching_data,'sponsor':sponsor})

class StudentViewEvents(View):
    # def get(self, request, *args, **kwargs):
    #     festival_id = self.kwargs.get('id')
    #
    #     # Get the FestivalMasterHeader instance or return 404 if not found
    #     festival_master = get_object_or_404(FestivalMasterHeader, id=festival_id)
    #
    #     # Retrieve EventMaster objects related to the FestivalMasterHeader
    #     event_master = EventMaster.objects.filter(
    #         festival_master_header_id=festival_master,
    #         is_active=True
    #     )
    #     print("----------------------------------------------------------", event_master)
    #
    #     return render(request, "Student/view_events.html", {'data': event_master})

    def get(self, request, *args, **kwargs):
        festival_id = self.kwargs.get('id')

        festival_master = get_object_or_404(FestivalMasterHeader, id=festival_id)
        festivalId = festival_master.id
        print("----------------------",festivalId)
        current_date = date.today()
        event_master = EventMaster.objects.filter(
            is_active=1,
            festival_master_header_id__is_active=True,
            festival_master_header_id=festival_master.id,
        ).exclude(
            Q(festival_master_header_id__to_date__lt=current_date)
        )

        # event_info_list = []
        # for event in event_master:
        #     event_scheduler = EventScheduler.objects.get(event_master_id=event.id)
        #
        #     event_info_list.append({
        #         'EventName': event.event_name,
        #         'RegistrationFee': event.registration_fee,
        #         'EventDocument': event.event_document,
        #         'EventType': event.event_type,
        #         'MaxTeamSize': event.max_team_size,
        #         'MinTeamSize': event.min_team_size,
        #         'EventDescription': event.event_description,
        #         'EventStartDate': event_scheduler.event_start_date,
        #         'EventEndDate': event_scheduler.event_end_date,
        #         'id': event.id
        #     })
        event_info_list = []
        for event in event_master:
            try:
                event_scheduler = EventScheduler.objects.get(event_master_id=event.id)

                participant_count = (
                    event
                    .participantregistrationheader_set
                    .filter(participantregistrationpayment__payment_status=1)
                    .aggregate(participant_count=Count('id'))['participant_count']
                )
                event_info_list.append({
                    'EventName': event.event_name,
                    'RegistrationFee': event.registration_fee,
                    'EventDocument': event.event_document,
                    'EventType': event.event_type,
                    'MaxTeamSize': event.max_team_size,
                    'MinTeamSize': event.min_team_size,
                    'EventDescription': event.event_description,
                    'EventStartDate': event_scheduler.event_start_date,
                    'EventEndDate': event_scheduler.event_end_date,
                    'id': event.id,
                    'ParticipantCount': participant_count,
                })
            except EventScheduler.DoesNotExist:
                # Handle the case when EventScheduler does not exist for the current event
                event_info_list.append({
                    'EventName': event.event_name,
                    'RegistrationFee': event.registration_fee,
                    'EventDocument': event.event_document,
                    'EventType': event.event_type,
                    'MaxTeamSize': event.max_team_size,
                    'MinTeamSize': event.min_team_size,
                    'EventDescription': event.event_description,
                    'EventStartDate': None,
                    'EventEndDate': None,
                    'id': event.id
                })

        sponsor = SponsorMaster.objects.filter(is_active=True,festival_master_header_id=festivalId)
        return render(request, "AdminMain/Student/view_events1.html", {'data': event_info_list,'sponsor':sponsor})

# class StudentRegisterEvent(View):
#     def get(self, request, *args, **kwargs):
#         id = self.kwargs.get('id')
#         event_master = get_object_or_404(EventMaster, id=id)
#         event_name =event_master.event_name
#         min_team_size = event_master.min_team_size
#         max_team_size = event_master.max_team_size
#         participant_type = ParticipantTypeMaster.objects.filter(is_active=1)
#         return render(request,'AdminMain/Student/registration.html',{'data':event_master,'event_name':event_name,'min_team_size': min_team_size,'max_team_size':max_team_size,'ParticipantType':participant_type})
#
#     def post(self, request, *args, **kwargs):
#
#         event_master_id = self.kwargs.get('id')
#         college_name = request.POST.get('college_name')
#         receipt_number = random.randint(1000, 9999999)
#         participant_type_id = 1
#
#         event_master = EventMaster.objects.get(pk=event_master_id)
#         abbreviation = event_master.abbreviation
#         chest_number = f"{abbreviation}{ParticipantRegistrationHeader.objects.filter(event_master_id__abbreviation=abbreviation).count() + 1:02d}"
#         # Create ParticipantRegistrationHeader instance with user info
#         registration_header = ParticipantRegistrationHeader.objects.create(
#             event_master_id=event_master,
#             college_name=college_name,
#             event_chest_no=chest_number,
#             receipt_no=receipt_number,
#             is_active=1
#             # Assign other fields accordingly
#         )
#
#         # Access participant details lists sent from the form
#         participant_names = request.POST.getlist('participant_name')
#         participant_phones = request.POST.getlist('participant_phone')
#         participant_email = request.POST.getlist('participant_email')
#         participant_id_nos = request.POST.getlist('participant_id_no')
#         participant_id_images = request.FILES.getlist('participant_id_image')
#
#         first_phone = participant_phones[0]
#         first_email = participant_email[0]
#
#         # Save participant_id_images using FileSystemStorage
#         file_urls = []
#         for participant_id_card in participant_id_images:
#             fss = FileSystemStorage()
#             file = fss.save(participant_id_card.name, participant_id_card)
#             file_url = fss.url(file)
#             file_urls.append(file_url)
#
#
#
#         # Create ParticipantRegistrationChild instances for each participant detail
#         for i in range(len(participant_names)):
#             participant_child = ParticipantRegistrationChild.objects.create(
#                 participant_registration_header_id=registration_header,
#                 participant_name=participant_names[i],
#                 participant_phone=participant_phones[i],
#                 participant_email=participant_email[i],
#                 participant_id_no=participant_id_nos[i],
#                 participant_id_card=file_urls[i],  # Using file URLs saved previously
#                 # Assign other fields accordingly
#             )
#
#         # Process and create ParticipantRegistrationPayment instance
#         registration_fee = event_master.registration_fee
#
#         payment = ParticipantRegistrationPayment.objects.create(
#             participant_registration_header_id=registration_header,
#             registration_fee=registration_fee,
#             # payment_type=payment_type,
#             payment_status=0,
#             created_by="admin"  # Store user who created this entry
#             # Assign other fields accordingly
#         )
#         payment.save()
#         payment_id = payment.id
#         request.session["PaymentID"] = payment_id
#         # registration_fee_float = float(registration_fee)
#         # fee = int(registration_fee_float) * 100
#         #
#         # # csrf_token = get_token(request)
#         # amount = fee  # Amount in paise (Example: 50000 paise = ₹500)
#         # amount_in_rupees = amount / 100  # Calculate amount in rupees
#         # client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
#         #
#         # data = { "amount": amount, "currency": "INR", "receipt": "001" }
#         # payment = client.order.create(data=data)
#
#         sponsor = SponsorMaster.objects.filter(is_active=1)
#         # return render(request, 'AdminMain/Student/razorpay_payment.html', {'payment': payment,'payment_id': payment_id,'sponsor':sponsor,'registration_fee':registration_fee})
#         return render(request, 'AdminMain/Student/Student_payment.html', {'payment': payment,'payment_id': payment_id,'sponsor':sponsor,'registration_fee':registration_fee,'phone':first_phone,'email':first_email})
#         # return render(request, 'AdminMain/Student/testing.html', {'payment': payment,'payment_id': payment_id,'sponsor':sponsor,'registration_fee':registration_fee})
#


class StudentRegisterEvent(View):
    def get(self, request, *args, **kwargs):
        print("-------------------------------------------------------------------")
        id = self.kwargs.get('id')
        event_master = get_object_or_404(EventMaster, id=id)
        event_id = event_master.id
        event_name =event_master.event_name
        min_team_size = event_master.min_team_size
        max_team_size = event_master.max_team_size
        event_description = event_master.event_description
        festival_id = event_master.festival_master_header_id_id
        print('----------------------------',festival_id)
        festival_master = get_object_or_404(FestivalMasterHeader, id=festival_id)
        festivalId = festival_master.id
        print("-------------------------------event id,festival header id",event_id,festivalId)
        participant_type = ParticipantTypeMaster.objects.filter(is_active=1)
        # sponsor = SponsorMaster.objects.filter(is_active=True, event_master_id=event_id,festival_master_header_id = festivalId)
        sponsor = SponsorMaster.objects.filter(is_active=True,festival_master_header_id=festivalId)
        print("----------------------------------------",sponsor)
        return render(request,'AdminMain/Student/registration1.html',{'data':event_master,'event_name':event_name,'min_team_size': min_team_size,'max_team_size':max_team_size,'ParticipantType':participant_type,'event_description':event_description,'sponsor':sponsor})

    def post(self, request, *args, **kwargs):

        event_master_id = self.kwargs.get('id')
        college_name = request.POST.get('college_name')
        reference_by = request.POST['reference_by']
        receipt_number = random.randint(1000, 9999999)
        participant_type_id = 1

        event_master = EventMaster.objects.get(pk=event_master_id)
        festival_id = event_master.festival_master_header_id

        festival_child = FestivalMasterChild.objects.filter(
            festival_master_header_id=festival_id,
            registration_end_date__lt=datetime.now()
            ).first()

        if festival_child:
            # Festival registration has ended, show alert message
            return HttpResponse("<script>alert('Registration ended.');window.location='../StudentHome';</script>")


        event_scheduler_instance = EventScheduler.objects.get(event_master_id = event_master_id,is_active=1)
        print("------------------------------event scheduler instance",event_scheduler_instance)

        print('-----------------------------event_scheduler_instance.event_start_date',event_scheduler_instance.event_start_date)
        # if event_scheduler_instance.event_start_date >= datetime.now():
        #     return HttpResponse("<script>alert('Event registration has ended.');window.location='../StudentHome';</script>")

        if event_scheduler_instance.event_start_date <= datetime.now().date():
            return HttpResponse("<script>alert('Event registration has ended.');window.location='../StudentHome';</script>")

        abbreviation = event_master.abbreviation
        # chest_number = f"{abbreviation}{ParticipantRegistrationHeader.objects.filter(event_master_id__abbreviation=abbreviation).count() + 1:02d}"

        # new code for chest number logic

        latest_registration = ParticipantRegistrationHeader.objects.filter(
            event_master_id=event_master
            ).order_by('-created_on').first()

        if latest_registration:
            # Extract the numeric part of the chest_number and increment it
            latest_chest_number = latest_registration.event_chest_no
            latest_chest_number_numeric = int(latest_chest_number[-2:])
            next_chest_number_numeric = latest_chest_number_numeric + 1
            next_chest_number = f"{abbreviation}{next_chest_number_numeric:02d}"
        else:
            # If there are no existing registrations, set chest_number to the initial value
            next_chest_number = f"{abbreviation}01"

        # if event_master.max_registration and ParticipantRegistrationHeader.objects.filter(event_master_id=event_master).count() >= event_master.max_registration:
        if event_master.max_registration and ParticipantRegistrationHeader.objects.filter(event_master_id=event_master,participantregistrationpayment__payment_status=1).count() >= event_master.max_registration:
            return HttpResponse("<script>alert('Registration limit reached maximum.');window.location='../StudentHome';</script>")

        # Create ParticipantRegistrationHeader instance with user info
        registration_header = ParticipantRegistrationHeader.objects.create(
            event_master_id=event_master,
            college_name=college_name,
            reference_by=reference_by,
            event_chest_no=next_chest_number,
            receipt_no=receipt_number,
            is_active=1
            # Assign other fields accordingly
        )

        participant_category_instance = event_master.participant_category_id
        participant_category_name = participant_category_instance.participant_category_name

        # Access participant details lists sent from the form
        participant_type = request.POST.getlist('participant_type')
        participant_names = request.POST.getlist('participant_name')
        participant_phones = request.POST.getlist('participant_phone')
        participant_email = request.POST.getlist('participant_email')
        participant_id_nos = request.POST.getlist('participant_id_no')
        participant_id_images = request.FILES.getlist('participant_id_image')

        first_phone = participant_phones[0]
        first_email = participant_email[0]

        # Save participant_id_images using FileSystemStorage
        file_urls = []
        for participant_id_card in participant_id_images:
            fss = FileSystemStorage()
            file = fss.save(participant_id_card.name, participant_id_card)
            file_url = fss.url(file)
            file_urls.append(file_url)

        # Check if participants with the same details already exist for the given EventMaster
        existing_participants = ParticipantRegistrationChild.objects.filter(
            # participant_registration_header_id__event_master_id=event_master,
            participant_phone__in=participant_phones,
            participant_email__in=participant_email,
            participant_id_no__in=participant_id_nos,
            participant_registration_header_id__event_master_id__festival_master_header_id=festival_id,
            participant_registration_header_id__in=ParticipantRegistrationPayment.objects.filter(
            payment_status=1
            ).values('participant_registration_header_id')
        )
        if existing_participants:
                return HttpResponse("<script>alert('Already registered ');window.location='../StudentHome';</script>")

        if participant_category_name == 'Group':
            team_leader_type_name = 'Team Leader'
            team_leader_type = ParticipantTypeMaster.objects.filter(participant_type=team_leader_type_name, is_active=1).first()
            if team_leader_type:
                team_leader_type_id = team_leader_type.id
            else:
                # Create a new ParticipantTypeMaster for Team Leader if not exists
                team_leader_type = ParticipantTypeMaster.objects.create(
                    participant_type=team_leader_type_name,
                    created_by="admin",
                    is_active=1
                )
                team_leader_type_id = team_leader_type.id
        else:
            team_leader_type_id = None  # Set to None for Single participants


        for i in range(len(participant_names)):
            # Determine the correct participant_type_id based on the role (Team Leader or Team Member)
            if i == 0 and participant_category_name == 'Group':
                participant_type_instance = team_leader_type
            else:
                # Check if the ParticipantTypeMaster with the given name and is_active=1 exists
                existing_participant_type = ParticipantTypeMaster.objects.filter(participant_type=participant_type[i], is_active=1).first()
                if existing_participant_type:
                    participant_type_instance = existing_participant_type
                else:
                    # Create a new ParticipantTypeMaster if not exists
                    new_participant_type = ParticipantTypeMaster.objects.create(
                        participant_type=participant_type[i],
                        created_by="admin",
                        is_active=1
                    )
                    participant_type_instance = new_participant_type

            participant_child = ParticipantRegistrationChild.objects.create(
                participant_registration_header_id=registration_header,
                participant_name=participant_names[i],
                participant_phone=participant_phones[i],
                participant_email=participant_email[i],
                participant_id_no=participant_id_nos[i],
                participant_id_card=file_urls[i],
                participant_type_id=participant_type_instance,  # Assign the instance, not the ID
                # created_by="admin"
                # Assign other fields accordingly
            )


        # Process and create ParticipantRegistrationPayment instance
        registration_fee = event_master.registration_fee

        payment = ParticipantRegistrationPayment.objects.create(
            participant_registration_header_id=registration_header,
            registration_fee=registration_fee,
            # payment_type=payment_type,
            payment_status=0,
            # created_by="admin"  # Store user who created this entry
            # Assign other fields accordingly
        )
        payment.save()
        payment_id = payment.id
        request.session["PaymentID"] = payment_id

        sponsor = SponsorMaster.objects.filter(is_active=1)
        # return render(request, 'AdminMain/Student/razorpay_payment.html', {'payment': payment,'payment_id': payment_id,'sponsor':sponsor,'registration_fee':registration_fee})
        # return render(request, 'AdminMain/Student/testing.html', {'payment': payment,'payment_id': payment_id,'sponsor':sponsor,'registration_fee':registration_fee})
        # return render(request, 'AdminMain/Student/Student_payment1.html', {'payment': payment,'payment_id': payment_id,'sponsor':sponsor,'registration_fee':registration_fee,'phone':first_phone,'email':first_email})
        return render(request, 'AdminMain/Student/Student_payment_test.html', {'payment': payment,'payment_id': payment_id,'sponsor':sponsor,'registration_fee':registration_fee,'phone':first_phone,'email':first_email})


# class StudentRegisterEvent(View):
#     def get(self, request, *args, **kwargs):
#         print("-------------------------------------------------------------------")
#         id = self.kwargs.get('id')
#         event_master = get_object_or_404(EventMaster, id=id)
#         event_id = event_master.id
#         event_name =event_master.event_name
#         min_team_size = event_master.min_team_size
#         max_team_size = event_master.max_team_size
#         event_description = event_master.event_description
#         festival_id = event_master.festival_master_header_id_id
#         print('----------------------------',festival_id)
#         festival_master = get_object_or_404(FestivalMasterHeader, id=festival_id)
#         festivalId = festival_master.id
#         print("-------------------------------event id,festival header id",event_id,festivalId)
#         participant_type = ParticipantTypeMaster.objects.filter(is_active=1)
#         # sponsor = SponsorMaster.objects.filter(is_active=True, event_master_id=event_id,festival_master_header_id = festivalId)
#         sponsor = SponsorMaster.objects.filter(is_active=True,festival_master_header_id=festivalId)
#         print("----------------------------------------",sponsor)
#         return render(request,'AdminMain/Student/registration1.html',{'data':event_master,'event_name':event_name,'min_team_size': min_team_size,'max_team_size':max_team_size,'ParticipantType':participant_type,'event_description':event_description,'sponsor':sponsor})
#
#     def post(self, request, *args, **kwargs):
#
#         event_master_id = self.kwargs.get('id')
#         college_name = request.POST.get('college_name')
#         reference_by = request.POST['reference_by']
#         receipt_number = random.randint(1000, 9999999)
#         participant_type_id = 1
#
#         event_master = EventMaster.objects.get(pk=event_master_id)
#         festival_id = event_master.festival_master_header_id
#
#
#         abbreviation = event_master.abbreviation
#         chest_number = f"{abbreviation}{ParticipantRegistrationHeader.objects.filter(event_master_id__abbreviation=abbreviation).count() + 1:02d}"
#
#         if event_master.max_registration and ParticipantRegistrationHeader.objects.filter(event_master_id=event_master).count() >= event_master.max_registration:
#             return HttpResponse("<script>alert('Registration limit reached maximum.');window.location='../StudentHome';</script>")
#
#         # Create ParticipantRegistrationHeader instance with user info
#         registration_header = ParticipantRegistrationHeader.objects.create(
#             event_master_id=event_master,
#             college_name=college_name,
#             reference_by=reference_by,
#             event_chest_no=chest_number,
#             receipt_no=receipt_number,
#             is_active=1
#             # Assign other fields accordingly
#         )
#
#         participant_category_instance = event_master.participant_category_id
#         participant_category_name = participant_category_instance.participant_category_name
#
#         # Access participant details lists sent from the form
#         participant_type = request.POST.getlist('participant_type')
#         participant_names = request.POST.getlist('participant_name')
#         participant_phones = request.POST.getlist('participant_phone')
#         participant_email = request.POST.getlist('participant_email')
#         participant_id_nos = request.POST.getlist('participant_id_no')
#         participant_id_images = request.FILES.getlist('participant_id_image')
#
#         first_phone = participant_phones[0]
#         first_email = participant_email[0]
#
#         # Save participant_id_images using FileSystemStorage
#         file_urls = []
#         for participant_id_card in participant_id_images:
#             fss = FileSystemStorage()
#             file = fss.save(participant_id_card.name, participant_id_card)
#             file_url = fss.url(file)
#             file_urls.append(file_url)
#
#         # Check if participants with the same details already exist for the given EventMaster
#         existing_participants = ParticipantRegistrationChild.objects.filter(
#             # participant_registration_header_id__event_master_id=event_master,
#             participant_phone__in=participant_phones,
#             participant_email__in=participant_email,
#             participant_id_no__in=participant_id_nos,
#             participant_registration_header_id__event_master_id__festival_master_header_id=festival_id,
#             participant_registration_header_id__in=ParticipantRegistrationPayment.objects.filter(
#             payment_status=1
#             ).values('participant_registration_header_id')
#         )
#         if existing_participants:
#                 return HttpResponse("<script>alert('Already registered ');window.location='../StudentHome';</script>")
#
#         if participant_category_name == 'Group':
#             team_leader_type_name = 'Team Leader'
#             team_leader_type = ParticipantTypeMaster.objects.filter(participant_type=team_leader_type_name, is_active=1).first()
#             if team_leader_type:
#                 team_leader_type_id = team_leader_type.id
#             else:
#                 # Create a new ParticipantTypeMaster for Team Leader if not exists
#                 team_leader_type = ParticipantTypeMaster.objects.create(
#                     participant_type=team_leader_type_name,
#                     created_by="admin",
#                     is_active=1
#                 )
#                 team_leader_type_id = team_leader_type.id
#         else:
#             team_leader_type_id = None  # Set to None for Single participants
#
#
#         for i in range(len(participant_names)):
#             # Determine the correct participant_type_id based on the role (Team Leader or Team Member)
#             if i == 0 and participant_category_name == 'Group':
#                 participant_type_instance = team_leader_type
#             else:
#                 # Check if the ParticipantTypeMaster with the given name and is_active=1 exists
#                 existing_participant_type = ParticipantTypeMaster.objects.filter(participant_type=participant_type[i], is_active=1).first()
#                 if existing_participant_type:
#                     participant_type_instance = existing_participant_type
#                 else:
#                     # Create a new ParticipantTypeMaster if not exists
#                     new_participant_type = ParticipantTypeMaster.objects.create(
#                         participant_type=participant_type[i],
#                         created_by="admin",
#                         is_active=1
#                     )
#                     participant_type_instance = new_participant_type
#
#             participant_child = ParticipantRegistrationChild.objects.create(
#                 participant_registration_header_id=registration_header,
#                 participant_name=participant_names[i],
#                 participant_phone=participant_phones[i],
#                 participant_email=participant_email[i],
#                 participant_id_no=participant_id_nos[i],
#                 participant_id_card=file_urls[i],
#                 participant_type_id=participant_type_instance,  # Assign the instance, not the ID
#                 # created_by="admin"
#                 # Assign other fields accordingly
#             )
#
#
#         # Process and create ParticipantRegistrationPayment instance
#         registration_fee = event_master.registration_fee
#
#         payment = ParticipantRegistrationPayment.objects.create(
#             participant_registration_header_id=registration_header,
#             registration_fee=registration_fee,
#             # payment_type=payment_type,
#             payment_status=0,
#             # created_by="admin"  # Store user who created this entry
#             # Assign other fields accordingly
#         )
#         payment.save()
#         payment_id = payment.id
#         request.session["PaymentID"] = payment_id
#
#         sponsor = SponsorMaster.objects.filter(is_active=1)
#         # return render(request, 'AdminMain/Student/razorpay_payment.html', {'payment': payment,'payment_id': payment_id,'sponsor':sponsor,'registration_fee':registration_fee})
#         return render(request, 'AdminMain/Student/Student_payment1.html', {'payment': payment,'payment_id': payment_id,'sponsor':sponsor,'registration_fee':registration_fee,'phone':first_phone,'email':first_email})
#         # return render(request, 'AdminMain/Student/testing.html', {'payment': payment,'payment_id': payment_id,'sponsor':sponsor,'registration_fee':registration_fee})


   #      client.utility.verify_payment_signature({
   # 'razorpay_order_id': razorpay_order_id,
   # 'razorpay_payment_id': razorpay_payment_id,
   # 'razorpay_signature': razorpay_signature
   # })

        # client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
        # payment = client.order.create({'amount': amount, 'currency': 'INR', 'payment_capture': '1'})
        # unique_order_id = str(uuid.uuid4())
        # your_MerchantID_variable = "JCuSrXyhqOW5W8"
        # your_TransactionDesc_variable = "Transaction Description"  # Replace with your actual description
        # your_OnlineTrackId_variable = "Online Tracking ID"  # Replace with your actual tracking ID
        # your_Returnurl_variable = ""  # Replace with your return URL
        # your_Name_variable = ""  # Replace with the name
        # your_Email_variable = ""  # Replace with the email
        # your_MobileNumber_variable = ""  # Replace with the mobile number
        #
        # return render(request, 'AdminMain/Student/razorpay.html', {
        #     'payment': payment, 'amount_in_rupees': amount_in_rupees,
        #     'unique_order_id': unique_order_id, 'your_MerchantID_variable':your_MerchantID_variable,
        #     'your_TransactionDesc_variable': your_TransactionDesc_variable,
        #     'your_OnlineTrackId_variable': your_OnlineTrackId_variable,
        #     'your_Returnurl_variable': your_Returnurl_variable,
        #     'your_Name_variable': your_Name_variable,
        #     'your_Email_variable': your_Email_variable,
        #     'your_MobileNumber_variable': your_MobileNumber_variable})
        #     # 'csrf_token': csrf_token})

@csrf_exempt
def create_order(request):
    print("Hi create order function ")
    if request.method == 'POST':
        print("Hi create order post method  ")

        registration_fee = request.POST.get('registration_fee')
        amount = int(registration_fee)  # Set your amount here (in paisa)

        client = razorpay.Client(auth=(razorpay_key_id, razorpay_key_secret))
        currency = 'INR'  # Set your currency code here

        data = {
            'amount': amount*100,
            'currency': currency,
            'receipt': 'order_rcptid_11',
        }

        order = client.order.create(data=data)
        order_id = order['id']
        print("----------------------------------order and order_id",order,order_id)
        return JsonResponse({'order_id': order_id, 'razorpay_key_id': razorpay_key_id, 'amount': amount})

    return JsonResponse({'error': 'Invalid request method'})

# def verify_payment(request):
#     print("hello its me verify payment function ")
#     if request.method == 'POST':
#         print("hello its me verify payment post method ")
#         # razorpay_order_id = request.POST.get('razorpay_order_id')
#         # razorpay_payment_id = request.POST.get('razorpay_payment_id')
#         # razorpay_signature = request.POST.get('razorpay_signature')
#
#         raw_data = request.body.decode('utf-8')
#
#         # Parse the JSON data
#         data = json.loads(raw_data)
#
#         # Extract values from the nested structure
#         razorpay_order_id = data.get('razorpay_order_id')
#         razorpay_payment_id = data.get('razorpay_payment_id')
#         razorpay_signature = data.get('razorpay_signature')
#
#         payment_id = data.get('payment_id')
#
#         # payment_id = request.POST.get('payment_id')
#         print("------------------------razorpay_order_id",razorpay_order_id)
#         print("------------------------razorpay_payment_id",razorpay_payment_id)
#         print("------------------------razorpay_signature",razorpay_signature)
#         print("------------------------payment_id",payment_id)
#         print("----------------sdfsgsgsga")
#
#         secret = razorpay_key_secret.encode('utf-8')
#         payload = f'{razorpay_order_id}|{razorpay_payment_id}'.encode('utf-8')
#         generated_signature = hmac.new(secret, payload, hashlib.sha256).hexdigest()
#
#         print("Generate signature and razorpay signature",generated_signature,razorpay_signature,razorpay_order_id,razorpay_payment_id)
#         if generated_signature == razorpay_signature:
#             print("Success")
#             # Payment is successful
#             payment_instance = ParticipantRegistrationPayment.objects.get(id=payment_id)
#             payment_instance.payment_status=4
#             payment_instance.is_active = True
#             payment_instance.save()
#             return JsonResponse({'status': 'success'})
#         else:
#             print("Failed")
#             # Payment verification failed
#             return JsonResponse({'status': 'failure', 'message': 'Payment verification failed'})
#
#     return JsonResponse({'error': 'Invalid request method'})


def verify_payment(request):
    print("hello its me verify payment function ")
    if request.method == 'POST':
        print("hello its me verify payment post method ")
        try:
            print("Hii try")
            # razorpay_order_id = request.POST.get('razorpay_order_id')
            # razorpay_payment_id = request.POST.get('razorpay_payment_id')
            # razorpay_signature = request.POST.get('razorpay_signature')

            # raw_data = request.body.decode('utf-8')

            # Print or log the raw data for debugging
            # print("Raw Data:", raw_data)

            # Parse the JSON data
            # data = json.loads(raw_data)

            # Extract values from the nested structure
            razorpay_order_id = request.POST.get('razorpay_order_id')
            razorpay_payment_id =  request.POST.get('razorpay_payment_id')
            razorpay_signature =  request.POST.get('razorpay_signature')
            payment_id =  request.POST.get('payment_id')


            # payment_id = request.POST.get('payment_id')
            print("------------------------razorpay_order_id",razorpay_order_id)
            print("------------------------razorpay_payment_id",razorpay_payment_id)
            print("------------------------razorpay_signature",razorpay_signature)
            print("------------------------payment_id",payment_id)

            secret = razorpay_key_secret.encode('utf-8')
            payload = f'{razorpay_order_id}|{razorpay_payment_id}'.encode('utf-8')
            generated_signature = hmac.new(secret, payload, hashlib.sha256).hexdigest()

            # print("Generate signature and razorpay signature",generated_signature,razorpay_signature,razorpay_order_id,razorpay_payment_id)
            if generated_signature == razorpay_signature:
                print("Success")
                # Payment is successful
                payment_instance = ParticipantRegistrationPayment.objects.get(id=payment_id)
                payment_instance.payment_status=1
                payment_instance.transaction_id = razorpay_payment_id
                payment_instance.is_active = True
                payment_instance.save()
                return JsonResponse({'status': 'success'})
            else:
                print("Failed")
                # Payment verification failed
                return JsonResponse({'status': 'failure', 'message': 'Payment verification failed'})

        except json.JSONDecodeError as e:
            print(f"JSON Decode Error: {e}")
            return JsonResponse({'status': 'failure', 'message': 'Invalid JSON data'})

    return JsonResponse({'error': 'Invalid request method'})

def Student_pay_slip(request):
    return render(request,'AdminMain/ParticipantRegistration/pay_slip.html')

def Slip(request):
    return render(request,"AdminMain/ParticipantRegistration/Slip.html")
# @csrf_exempt
# def create_order(request):
#     if request.method == 'POST':
#         print("-----------------------------------------------------------")
#         registration_fee = request.POST.get('registration_fee')
#         amount = int(registration_fee)  # Set your amount here (in paisa)
#
#         currency = 'INR'  # Set your currency code here
#
#         data = {
#             'amount': amount*100,
#             'currency': currency,
#             'receipt': 'order_rcptid_11',
#         }
#
#         response = requests.post('https://api.razorpay.com/v1/orders',
#                                  auth=(razorpay_key_id, razorpay_key_secret),
#                                  json=data)
#
#         if response.status_code == 200:
#             razorpay_order_data = response.json()
#             # Extract relevant information from razorpay_order_data
#             return JsonResponse({'success': True, 'razorpay_order_id': razorpay_order_data['id']})
#         else:
#             return JsonResponse({'success': False, 'error_message': response.text})
#
#     return JsonResponse({'error': 'Invalid request method'})
#
#
# def create_transfer(request):
#     if request.method == 'POST':
#         # Assuming you have a recipient's bank account ID
#         recipient_bank_account_id = 'acc_LzorlYRcQivyLm'
#         print("-----------------------------------------------------create_transfer")
#         client = razorpay.Client(auth=(razorpay_key_id, razorpay_key_secret))
#         registration_fee = int(request.POST.get('registration_fee'))
#         currency = 'INR'
#
#         transfer_data = {
#             'account': recipient_bank_account_id,
#             'amount': registration_fee * 100,
#             'currency': currency,
#             'notes': {
#                 'branch': '',
#                 'name': ''
#             },
#             'linked_account_notes': ['branch'],
#             'on_hold': False,
#         }
#
#         transfer = client.transfer.create(data=transfer_data)
#         transfer_id = transfer['id']
#
#         return JsonResponse({'transfer_id': transfer_id, 'amount': registration_fee})
#
#     return JsonResponse({'error': 'Invalid request method'})

# @csrf_exempt
# def create_order(request):
#     if request.method == 'POST':
#         registration_fee = request.POST.get('registration_fee')
#         amount = int(registration_fee)  # Set your amount here (in paisa)
#         print("---------------------------------------------",amount)
#         # Replace [YOUR_RAZORPAY_KEY_ID] and [YOUR_RAZORPAY_KEY_SECRET] with your actual Razorpay API key ID and secret
#
#         # Create order using Razorpay Orders API
#         orders_api_url = "https://api.razorpay.com/v1/orders"
#         headers = {
#             'content-type': 'application/json',
#         }
#
#         data = {
#             'amount': amount * 100,
#             'currency': 'INR',
#             'transfers': [
#                 {
#                     'account': 'acc_LzorlYRcQivyLm',
#                     'amount': amount*100,
#                     'currency': 'INR',
#                     'notes': {
#                         'branch': '',
#                         'name': '',
#                     },
#                     'linked_account_notes': ['branch'],
#                     'on_hold': 0,
#                     'on_hold_until': '',
#                 },
#             ],
#         }
#
#         response = requests.post(orders_api_url, data=json.dumps(data), headers=headers, auth=(razorpay_key_id, razorpay_key_secret))
#         order_data = response.json()
#
#         order_id = order_data.get('id')
#
#         return JsonResponse({'order_id': order_id, 'razorpay_key_id': razorpay_key_id, 'amount': amount})
#
#     return JsonResponse({'error': 'Invalid request method'})
#
# @csrf_exempt
# def verify_payment(request):
#     if request.method == 'POST':
#         razorpay_order_id = request.POST.get('razorpay_order_id')
#         razorpay_payment_id = request.POST.get('razorpay_payment_id')
#         razorpay_signature = request.POST.get('razorpay_signature')
#
#         payment_id = request.POST.get('payment_id')
#
#         secret = razorpay_key_secret.encode('utf-8')
#         payload = f'{razorpay_order_id}|{razorpay_payment_id}'.encode('utf-8')
#         generated_signature = hmac.new(secret, payload, hashlib.sha256).hexdigest()
#
#         if generated_signature == razorpay_signature:
#             # Payment is successful
#             payment_instance = ParticipantRegistrationPayment.objects.get(id=payment_id)
#             payment_instance.is_active = True
#             payment_instance.save()
#             return JsonResponse({'status': 'success'})
#         else:
#             # Payment verification failed
#             return JsonResponse({'status': 'failure', 'message': 'Payment verification failed'})
#
#     return JsonResponse({'error': 'Invalid request method'})

def participant_list_report(request):
    festival_master = FestivalMasterHeader.objects.filter(is_active=1)
    event_master = EventMaster.objects.filter(is_active=1)
    return render(request,'AdminMain/Report/ParticipantList.html',{'festival':festival_master,'EventMaster':event_master})

class GetEventListCategoriesView(View):
    def get(self, request, *args, **kwargs):
        festival_id = request.GET.get('festival_id')
        # # Fetch Event Categories based on the selected Festival ID
        # if festival_id:
        #     event_categories = EventMaster.objects.filter(festival_master_header_id=festival_id,is_active=1).values('id','event_category_id__event_category_name')
        #
        #     categories_list = list(event_categories)

        Participants = ParticipantRegistrationChild.objects.filter(
        participant_registration_header_id__event_master_id__festival_master_header_id=festival_id,
        participant_registration_header_id__participantregistrationpayment__payment_status=1
        ).order_by('participant_registration_header_id__event_chest_no')

        response_data = []
        for participant in Participants:
            participant_info = {
                'participant_chest_no':participant.participant_registration_header_id.event_chest_no,
                'participant_name': participant.participant_name,
                'college_name': participant.participant_registration_header_id.college_name,
                'participant_phone': participant.participant_phone,
                'participant_email': participant.participant_email,
                'reference_by': participant.participant_registration_header_id.reference_by,
                'participant_id_card': participant.participant_id_no,
                'id':participant.id
                # Include other fields as needed
            }
            response_data.append(participant_info)

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

            print('---------------',unique_categories)

            data = {
                'unique_categories':unique_categories,
                'Participants':response_data,
            }
            return JsonResponse(data, safe=False)
        else:
            return JsonResponse([], safe=False)

# class GetEventListCategoriesView(View):
#     def get(self, request, *args, **kwargs):
#         festival_id = request.GET.get('festival_id')
#         page_number = request.GET.get('page')  # Get the page number from the request
#
#         # Your existing code for fetching participants
#         Participants = ParticipantRegistrationChild.objects.filter(
#             participant_registration_header_id__event_master_id__festival_master_header_id=festival_id,
#             participant_registration_header_id__participantregistrationpayment__payment_status=1
#         ).order_by('participant_registration_header_id__event_chest_no')
#
#         # Pagination
#         paginator = Paginator(Participants, 10)  # Show 10 participants per page
#
#         try:
#             participants_page = paginator.page(page_number)
#         except PageNotAnInteger:
#             participants_page = paginator.page(1)
#         except EmptyPage:
#             participants_page = paginator.page(paginator.num_pages)
#
#         # Format the response data
#         response_data = {
#             'Participants': [{
#                 'participant_chest_no': participant.participant_registration_header_id.event_chest_no,
#                 'participant_name': participant.participant_name,
#                 'college_name': participant.participant_registration_header_id.college_name,
#                 'participant_phone': participant.participant_phone,
#                 'participant_email': participant.participant_email,
#                 'reference_by': participant.participant_registration_header_id.reference_by,
#                 'participant_id_card': participant.participant_id_no,
#                 'id': participant.id
#             } for participant in participants_page],
#             'has_next': participants_page.has_next(),
#             'has_previous': participants_page.has_previous(),
#             'total_pages': paginator.num_pages
#         }
#
#         return JsonResponse(response_data)

class GetParticipantListCategory(View):
    def get(self, request, *args, **kwargs):
        print("----------------------------GetParticipantCategory")
        event_category_id = request.GET.get('eventcategoryid')
        festival_id = request.GET.get('festival_id')
        Participants = ParticipantRegistrationChild.objects.filter(
        participant_registration_header_id__event_master_id__festival_master_header_id=festival_id,
        participant_registration_header_id__event_master_id__event_category_id=event_category_id,
        participant_registration_header_id__participantregistrationpayment__payment_status=1
        ).order_by('participant_registration_header_id__event_chest_no')

        response_data = []
        for participant in Participants:
            participant_info = {
                'participant_chest_no':participant.participant_registration_header_id.event_chest_no,
                'participant_name': participant.participant_name,
                'college_name': participant.participant_registration_header_id.college_name,
                'participant_phone': participant.participant_phone,
                'participant_email': participant.participant_email,
                'reference_by': participant.participant_registration_header_id.reference_by,
                'participant_id_card': participant.participant_id_no,
                'id':participant.id
                # Include other fields as needed
            }
            response_data.append(participant_info)

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
            data = {
                'unique_categories':unique_categories,
                'Participants':response_data,
            }
            return JsonResponse(data, safe=False)
        else:
            return JsonResponse([], safe=False)


class GetEventMasterList(View):
    def get(self, request, *args, **kwargs):
        participant_id = request.GET.get('participant_id')
        event_category_id = request.GET.get('event_category_id')
        festival_id = request.GET.get('festival_id')
        print("-------------------------------------------------------------------",participant_id,event_category_id,festival_id)
        festival = FestivalMasterHeader.objects.get(pk = festival_id)

        Participants = ParticipantRegistrationChild.objects.filter(
        participant_registration_header_id__event_master_id__festival_master_header_id=festival_id,
        participant_registration_header_id__event_master_id__event_category_id=event_category_id,
        participant_registration_header_id__event_master_id__participant_category_id=participant_id,
        participant_registration_header_id__participantregistrationpayment__payment_status=1
        ).order_by('participant_registration_header_id__event_chest_no')

        response_data = []
        for participant in Participants:
            participant_info = {
                'participant_chest_no':participant.participant_registration_header_id.event_chest_no,
                'participant_name': participant.participant_name,
                'college_name': participant.participant_registration_header_id.college_name,
                'participant_phone': participant.participant_phone,
                'participant_email': participant.participant_email,
                'reference_by': participant.participant_registration_header_id.reference_by,
                'participant_id_card': participant.participant_id_no,
                'id':participant.id
                # Include other fields as needed
            }
            response_data.append(participant_info)

       # Fetch Event Categories based on the selected Festival ID
        if participant_id:
            event_master = EventMaster.objects.filter(
                participant_category_id=participant_id,
                event_category_id = event_category_id,
                festival_master_header_id = festival,
                is_active=1
            ).values('id', 'event_name')

            # Manually remove duplicates based on 'id'
            unique_categories = []
            seen_ids = set()
            for category in event_master:
                category_id = category['id']
                if category_id not in seen_ids:
                    unique_categories.append(category)
                    seen_ids.add(category_id)

            data = {
                'unique_categories':unique_categories,
                'Participants':response_data,
            }
            return JsonResponse(data, safe=False)
        else:
            return JsonResponse([], safe=False)


def participant_statistics_report(request):
    festival_master = FestivalMasterHeader.objects.filter(is_active=1)
    event_master = EventMaster.objects.filter(is_active=1)
    return render(request,'AdminMain/Report/RegistrationStatisticsReport.html',{'festival':festival_master,'EventMaster':event_master})

class GetEventMasterReport(View):
    def get(self, request, *args, **kwargs):
        festival_id = request.GET.get('festival_id')

        if festival_id:
            try:
                festival_instance = FestivalMasterHeader.objects.get(pk=festival_id)
                events = EventMaster.objects.filter(festival_master_header_id=festival_instance.id,is_active=1)

                event_data = []
                for event in events:
                    max_registration = event.max_registration
                    # Filter based on payment_status and include only successful payments (payment_status = 1)
                    teams_registered = ParticipantRegistrationHeader.objects.filter(
                        event_master_id=event.id,
                        participantregistrationpayment__payment_status=1
                    ).count()

                    event_data.append({
                        'event_name': event.event_name,
                        'max_registration': max_registration,
                        'teams_registered': teams_registered,
                    })

                return JsonResponse({'event_data': event_data, 'selected_festival': festival_instance.festival_name})

            except FestivalMasterHeader.DoesNotExist:
                # Handle the case where the selected festival does not exist
                return JsonResponse({'error': 'Selected festival not found'}, status=400)

        return JsonResponse({'error': 'No festival selected'}, status=400)


def result_report(request):
    festival_master = FestivalMasterHeader.objects.filter(is_active=1)
    return render(request,'AdminMain/Report/ResultReport.html',{'festival':festival_master})

# def GetResultReport(request):
#     if request.method == 'GET':
#         festival_id = request.GET.get('festival_id')
#
#         # Assuming you have a FestivalMasterHeader model with 'id' as its primary key
#         # Replace 'FestivalMasterHeader' with the actual model name if different
#         festival = get_object_or_404(FestivalMasterHeader, id=festival_id)
#
#         # Fetch relevant data based on your models and relationships
#         event_results_data = EventResult.objects.filter(
#             event_master_id__festival_master_header_id=festival.id,
#             is_active=True,
#             winner_position_id__is_active=True
#         ).order_by('event_master_id', 'winner_position_id__winner_position')
#
#         # Group the results by event
#         grouped_results = {key: list(group) for key, group in groupby(event_results_data, key=lambda x: x.event_master_id)}
#
#         # Iterate through the groups and append to event_results
#         event_results = []
#         for event_id, results in grouped_results.items():
#             for position, result in enumerate(results, start=1):
#                 event = result.event_master_id
#                 participant_header = result.participant_registration_header_id
#                 participants = ParticipantRegistrationChild.objects.filter(participant_registration_header_id=participant_header.id)
#
#                 for participant in participants:
#                     # Fetch additional data as needed
#                     winner_position = result.winner_position_id
#                     participant_type = participant.participant_type_id
#
#                     # Append relevant data to event_results
#                     event_results.append({
#                         'event_name': event.event_name if event else None,
#                         'participant_name': participant.participant_name if participant else None,
#                         'event_chest_no': participant_header.event_chest_no if participant_header else None,
#                         'college_name': participant_header.college_name if participant_header else None,
#                         'position': winner_position.winner_position if winner_position else None,
#                         'participant_type': participant_type.participant_type if participant_type else None,
#                     })
#
#         # Return the data as a JSON response
#         return JsonResponse({'event_results': event_results})
#
#     return JsonResponse({'error': 'Invalid request method'}, status=400)

def GetResultReport(request):
    if request.method == 'GET':
        festival_id = request.GET.get('festival_id')
        if festival_id:
            event_names = EventMaster.objects.filter(
                festival_master_header_id=festival_id, is_active=1
            ).values('id', 'event_name')
            unique_events = []
            print(event_names)
            seen_ids = set()
            for event in event_names:
                event_id = event['id']
                if event_id not in seen_ids:
                    unique_events.append(event)
                    seen_ids.add(event_id)

        # Assuming you have a FestivalMasterHeader model with 'id' as its primary key
        # Replace 'FestivalMasterHeader' with the actual model name if different
        festival = get_object_or_404(FestivalMasterHeader, id=festival_id)

        # Fetch relevant data based on your models and relationships
        event_results_data = EventResult.objects.filter(
            event_master_id__festival_master_header_id=festival.id,
            is_active=True,
            winner_position_id__is_active=True
        ).order_by('event_master_id', 'winner_position_id__winner_position')

        # Group the results by event
        grouped_results = {key: list(group) for key, group in groupby(event_results_data, key=lambda x: x.event_master_id)}

        # Iterate through the groups and append to event_results
        event_results = []
        for event_id, results in grouped_results.items():
            for position, result in enumerate(results, start=1):
                event = result.event_master_id
                participant_header = result.participant_registration_header_id
                participants = ParticipantRegistrationChild.objects.filter(participant_registration_header_id=participant_header.id)

                for participant in participants:
                    # Fetch additional data as needed
                    winner_position = result.winner_position_id
                    participant_type = participant.participant_type_id

                    # Append relevant data to event_results
                    event_results.append({
                        'event_name': event.event_name if event else None,
                        'participant_name': participant.participant_name if participant else None,
                        'event_chest_no': participant_header.event_chest_no if participant_header else None,
                        'college_name': participant_header.college_name if participant_header else None,
                        'position': winner_position.winner_position if winner_position else None,
                        'participant_type': participant_type.participant_type if participant_type else None,
                    })
        data = {
            'unique_events':unique_events,
            'event_results':event_results,
        }

        # Return the data as a JSON response
        return JsonResponse(data)

    return JsonResponse({'error': 'Invalid request method'}, status=400)


# def GetResultReport(request):
#     if request.method == 'GET':
#         festival_id = request.GET.get('festival_id')
#
#         # Assuming you have a FestivalMasterHeader model with 'id' as its primary key
#         # Replace 'FestivalMasterHeader' with the actual model name if different
#         festival = get_object_or_404(FestivalMasterHeader, id=festival_id)
#
#         # Fetch relevant data based on your models and relationships
#         event_results_data = EventResult.objects.filter(
#             event_master_id__festival_master_header_id=festival.id,
#             is_active=True,
#             winner_position_id__is_active=True
#         ).order_by('event_master_id', 'winner_position_id__winner_position')
#
#         # Group the results by event
#         grouped_results = {key: list(group) for key, group in groupby(event_results_data, key=lambda x: x.event_master_id)}
#
#         # Iterate through the groups and append to event_results
#         event_results = []
#         for event_id, results in grouped_results.items():
#             for position, result in enumerate(results, start=1):
#                 event = result.event_master_id
#                 participant_header = result.participant_registration_header_id
#                 participants = ParticipantRegistrationChild.objects.filter(participant_registration_header_id=participant_header.id)
#
#                 for participant in participants:
#                     # Append relevant data to event_results
#                     event_results.append({
#                         'event_name': event.event_name if event else None,
#                         'participant_name': participant.participant_name if participant else None,
#                         'event_chest_no': participant_header.event_chest_no if participant_header else None,
#                         'college_name': participant_header.college_name if participant_header else None,
#                         'position': result.winner_position_id.winner_position if result.winner_position_id else None,
#                     })
#
#         # Return the data as a JSON response
#         return JsonResponse({'event_results': event_results})
#
#     return JsonResponse({'error': 'Invalid request method'}, status=400)

# def GetResultReport(request):
#     if request.method == 'GET':
#         festival_id = request.GET.get('festival_id')
#
#         # Assuming you have a FestivalMasterHeader model with 'id' as its primary key
#         # Replace 'FestivalMasterHeader' with the actual model name if different
#         festival = get_object_or_404(FestivalMasterHeader, id=festival_id)
#
#         # Fetch relevant data based on your models and relationships
#         event_results = []
#
#         # Example: Fetch event result data
#         event_results_data = EventResult.objects.filter(event_master_id__festival_master_header_id=festival.id, is_active=True)
#         event_results_data = event_results_data.order_by('participant_registration_header_id__event_chest_no')
#
#
#         for result in event_results_data:
#             event = result.event_master_id
#             participant_header = result.participant_registration_header_id
#             participants = ParticipantRegistrationChild.objects.filter(participant_registration_header_id=participant_header.id)
#
#             for participant in participants:
#                 # Fetch additional data as needed
#                 winner_position = result.winner_position_id
#
#                 # Example: Append relevant data to event_results
#                 event_results.append({
#                     'event_name': event.event_name if event else None,
#                     'participant_name': participant.participant_name if participant else None,
#                     'event_chest_no': participant_header.event_chest_no if participant_header else None,  # Replace with the actual field name
#                     'college_name': participant_header.college_name if participant_header else None,  # Replace with the actual field name
#                     'position': winner_position.winner_position if winner_position else None,  # Replace with the actual field name
#                 })
#
#         # Return the data as a JSON response
#         return JsonResponse({'event_results': event_results})
#
#     return JsonResponse({'error': 'Invalid request method'}, status=400)

# def GetResultReport(request):
#     if request.method == 'GET':
#         festival_id = request.GET.get('festival_id')
#
#         # Assuming you have a FestivalMasterHeader model with 'id' as its primary key
#         # Replace 'FestivalMasterHeader' with the actual model name if different
#         festival = get_object_or_404(FestivalMasterHeader, id=festival_id)
#
#         # Fetch relevant data based on your models and relationships
#         event_results = []
#
#         # Example: Fetch event result data
#         event_results_data = EventResult.objects.filter(event_master_id__festival_master_header_id=festival.id, is_active=True)
#
#         for result in event_results_data:
#             # Fetch additional data as needed
#             event = result.event_master_id
#             participant_header = result.participant_registration_header_id
#             participant = ParticipantRegistrationChild.objects.filter(participant_registration_header_id=participant_header.id).first()
#             winner_position = result.winner_position_id
#
#             # Example: Append relevant data to event_results
#             event_results.append({
#                 'event_name': event.event_name if event else None,
#                 'participant_name': participant.participant_name if participant else None,
#                 'event_chest_no': participant_header.event_chest_no if participant_header else None,  # Replace with the actual field name
#                 'college_name': participant_header.college_name if participant_header else None,  # Replace with the actual field name
#                 'position': winner_position.winner_position if winner_position else None,  # Replace with the actual field name
#             })
#
#         # Return the data as a JSON response
#         return JsonResponse({'event_results': event_results})
#
#     return JsonResponse({'error': 'Invalid request method'}, status=400)

# def GetResultReport(request):
#     if request.method == 'GET':
#         festival_id = request.GET.get('festival_id')
#
#         # Assuming you have a FestivalMasterHeader model with 'id' as its primary key
#         # Replace 'FestivalMasterHeader' with the actual model name if different
#         festival = get_object_or_404(FestivalMasterHeader, id=festival_id)
#
#         # Fetch relevant data based on your models and relationships
#         event_results = []
#
#         # Example: Fetch event result data
#         event_results_data = EventResult.objects.filter(event_master_id__festival_master_header_id=festival.id,is_active=1)
#
#         for result in event_results_data:
#             # Fetch additional data as needed
#             event = EventMaster.objects.get(id=result.event_master_id.id)
#             participant_header = ParticipantRegistrationHeader.objects.get(pk=festival_id)
#             participant = ParticipantRegistrationChild.objects.get(id=result.participant_registration_header_id.id)
#             winner_position = WinnerPositionMasterModel.objects.get(id=result.winner_position_id.id)
#
#             # Example: Append relevant data to event_results
#             event_results.append({
#                 'event_name': event.event_name,
#                 'participant_name': participant.participant_name,
#                 'event_chest_no': participant_header.event_chest_no,  # Replace with the actual field name
#                 'college_name': participant_header.college_name,  # Replace with the actual field name
#                 'position': winner_position.winner_position,  # Replace with the actual field name
#             })
#
#         # Return the data as a JSON response
#         return JsonResponse({'event_results': event_results})
#
#     return JsonResponse({'error': 'Invalid request method'}, status=400)

# def GetResultReport(request):
#     if request.method == 'GET':
#         festival_id = request.GET.get('festival_id')
#
#         event_results_data  = EventResult.objects.filter(event_master_id__festival_master_header_id=festival_id)
#         print("---------------------",event_results_data)
#
#         event_results = event_results_data.values(
#             'event_master_id__event_name',
#             'participant_registration_header_id__participantregistrationchild__participant_name',
#             'participant_registration_header_id__event_chest_no',
#             'participant_registration_header_id__college_name',
#             'winner_position_id__winner_position'
#         )
#         event_results_list = list(event_results)
#         print("---------------------------------------",event_results_list)
#         return JsonResponse({'event_results': event_results_list})

        # # Assuming you have a FestivalMasterHeader model with 'id' as its primary key
        # # Replace 'FestivalMasterHeader' with the actual model name if different
        # festival = get_object_or_404(FestivalMasterHeader, id=festival_id)
        #
        # # Fetch relevant data using select_related to optimize queries
        # event_results_data = EventResult.objects.select_related(
        #     'event_master_id',
        #     'participant_registration_header_id__participantregistrationchild',
        #     'winner_position_id'
        # ).filter(event_master_id__festival_master_header_id=festival.id)
        # print("------------------------------",event_results_data)
        # event_results = []
        #
        # for result in event_results_data:
        #     # Access attributes using the correct field names
        #     event_name = result.event_master_id.event_name
        #     participant_name = result.participant_registration_header_id.participantregistrationchild.participant_name
        #     event_chest_no = result.participant_registration_header_id.event_chest_no
        #     college_name = result.participant_registration_header_id.college_name
        #     position = result.winner_position_id.winner_position
        #
        #     # Append relevant data to event_results
        #     event_results.append({
        #         'event_name': event_name,
        #         'participant_name': participant_name,
        #         'event_chest_no': event_chest_no,
        #         'college_name': college_name,
        #         'position': position,
        #     })
        # print("-------------------------------------------",event_results)
        # # Return the data as a JSON response
        # return JsonResponse({'event_results': event_results})

    # return JsonResponse({'error': 'Invalid request method'}, status=400)

def referalreport(re):
    return render(re,'AdminMain/Report/ReferralReport.html')


def participantlist(request):
    Festivalname=FestivalMasterHeader.objects.all()
    return render(request,'AdminMain/Report/ParticipantList.html',{'festival':Festivalname})

class GetFestivalParticipant(View):
    def get(self,request,*args,**kwargs):

        print("------------------------------------getfestivalparticipant")
        festival_id = request.GET.get('festival_id')
        print("-----------------------festival id ",festival_id)
        Participants = ParticipantRegistrationChild.objects.filter(
        participant_registration_header_id__event_master_id__festival_master_header_id=festival_id,
        participant_registration_header_id__participantregistrationpayment__payment_status=1
        ).order_by('participant_registration_header_id__event_chest_no')

        response_data = []
        for participant in Participants:
            participant_info = {
                'participant_chest_no':participant.participant_registration_header_id.event_chest_no,
                'participant_name': participant.participant_name,
                'college_name': participant.participant_registration_header_id.college_name,
                'participant_phone': participant.participant_phone,
                'participant_email': participant.participant_email,
                'reference_by': participant.participant_registration_header_id.reference_by,
                'participant_id_card': participant.participant_id_no,
                'id':participant.id
                # Include other fields as needed
            }
            response_data.append(participant_info)

        events = EventMaster.objects.filter(festival_master_header_id=festival_id,is_active=1)

        event_data = []
        for event in events:
            max_registration = event.max_registration
            # Filter based on payment_status and include only successful payments (payment_status = 1)
            teams_registered = ParticipantRegistrationHeader.objects.filter(
                event_master_id=event.id,
                participantregistrationpayment__payment_status=1
            ).count()

            event_data.append({
                'event_name': event.event_name,
                'max_registration': max_registration,
                'teams_registered': teams_registered,
                'response_data': response_data
            })
        data = {
                'event_data': event_data,
                'response_data': response_data,
            }
        print("----------------------data",data)
        return JsonResponse(data)


class ParticipantListEdit(View):
    def get(self,request,*args,**kwargs):
        id = self.kwargs.get('id')

        Participants = ParticipantRegistrationChild.objects.filter(pk=id)
        response_data = []
        for participant in Participants:
            participant_info = {
                'participant_chest_no':participant.participant_registration_header_id.event_chest_no,
                'participant_name': participant.participant_name,
                'college_name': participant.participant_registration_header_id.college_name,
                'participant_phone': participant.participant_phone,
                'participant_email': participant.participant_email,
                'reference_by': participant.participant_registration_header_id.reference_by,
                'participant_id_card': participant.participant_id_no,
                'id':participant.id
                # Include other fields as needed
            }
            response_data.append(participant_info)
        return render(request,'AdminMain/Report/participant_list_edit.html',{'data':response_data})

    def post(self,request,*args,**kwargs):
        id = self.kwargs.get('id')
        Participants = ParticipantRegistrationChild.objects.get(pk=id)
        participant_header = Participants.participant_registration_header_id

        # participant_chest_no = request.POST['participant_chest_no']
        participant_name = request.POST['participant_name']
        college_name = request.POST['college_name']
        participant_phone = request.POST['participant_phone']
        participant_email = request.POST['participant_email']
        reference_by = request.POST['reference_by']
        participant_id_no = request.POST['participant_id_no']
        print("-----------------------------participant child :",participant_name,participant_phone,participant_email,participant_id_no,reference_by)
        participant_header.college_name = college_name
        participant_header.reference_by = reference_by
        participant_header.save()

        Participants.participant_name = participant_name
        Participants.participant_phone = participant_phone
        Participants.participant_email = participant_email
        Participants.participant_id_no = participant_id_no
        Participants.modified_on = datetime.now()
        # Save the changes to the database
        Participants.save()
        return HttpResponse("<script>alert('Participant details updated.');window.location='../ParticipantListReport';</script>")

def getcategorytype(request):
    print("-------------------------- getcategorytype function ")
    festival_id = request.GET.get('festival_id')
    print("-------------------------- getcategorytype function festival id ",festival_id)

    if festival_id:
        event_type = EventMaster.objects.filter(
            festival_master_header_id=festival_id,
            is_active=1
        ).values('participant_category_id','participant_category_id.participant_category_name')

        print("------------------------------",event_type)
        # Manually remove duplicates based on 'id'
        unique_categories = []
        seen_ids = set()

        for types in event_type:
            category_id = types['participant_category_id']
            if category_id not in seen_ids:
                unique_categories.append(types)
                seen_ids.add(category_id)
        print(unique_categories)
        return JsonResponse(unique_categories, safe=False)
    else:
        return JsonResponse([], safe=False)



class GetParticipantView(View):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def get(self,request):
        festival_id = request.GET.get('festival_id')
        Event_id = request.GET.get('eventId')
        Participants = ParticipantRegistrationChild.objects.filter(
        participant_registration_header_id__event_master_id__festival_master_header_id=festival_id,
        participant_registration_header_id__event_master_id=Event_id,
        participant_registration_header_id__participantregistrationpayment__payment_status=1
        ).order_by('participant_registration_header_id__event_chest_no')

        response_data = []
        for participant in Participants:
            participant_info = {
                'participant_chest_no':participant.participant_registration_header_id.event_chest_no,
                'participant_name': participant.participant_name,
                'college_name': participant.participant_registration_header_id.college_name,
                'participant_phone': participant.participant_phone,
                'participant_email': participant.participant_email,
                'reference_by': participant.participant_registration_header_id.reference_by,
                'participant_id_card': participant.participant_id_no,
                'id':participant.id
                # Include other fields as needed
            }
            response_data.append(participant_info)

        return JsonResponse({'Participants':response_data})


def referal_report(re):
    festival_master = FestivalMasterHeader.objects.filter(is_active=1)
    return render(re,'AdminMain/Report/ReferralReport.html',{'festival':festival_master})

class GetReferrealReport(View):
    def get(self, request, *args, **kwargs):
        festival_id = request.GET.get('festival_id')

        if festival_id:
            event_names = EventMaster.objects.filter(
                festival_master_header_id=festival_id, is_active=1
            ).values('id', 'event_name')
            unique_events = []

            seen_ids = set()
            for event in event_names:
                event_id = event['id']
                if event_id not in seen_ids:
                    unique_events.append(event)
                    seen_ids.add(event_id)

        if festival_id:
            try:
                festival_instance = FestivalMasterHeader.objects.get(pk=festival_id)
                events = EventMaster.objects.filter(festival_master_header_id=festival_instance.id,is_active=1)

                event_data = []
                unique_colleges = set()  # Set to store unique college names

                for event in events:
                    # Filter based on payment_status and include only successful payments (payment_status = 1)
                    reffers = ParticipantRegistrationHeader.objects.filter(
                        event_master_id=event.id,
                        participantregistrationpayment__payment_status=1,
                        reference_by__isnull=False,
                        reference_by__gt=''
                    ).distinct()

                    for refer in reffers:
                        college_name = refer.college_name
                        unique_colleges.add(college_name)  # Add college name to the set
                        event_data.append({
                            'referral_name': refer.reference_by,
                            'college_name': college_name,
                            'chest_no': refer.event_chest_no,
                        })

                college_count = len(unique_colleges)
                print("---------------------------------------------------college_count",college_count)
                return JsonResponse({'event_data': event_data, 'selected_festival': festival_instance.festival_name, 'college_count': college_count,'unique_events':unique_events})

            except FestivalMasterHeader.DoesNotExist:
                # Handle the case where the selected festival does not exist
                return JsonResponse({'error': 'Selected festival not found'}, status=400)

        return JsonResponse({'error': 'No festival selected'}, status=400)

class GetRefferalReportEventwise(View):
    def get(self, request, *args, **kwargs):
        festival_id = request.GET.get('festival_id')
        event_id=request.GET.get('eventId')
        if festival_id:
            try:
                festival_instance = FestivalMasterHeader.objects.get(pk=festival_id)
                events = EventMaster.objects.filter(pk=event_id)

                event_data = []
                unique_colleges = set()  # Set to store unique college names

                for event in events:
                    # Filter based on payment_status and include only successful payments (payment_status = 1)
                    reffers = ParticipantRegistrationHeader.objects.filter(
                        event_master_id=event.id,
                        participantregistrationpayment__payment_status=1,
                        reference_by__isnull=False,
                        reference_by__gt=''
                    ).distinct()

                    for refer in reffers:
                        college_name = refer.college_name
                        unique_colleges.add(college_name)  # Add college name to the set
                        event_data.append({
                            'referral_name': refer.reference_by,
                            'college_name': college_name,
                            'chest_no': refer.event_chest_no,
                        })

                college_count = len(unique_colleges)
                print("---------------------------------------------------college_count",college_count)
                return JsonResponse({'event_data': event_data, 'selected_festival': festival_instance.festival_name, 'college_count': college_count})

            except FestivalMasterHeader.DoesNotExist:
                # Handle the case where the selected festival does not exist
                return JsonResponse({'error': 'Selected festival not found'}, status=400)

        return JsonResponse({'error': 'No festival selected'}, status=400)


# class GetReferrealReport(View):
#     def get(self, request, *args, **kwargs):
#         festival_id = request.GET.get('festival_id')
#
#         if festival_id:
#             try:
#                 festival_instance = FestivalMasterHeader.objects.get(pk=festival_id)
#                 events = EventMaster.objects.filter(festival_master_header_id=festival_instance.id)
#
#                 event_data = []
#                 for event in events:
#                     # Filter based on payment_status and include only successful payments (payment_status = 1)
#                     reffers = ParticipantRegistrationHeader.objects.filter(
#                         event_master_id=event.id,
#                         participantregistrationpayment__payment_status=1,
#                         reference_by__isnull=False,  # Include only non-null reference_by values
#                         reference_by__gt=''          # Include only non-empty reference_by values
#                     ).distinct()
#
#
#                     for refer in reffers:
#                         event_data.append({
#                             'referral_name': refer.reference_by,
#                             'college_name': refer.college_name,
#                             'chest_no': refer.event_chest_no,
#                         })
#
#                 return JsonResponse({'event_data': event_data, 'selected_festival': festival_instance.festival_name})
#
#             except FestivalMasterHeader.DoesNotExist:
#                 # Handle the case where the selected festival does not exist
#                 return JsonResponse({'error': 'Selected festival not found'}, status=400)
#
#         return JsonResponse({'error': 'No festival selected'}, status=400)


#----------------------------------------------------------------------------------------------
def college_report(request):
    festival_master = FestivalMasterHeader.objects.filter(is_active=1)
    return render(request,'AdminMain/Report/collegereport.html',{'festival':festival_master})

# class GetCollegeReport(View):
#     def get(self, request, *args, **kwargs):
#         festival_id = request.GET.get('festival_id')
#
#         if festival_id:
#             try:
#                 festival_instance = FestivalMasterHeader.objects.get(pk=festival_id)
#                 events = EventMaster.objects.filter(festival_master_header_id=festival_instance.id)
#
#                 event_data = []
#                 for event in events:
#                     # Filter based on payment_status and include only successful payments (payment_status = 1)
#                     colleges = ParticipantRegistrationHeader.objects.filter(
#                         event_master_id=event.id,
#                         participantregistrationpayment__payment_status=1  # Adding the payment_status condition
#                     ).values('college_name', 'event_master_id__event_name').distinct()
#
#                     for college in colleges:
#                         event_data.append({
#                             'college_name': college['college_name'],
#                             'events': college['event_master_id__event_name'],
#                         })
#
#                 return JsonResponse({'event_data': event_data})
#
#             except FestivalMasterHeader.DoesNotExist:
#                 # Handle the case where the selected festival does not exist
#                 return JsonResponse({'error': 'Selected festival not found'}, status=400)
#
#         return JsonResponse({'error': 'No festival selected'}, status=400)

class GetCollegeReport(View):
    def get(self, request, *args, **kwargs):
        festival_id = request.GET.get('festival_id')

        if festival_id:
            try:
                festival_instance = FestivalMasterHeader.objects.get(pk=festival_id)
                events = EventMaster.objects.filter(festival_master_header_id=festival_instance.id)

                event_data = []

                # Collect all colleges and events
                for event in events:
                    colleges = ParticipantRegistrationHeader.objects.filter(
                        event_master_id=event.id,
                        participantregistrationpayment__payment_status=1
                    ).values('college_name', 'event_master_id__event_name').distinct()

                    for college in colleges:
                        event_data.append({
                            'college_name': college['college_name'],
                            'events': college['event_master_id__event_name'],
                        })

                # Pagination
                paginator = Paginator(event_data, 10)  # 10 items per page
                page_number = request.GET.get('page')
                page_obj = paginator.get_page(page_number)
                print("-----------------------------------total page",paginator.num_pages)
                print("-----------------------------------curren page",page_obj.number)
                return JsonResponse({
                    'event_data': list(page_obj),
                    'total_pages': paginator.num_pages,
                    'current_page': page_obj.number,
                })

            except FestivalMasterHeader.DoesNotExist:
                return JsonResponse({'error': 'Selected festival not found'}, status=400)

        return JsonResponse({'error': 'No festival selected'}, status=400)


class GetCollegeReport1(View):
    def get(self, request, *args, **kwargs):
        festival_id = request.GET.get('festival_id')
        page_number = request.GET.get('page')
        print('------------------------------page number',page_number)

        if festival_id:
            try:
                festival_instance = FestivalMasterHeader.objects.get(pk=festival_id)
                events = EventMaster.objects.filter(festival_master_header_id=festival_instance.id)

                event_data = []

                # Collect all colleges and events
                for event in events:
                    colleges = ParticipantRegistrationHeader.objects.filter(
                        event_master_id=event.id,
                        participantregistrationpayment__payment_status=1
                    ).values('college_name', 'event_master_id__event_name').distinct()

                    for college in colleges:
                        event_data.append({
                            'college_name': college['college_name'],
                            'events': college['event_master_id__event_name'],
                        })

                # Pagination
                paginator = Paginator(event_data, 10)  # 10 items per page
                page_obj = paginator.get_page(page_number)

                return JsonResponse({
                    'event_data': list(page_obj),
                    'total_pages': paginator.num_pages,
                    'current_page': page_obj.number,
                })

            except FestivalMasterHeader.DoesNotExist:
                return JsonResponse({'error': 'Selected festival not found'}, status=400)

        return JsonResponse({'error': 'No festival selected'}, status=400)

class GetCollegeReport2(View):
    def get(self, request, *args, **kwargs):
        festival_id = request.GET.get('festival_id')
        page_number = request.GET.get('page')
        print('------------------------------page number', page_number)

        if festival_id:
            try:
                festival_instance = FestivalMasterHeader.objects.get(pk=festival_id)
                events = EventMaster.objects.filter(festival_master_header_id=festival_instance.id)

                event_data = []

                # Collect all colleges and events
                for event in events:
                    colleges = ParticipantRegistrationHeader.objects.filter(
                        event_master_id=event.id,
                        participantregistrationpayment__payment_status=1
                    ).values('college_name', 'event_master_id__event_name').distinct()

                    for college in colleges:
                        event_data.append({
                            'college_name': college['college_name'],
                            'events': college['event_master_id__event_name'],
                        })

                # Pagination
                paginator = Paginator(event_data, 10)  # 10 items per page

                if page_number:
                    page_number = int(page_number)
                    if page_number > 1:
                        page_number -= 1  # Adjust for previous page

                page_obj = paginator.get_page(page_number)

                return JsonResponse({
                    'event_data': list(page_obj),
                    'total_pages': paginator.num_pages,
                    'current_page': page_obj.number,
                })

            except FestivalMasterHeader.DoesNotExist:
                return JsonResponse({'error': 'Selected festival not found'}, status=400)

        return JsonResponse({'error': 'No festival selected'}, status=400)

# class GetCollegeReport(View):
#     def get(self, request, *args, **kwargs):
#         festival_id = request.GET.get('festival_id')
#
#         if festival_id:
#             try:
#                 festival_instance = FestivalMasterHeader.objects.get(pk=festival_id)
#                 events = EventMaster.objects.filter(festival_master_header_id=festival_instance.id)
#
#                 event_data = []
#                 for event in events:
#                     # Filter based on payment_status and include only successful payments (payment_status = 1)
#                     colleges = ParticipantRegistrationHeader.objects.filter(
#                         event_master_id=event.id
#                     ).values('college_name', 'event_master_id__event_name').distinct()
#
#                     for college in colleges:
#                         event_data.append({
#                             'college_name':  college['college_name'],
#                             'events': college['event_master_id__event_name'],
#                         })
#
#                 return JsonResponse({'event_data': event_data})
#
#             except FestivalMasterHeader.DoesNotExist:
#                 # Handle the case where the selected festival does not exist
#                 return JsonResponse({'error': 'Selected festival not found'}, status=400)
#
#         return JsonResponse({'error': 'No festival selected'}, status=400)


def overall_point_wise_report(request):
    festival_master = FestivalMasterHeader.objects.filter(is_active=1)
    return render(request,'AdminMain/Report/OverallPointwiseReport.html',{'festival':festival_master})

def participant_statistics_report(request):
    festival_master = FestivalMasterHeader.objects.filter(is_active=1)
    return render(request,'AdminMain/Report/RegistrationStatisticsReport.html',{'festival':festival_master})

class GetEventMasterReport(View):
    def get(self, request, *args, **kwargs):
        festival_id = request.GET.get('festival_id')

        if festival_id:
            try:
                festival_instance = FestivalMasterHeader.objects.get(pk=festival_id)
                events = EventMaster.objects.filter(festival_master_header_id=festival_instance.id,is_active=1)

                event_data = []
                for event in events:
                    max_registration = event.max_registration
                    # Filter based on payment_status and include only successful payments (payment_status = 1)
                    teams_registered = ParticipantRegistrationHeader.objects.filter(
                        event_master_id=event.id,
                        participantregistrationpayment__payment_status=1
                    ).count()

                    event_data.append({
                        'event_name': event.event_name,
                        'max_registration': max_registration,
                        'teams_registered': teams_registered,
                    })

                return JsonResponse({'event_data': event_data})

            except FestivalMasterHeader.DoesNotExist:
                # Handle the case where the selected festival does not exist
                return JsonResponse({'error': 'Selected festival not found'}, status=400)

        return JsonResponse({'error': 'No festival selected'}, status=400)

def spot_registration_report(request):
    festival_master = FestivalMasterHeader.objects.filter(is_active=1)
    return render(request,'AdminMain/Report/SpotRegistrationReport1.html',{'festival':festival_master})

class GetEventNames(View):
    def get(self, request, *args, **kwargs):
        festival_id = request.GET.get('festival_id')
        if festival_id:
            event_names = EventMaster.objects.filter(
                festival_master_header_id=festival_id, is_active=1
            ).values('id', 'event_name')
            unique_events = []

            seen_ids = set()
            for event in event_names:
                event_id = event['id']
                if event_id not in seen_ids:
                    unique_events.append(event)
                    seen_ids.add(event_id)

            participant_headers = ParticipantRegistrationHeader.objects.filter(
                event_master_id__festival_master_header_id=festival_id,
            ).order_by('event_chest_no')

            response_data = []
            for header in participant_headers:
                leader_name = ParticipantRegistrationChild.objects.filter(
                    participant_registration_header_id=header.id
                ).first()

                payment = ParticipantRegistrationPayment.objects.filter(
                    participant_registration_header_id=header.id,
                    registration="spot",
                ).first()

                if payment:
                    reg_info = {
                        'Event_name': header.event_master_id.event_name,
                        'Team_Leader': leader_name.participant_name if leader_name else None,
                        'Chest_no': header.event_chest_no,
                        'Amount': payment.registration_fee if payment else None,
                    }
                    response_data.append(reg_info)

            data = {
                'unique_events': unique_events,
                'response_data': response_data,
            }
            return JsonResponse(data)
        else:
            return JsonResponse({}, status=400)

# class GetEventNames(View):
#     def get(self, request, *args, **kwargs):
#         festival_id = request.GET.get('festival_id')
#         if festival_id:
#             event_names = EventMaster.objects.filter(
#             festival_master_header_id=festival_id, is_active=1
#             ).values('id', 'event_name')
#             unique_events = []
#             seen_ids = set()
#             for event in event_names:
#                 event_id = event['id']
#                 if event_id not in seen_ids:
#                     unique_events.append(event)
#                     seen_ids.add(event_id)
#             return JsonResponse(unique_events, safe=False)
#         else:
#             return JsonResponse([], safe=False)

class SpotRegistrationReportView(View):
    print("------------------------------------SpotRegistrationReportView")
    def get(self, request, *args, **kwargs):
        festival_id = request.GET.get('festival_id')
        event_id = request.GET.get('eventId')
        print("------------------------------------get")

        # Retrieve all participant headers for the specified festival and event
        participant_headers = ParticipantRegistrationHeader.objects.filter(
            event_master_id__festival_master_header_id=festival_id,
            event_master_id=event_id
        ).order_by('event_chest_no')
        print("------------------------------------participant_headers",participant_headers)

        response_data = []
        for header in participant_headers:
            # Retrieve the leader name for the current header
            leader_name = ParticipantRegistrationChild.objects.filter(
                participant_registration_header_id=header.id
            ).first()

            # Retrieve the payment details for the current header
            payment = ParticipantRegistrationPayment.objects.filter(
                participant_registration_header_id=header.id,
                registration="spot",
            ).first()
            print("---------------------------------------payment",payment)
            # Construct the response data
            if payment:
                reg_info = {
                    'Event_name': header.event_master_id.event_name,
                    'Team_Leader': leader_name.participant_name if leader_name else None,
                    'Chest_no': header.event_chest_no,
                    'Amount': payment.registration_fee if payment else None,
                    # Include other fields as needed
                }
                response_data.append(reg_info)
        print("------------------------------------participant_headers",response_data)

        return JsonResponse({'spotregistration': response_data})

def account_report(request):
    festival_master = FestivalMasterHeader.objects.filter(is_active=1)
    return render(request,'AdminMain/Report/AccountReport.html',{'festival':festival_master})


# class GetAccountReportYear(View):
#     print("---------------------------- class GetAccountReport")
#     def get(self, request, *args, **kwargs):
#         target_year = request.GET.get('festival_year')
#
#         target_year = int(target_year) if target_year else None
#         print("---------------------------- get",target_year)
#
#
#         # Retrieve the data where ParticipantRegistrationPayment.payment_status = 1 and created in the target year
#         queryset = ParticipantRegistrationPayment.objects.filter(
#             payment_status=1,
#             created_on__year=target_year
#         )
#         print("--------------------------------queryset",queryset)
#         # Fetch the related information
#         data = queryset.values(
#             'participant_registration_header_id__event_chest_no',
#             'participant_registration_header_id__event_master_id__event_name',
#             'participant_registration_header_id__participant_registration_child__participant_name',
#             'transaction_id',
#             'created_on',
#             'registration_fee'
#         )
#         print("------------------------------------data",data)
#
#         # Convert the queryset data to a list of dictionaries
#         participant_data = list(data)
#
#         print("-----------------------------------------participant_data",participant_data)
#         # Return the JSON response
#         return JsonResponse({'participant_data': participant_data})


class GetAccountReportYear(View):
    print("---------------------------- class GetAccountReport")
    def get(self, request, *args, **kwargs):
        target_year = request.GET.get('festival_year')
        print("----------------------year",target_year)

        target_year = int(target_year) if target_year else None
        print("---------------------------- get",target_year)

        festivalname = FestivalMasterHeader.objects.filter(created_on__year=target_year
                                                          ).values('id','festival_name')
        if target_year:
            festival_names = FestivalMasterHeader.objects.filter(from_date__year=target_year,is_active=1,
                                                          ).values('id','festival_name')
            unique_festivals = []

            seen_ids = set()
            for festival in festival_names:
                festival_id = festival['id']
                if festival_id not in seen_ids:
                    unique_festivals.append(festival)
                    seen_ids.add(festival_id)


        # Retrieve the data where ParticipantRegistrationPayment.payment_status = 1 and created in the target year
        queryset = ParticipantRegistrationHeader.objects.filter(
            created_on__year=target_year,
            participantregistrationpayment__payment_status=1,
            participantregistrationchild__participant_type_id__participant_type= "Team Leader"
        )
        print("--------------------------------queryset",queryset)
        # Fetch the related information
        data = queryset.annotate(
            truncated_created_on=TruncDate('created_on')
        ).values(
            'event_chest_no',
            'college_name',
            'event_master_id__event_name',
            'truncated_created_on',
            'participantregistrationchild__participant_name',
            'participantregistrationpayment__transaction_id',
            'participantregistrationpayment__registration_fee',
        )
        print("------------------------------------data",data)

        # Convert the queryset data to a list of dictionaries
        participant_data = list(data)

        print("-----------------------------------------participant_data",participant_data)
        # Return the JSON response
        return JsonResponse({'participant_data': participant_data,'unique_festivals':unique_festivals})

class GetAccountReportFestivalWise(View):
    print("---------------------------- class GetAccountReportFestivalWise")
    def get(self, request, *args, **kwargs):
        Festival_Id=request.GET.get('festival_id')

        if Festival_Id:
            event_names = EventMaster.objects.filter(
                festival_master_header_id=Festival_Id, is_active=1
            ).values('id', 'event_name')
            unique_events = []

            seen_ids = set()
            for event in event_names:
                event_id = event['id']
                if event_id not in seen_ids:
                    unique_events.append(event)
                    seen_ids.add(event_id)

        queryset = ParticipantRegistrationHeader.objects.filter(
            event_master_id__festival_master_header_id=Festival_Id,
            participantregistrationpayment__payment_status=1,
            participantregistrationchild__participant_type_id__participant_type= "Team Leader"
        )

        data = queryset.annotate(
            truncated_created_on=TruncDate('created_on')
        ).values(
            'event_chest_no',
            'college_name',
            'event_master_id__event_name',
            'truncated_created_on',
            'participantregistrationchild__participant_name',
            'participantregistrationpayment__transaction_id',
            'participantregistrationpayment__registration_fee',
        )

        # Convert the queryset data to a list of dictionaries
        participant_data = list(data)

        return JsonResponse({'participant_data': participant_data,'unique_events':unique_events})


class GetAccountReportEventWise(View):
    print("---------------------------- class GetAccountReportFestivalWise")
    def get(self, request, *args, **kwargs):
        Festival_Id=request.GET.get('festival_id')
        event_id=request.GET.get('eventId')

        print('...........................eventid',event_id)

        queryset = ParticipantRegistrationHeader.objects.filter(
            event_master_id=event_id,
            event_master_id__festival_master_header_id=Festival_Id,
            participantregistrationpayment__payment_status=1,
            participantregistrationchild__participant_type_id__participant_type= "Team Leader"
        )

        data = queryset.annotate(
            truncated_created_on=TruncDate('created_on')
        ).values(
            'event_chest_no',
            'college_name',
            'event_master_id__event_name',
            'truncated_created_on',
            'participantregistrationchild__participant_name',
            'participantregistrationpayment__transaction_id',
            'participantregistrationpayment__registration_fee',
        )

        # Convert the queryset data to a list of dictionaries
        participant_data = list(data)

        return JsonResponse({'participant_data': participant_data})


class GetResultReportFestival(View):
    def get(self,request,*args,**kwargs):
        festival_id = request.GET.get('festival_id')

        # Assuming you have a FestivalMasterHeader model with 'id' as its primary key
        # Replace 'FestivalMasterHeader' with the actual model name if different
        festival = get_object_or_404(FestivalMasterHeader, id=festival_id)

        # Fetch relevant data based on your models and relationships
        event_results = []

        # Example: Fetch event result data
        event_results_data = EventResult.objects.filter(event_master_id__festival_master_header_id=festival.id, is_active=True)

        for result in event_results_data:
            # Fetch additional data as needed
            event = result.event_master_id
            participant_header = result.participant_registration_header_id
            participant = ParticipantRegistrationChild.objects.filter(participant_registration_header_id=participant_header.id).first()

            # Example: Append relevant data to event_results
            event_results.append({
                'event_name': event.event_name if event else None,
                'participant_name': participant.participant_name if participant else None,
                'event_chest_no': participant_header.event_chest_no if participant_header else None,  # Replace with the actual field name
                'college_name': participant_header.college_name if participant_header else None,  # Replace with the actual field name
                # 'transaction_id':
            })

        # Return the data as a JSON response
        return JsonResponse({'event_results': event_results})

class GetResultEventWise(View):
    def get(self,request,*args,**kwargs):
        festival_id = request.GET.get('festival_id')
        event_id=request.GET.get('eventId')

        festival = get_object_or_404(FestivalMasterHeader, id=festival_id)

        # Fetch relevant data based on your models and relationships
        event_results_data = EventResult.objects.filter(
            event_master_id__festival_master_header_id=festival.id,
            is_active=True,
            event_master_id=event_id,
            winner_position_id__is_active=True,).order_by('event_master_id', 'winner_position_id__winner_position')


        grouped_results = {key: list(group) for key, group in groupby(event_results_data, key=lambda x: x.event_master_id)}

        # Iterate through the groups and append to event_results
        event_results = []
        for event_id, results in grouped_results.items():
            for position, result in enumerate(results, start=1):
                event = result.event_master_id
                participant_header = result.participant_registration_header_id
                participants = ParticipantRegistrationChild.objects.filter(participant_registration_header_id=participant_header.id)

                for participant in participants:
                    # Fetch additional data as needed
                    winner_position = result.winner_position_id
                    participant_type = participant.participant_type_id

                    # Append relevant data to event_results
                    event_results.append({
                        'event_name': event.event_name if event else None,
                        'participant_name': participant.participant_name if participant else None,
                        'event_chest_no': participant_header.event_chest_no if participant_header else None,
                        'college_name': participant_header.college_name if participant_header else None,
                        'position': winner_position.winner_position if winner_position else None,
                        'participant_type': participant_type.participant_type if participant_type else None,
                    })
            return JsonResponse({'event_results':event_results})
        return JsonResponse({'error': 'Invalid request method'}, status=400)


# correct
# def get_overall_pointwise_report(request):
#     festival_id = request.GET.get('festival_id')
#     print("---------------------------------------get_overall_pointwise_report")
#     if festival_id:
#         try:
#             # Fetch event results with related data
#             event_results = EventResult.objects.select_related(
#                 'event_master_id', 'winner_position_id', 'participant_registration_header_id'
#             ).filter(is_active=1, event_master_id__festival_master_header_id=festival_id)
#
#             table_data = []
#             unique_colleges = set()  # Set to store unique college names
#
#             for index, result in enumerate(event_results, start=1):
#                 winner_position = result.winner_position_id.winner_position if result.winner_position_id else None
#
#                 # Fetch related EventPrizeMaster for additional details
#                 event_prize = EventPrizeMaster.objects.filter(
#                     event_master_id=result.event_master_id,
#                     winner_position_id=result.winner_position_id
#                 ).first()
#
#                 prize_type = event_prize.prize_type_id.prize_type if event_prize and event_prize.prize_type_id else None
#                 cash_amount = event_prize.event_cash_prize if event_prize else None
#
#                 # Check if ParticipantRegistrationHeader has related ParticipantRegistrationChild
#                 participant_registration_header = result.participant_registration_header_id
#                 participant_name = None
#
#                 # Get the related ParticipantRegistrationChild data based on the header ID
#                 participant_registration_child = ParticipantRegistrationChild.objects.filter(
#                     participant_registration_header_id=participant_registration_header.id
#                 ).first()
#
#                 if participant_registration_child:
#                     participant_name = participant_registration_child.participant_name
#
#                     # Add college_name to the set if not already present
#                     if participant_name not in unique_colleges:
#                         unique_colleges.add(participant_name)
#
#                         table_data.append({
#                             'SlNo': index,
#                             'CollegeName': participant_registration_header.college_name if participant_registration_header else None,
#                             'EventName': result.event_master_id.event_name if result.event_master_id else None,
#                             'Position': winner_position,
#                             'Points': event_prize.event_scores if event_prize else None,
#                         })
#             print("-------------------------------------table_data-",table_data)
#             return JsonResponse({'result_data': table_data})
#
#         except EventResult.DoesNotExist:
#             return JsonResponse({'error': 'No event results found for the selected festival'}, status=400)
#
#     return JsonResponse({'error': 'No festival selected'}, status=400)


def get_overall_pointwise_report(request):

    festival_id = request.GET.get('festival_id')
    event_results = EventResult.objects.select_related(
        'event_master_id', 'winner_position_id', 'participant_registration_header_id'
    ).filter(is_active=1,event_master_id__festival_master_header_id = festival_id)

    table_data = []

    for index, result in enumerate(event_results, start=1):
        winner_position = result.winner_position_id.winner_position if result.winner_position_id else None

        # Fetch related EventPrizeMaster for additional details
        event_prize = EventPrizeMaster.objects.filter(
            event_master_id=result.event_master_id,
            winner_position_id=result.winner_position_id
        ).first()

        prize_type = event_prize.prize_type_id.prize_type if event_prize and event_prize.prize_type_id else None
        cash_amount = event_prize.event_cash_prize if event_prize else None

        # Check if ParticipantRegistrationHeader has related ParticipantRegistrationChild
        participant_registration_header = result.participant_registration_header_id
        participant_name = None

        # Get the related ParticipantRegistrationChild data based on the header ID
        participant_registration_child = ParticipantRegistrationChild.objects.filter(
            participant_registration_header_id=participant_registration_header.id
        ).first()

        if participant_registration_child:
            participant_name = participant_registration_child.participant_name

        table_data.append({
            'SlNo': index,
            'Festival': result.event_master_id.festival_master_header_id.festival_name if result.event_master_id else None,
            'EventName': result.event_master_id.event_name if result.event_master_id else None,
            'EventCategory': result.event_master_id.event_category_id.event_category_name if result.event_master_id and result.event_master_id.event_category_id else None,
            'WinnerPosition': winner_position,
            'PrizeType': prize_type,
            'EventScore': event_prize.event_scores if event_prize else None,
            'CollegeName': participant_registration_header.college_name if participant_registration_header else None,
            'ChestNumber': participant_registration_header.event_chest_no if participant_registration_header else None,
            'CashAmount': cash_amount,
            'ParticipantName': participant_name,
            'ID': result.id,
        })

    score = {}

    for i in table_data:
        college_name = i['CollegeName']
        score_event = i['EventScore']

        if college_name not in score:
            score[college_name] = 0

        total_score = score[college_name] + (score_event or 0)  # Use 0 if score_event is None
        score[college_name] = total_score

    result_data = []
    sl_no = 0
    for college, total_points in score.items():
        sl_no += 1
        result_data.append({
            'SlNo': sl_no,
            'CollegeName': college,
            'TotalPoints': int(total_points),
        })
    sorted_result_data = sorted(result_data, key=lambda x: x['TotalPoints'], reverse=True)

    return JsonResponse({'result_data': sorted_result_data})

# def ViewMenuHeader(request):
#     return render(request,'AdminMain/Menu/view_menu_header.html')

# ---------------------------------------------------Menu-------------------------------------------------------

class ViewMenuHeader(View):
    def get(self,request,*args,**kwargs):
        menu_header = MenuHeader.objects.filter(is_active=1)
        return render(request,'AdminMain/Menu/view_menu_header.html',{'data':menu_header})

    def post(self,request,*args,**kwargs):
        name = request.POST['name'].strip()
        menu_header = MenuHeader(
            name=name,
            is_active =1,
            created_on =datetime.now()
        )
        menu_header.save()
        return HttpResponse("<script>alert('Successfully created menu');window.location='../ViewMenuHeader';</script>")

class EditMenuHeader(View):
    def get(self,request,*args,**kwargs):
        id = self.kwargs.get('id')
        menu_header = MenuHeader.objects.get(pk=id)
        return render(request,'AdminMain/Menu/edit_menu_header.html',{'data':menu_header})

    def post(self,request,*args,**kwargs):
        id = self.kwargs.get('id')
        name=request.POST['name'].strip()
        menu_header = MenuHeader.objects.get(pk=id)
        menu_header.name = name
        menu_header.modified_on = datetime.now()
        menu_header.save()
        return HttpResponse("<script>alert('Menu updated successfully');window.location='../ViewMenuHeader';</script>")


def delete_menu_header(request,id):
    return render(request,'AdminMain/Menu/delete_menu_header.html',{'data':id})

def delete_menu_header1(request,id):
    menu_header = MenuHeader.objects.get(pk=id)
    menu_header.is_active = 0
    menu_header.save()
    return redirect("ViewMenuHeader")

class CreateMenuChild(View):
    def get(self,request,*args,**kwargs):
        id = self.kwargs.get('id')
        menu_header = MenuHeader.objects.get(pk=id)
        return render(request,'AdminMain/Menu/create_menu_child.html',{'menu_header':menu_header.name})

    def post(self,request,*args,**kwargs):
        id = self.kwargs.get('id')
        name = request.POST['name'].strip()
        url = request.POST['url'].strip()
        menu_header = MenuHeader.objects.get(pk=id)
        menu_child = MenuChild(
            menu_header_id = menu_header,
            name=name,
            url=url,
            is_active =1,
            created_on =datetime.now()
        )
        menu_child.save()
        return HttpResponse("<script>alert('sub menu created successfully');window.location='../ViewMenuHeader';</script>")


def view_menu_child(request,id):
    menu_header = MenuHeader.objects.get(pk=id)
    menu_child = MenuChild.objects.filter(menu_header_id=menu_header,is_active=1)
    return render(request,'AdminMain/Menu/view_menu_child.html',{'data':menu_child})

class EditMenuChild(View):
    def get(self,request,*args,**kwargs):
        id = self.kwargs.get('id')
        menu_child = MenuChild.objects.get(pk=id)
        return render(request,'AdminMain/Menu/edit_menu_child.html',{'data':menu_child})

    def post(self,request,*args,**kwargs):
        id = self.kwargs.get('id')
        name = request.POST['name'].strip()
        url = request.POST['url'].strip()
        menu_child = MenuChild.objects.get(pk=id)
        menu_child.name = name
        menu_child.url = url
        menu_child.modified_on = datetime.now()
        menu_child.save()
        return HttpResponse("<script>alert('sub menu updated successfully');window.location='../ViewMenuHeader';</script>")

def delete_menu_child(request,id):
    return render(request,'AdminMain/Menu/delete_menu_child.html',{'data':id})

def delete_menu_child1(request,id):
    menu_child = MenuChild.objects.get(pk=id)
    menu_child.is_active = 0
    print("------------------------menu header",menu_child.is_active)
    menu_child.save()
    return redirect("ViewMenuHeader")
