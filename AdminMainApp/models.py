from django.db import models
# Create your models here.

class InstitutionMaster(models.Model):
    institution_name = models.CharField(max_length=100)
    institution_address = models.CharField(max_length=250)
    institution_phone_no = models.CharField(max_length=15, null=True, blank=True)
    institution_icon = models.CharField(max_length=50, null=True, blank=True)
    institution_banner = models.CharField(max_length=50, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.institution_name

class DepartmentMaster(models.Model):
    department_name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=20, null=True)
    modified_on = models.DateTimeField(null=True)
    modified_by = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.department_name

class EventCategoryMaster(models.Model):
    event_category_name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=20, null=True)
    modified_on = models.DateTimeField(null=True)
    modified_by = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.event_category_name

class ParticipantCategoryMaster(models.Model):
    participant_category_name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=20, null=True)
    modified_on = models.DateTimeField(null=True)
    modified_by = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.participant_category_name

class FestivalMasterHeader(models.Model):
    festival_name = models.CharField(max_length=100)
    # institution_id = models.ForeignKey(InstitutionMaster, on_delete=models.CASCADE, null=True)
    festival_icon = models.CharField(max_length=50, null=True, blank=True)
    festival_banner = models.CharField(max_length=50, null=True, blank=True)
    video_file = models.FileField(upload_to='media/', null=True)
    from_date = models.DateField()
    to_date = models.DateField()
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=20, null=True)
    modified_on = models.DateTimeField(null=True)
    modified_by = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.festival_name

class FestivalMasterChild(models.Model):
    festival_master_header_id = models.ForeignKey(FestivalMasterHeader, on_delete=models.CASCADE)
    registration_start_date = models.DateField(null=True, blank=True)
    registration_end_date = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=20, null=True)
    modified_on = models.DateTimeField(null=True)
    modified_by = models.CharField(max_length=20, null=True)

    def __str__(self):
        return f"FestivalChild - {self.id}"

class CommitteMemberTypeMaster(models.Model):
    committe_member_type = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=20, null=True)
    modified_on = models.DateTimeField(null=True)
    modified_by = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.committe_member_type

class OrganizingCommitteMaster(models.Model):
    festival_master_header_id = models.ForeignKey(FestivalMasterHeader, on_delete=models.CASCADE)
    department_master_id = models.ForeignKey(DepartmentMaster, on_delete=models.CASCADE)
    committe_member_type_id = models.ForeignKey(CommitteMemberTypeMaster, on_delete=models.SET_NULL, null=True, blank=True)
    committe_member_name = models.CharField(max_length=70)
    committe_member_phone = models.CharField(max_length=15, null=True, blank=True)
    committe_member_photo = models.CharField(max_length=50, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=20, null=True)
    modified_on = models.DateTimeField(null=True)
    modified_by = models.CharField(max_length=20, null=True)

    def __str__(self):
        return f"OrganizingCommittee - {self.id}"


class EventMaster(models.Model):
    festival_master_header_id = models.ForeignKey(FestivalMasterHeader, on_delete=models.CASCADE)
    event_category_id = models.ForeignKey(EventCategoryMaster, on_delete=models.CASCADE)
    participant_category_id = models.ForeignKey(ParticipantCategoryMaster, on_delete=models.CASCADE)
    event_name = models.CharField(max_length=80,null=True,)
    registration_fee = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    event_document = models.CharField(max_length=50, null=True, blank=True)
    event_type = models.CharField(max_length=20, null=True)
    max_team_size = models.IntegerField(null=True, blank=True)
    min_team_size = models.IntegerField(null=True, blank=True)
    abbreviation = models.CharField(max_length=20, null=True)
    max_registration = models.IntegerField(null=True, blank=True)
    event_description = models.TextField(null=True, blank=True)
    video_file = models.FileField(upload_to='media/', null=True)
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=20, null=True)
    modified_on = models.DateTimeField(null=True)
    modified_by = models.CharField(max_length=20, null=True)

    def __str__(self):
        return f"Event - {self.id}"

class EventScheduler(models.Model):
    event_master_id = models.ForeignKey(EventMaster, on_delete=models.CASCADE)
    event_start_date = models.DateField(null=True, blank=True)
    event_end_date = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=20, null=True)
    modified_on = models.DateTimeField(null=True)
    modified_by = models.CharField(max_length=20, null=True)

    def __str__(self):
        return f"EventScheduler - {self.id}"

class SponsorMaster(models.Model):
    festival_master_header_id = models.ForeignKey(FestivalMasterHeader, on_delete=models.CASCADE,null=True)
    event_master_id = models.ForeignKey(EventMaster, on_delete=models.CASCADE,null=True)
    sponsor_type =  models.TextField(null=True, blank=True)
    sponsor_name = models.CharField(max_length=50)
    sponsor_logo = models.CharField(max_length=50, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=20, null=True)
    modified_on = models.DateTimeField(null=True)
    modified_by = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.sponsor_name

class WinnerPositionMasterModel(models.Model):
    winner_position = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=20, null=True)
    modified_on = models.DateTimeField(null=True)
    modified_by = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.winner_position

class PrizeTypeMasterModel(models.Model):
    prize_type = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=20, null=True)
    modified_on = models.DateTimeField(null=True)
    modified_by = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.prize_type

class EventPrizeMaster(models.Model):
    event_master_id = models.ForeignKey(EventMaster, on_delete=models.CASCADE)
    winner_position_id = models.ForeignKey(WinnerPositionMasterModel, on_delete=models.CASCADE)
    prize_type_id = models.ForeignKey(PrizeTypeMasterModel, on_delete=models.CASCADE)
    event_cash_prize = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    event_scores = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=20, null=True)
    modified_on = models.DateTimeField(null=True)
    modified_by = models.CharField(max_length=20, null=True)

    def __str__(self):
        return f"EventPrize - {self.id}"

class ParticipantTypeMaster(models.Model):
    participant_type = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=20, null=True)
    modified_on = models.DateTimeField(null=True)
    modified_by = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.participant_type

class ParticipantRegistrationHeader(models.Model):
    event_master_id = models.ForeignKey(EventMaster, on_delete=models.CASCADE)
    college_name = models.CharField(max_length=500,null=True)
    reference_by = models.TextField(null=True, blank=True)
    event_chest_no = models.CharField(max_length=20, null=True, blank=True)
    receipt_no = models.CharField(max_length=20, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=20, null=True)
    modified_on = models.DateTimeField(null=True)
    modified_by = models.CharField(max_length=20, null=True)

    def __str__(self):
        return f"ParticipantRegistrationHeader - {self.id}"

class ParticipantRegistrationChild(models.Model):
    participant_registration_header_id = models.ForeignKey(ParticipantRegistrationHeader, on_delete=models.CASCADE)
    participant_name = models.CharField(max_length=100)
    participant_type_id = models.ForeignKey(ParticipantTypeMaster, on_delete=models.SET_NULL, null=True, blank=True)
    participant_id_no = models.CharField(max_length=20, null=True, blank=True)
    participant_phone = models.CharField(max_length=15, null=True, blank=True)
    participant_email = models.EmailField(max_length=50,null=True)
    participant_id_card = models.CharField(max_length=500, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=20, null=True)
    modified_on = models.DateTimeField(null=True)
    modified_by = models.CharField(max_length=20, null=True)

    def __str__(self):
        return f"ParticipantRegistrationChild - {self.id}"

class ParticipantRegistrationPayment(models.Model):
    participant_registration_header_id = models.ForeignKey(ParticipantRegistrationHeader, on_delete=models.CASCADE)
    registration_fee = models.DecimalField(max_digits=6, decimal_places=2)
    payment_type = models.BooleanField(default=True)
    payment_status = models.IntegerField()
    transaction_id = models.TextField(null=True, blank=True)
    registration = models.CharField(max_length=20, null=True)
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=20, null=True)
    modified_on = models.DateTimeField(null=True)
    modified_by = models.CharField(max_length=20, null=True)

    def __str__(self):
        return f"ParticipantRegistrationPayment - {self.id}"

class EventResult(models.Model):
    event_master_id = models.ForeignKey(EventMaster, on_delete=models.CASCADE)
    winner_position_id = models.ForeignKey(WinnerPositionMasterModel, on_delete=models.CASCADE)
    participant_registration_header_id = models.ForeignKey(ParticipantRegistrationHeader, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=20, null=True)
    modified_on = models.DateTimeField(null=True)
    modified_by = models.CharField(max_length=20, null=True)

    def __str__(self):
        return f"EventResult - {self.id}"

class GalleryMaster(models.Model):
    event_result_id = models.ForeignKey(EventResult, on_delete=models.CASCADE)
    gallery_photo = models.CharField(max_length=50, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=20, null=True)
    modified_on = models.DateTimeField(null=True)
    modified_by = models.CharField(max_length=20, null=True)

    def __str__(self):
        return f"GalleryMaster - {self.id}"

class UserType(models.Model):
    usertype = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.usertype

class UserMaster(models.Model):
    organizing_committe_master_id = models.ForeignKey(OrganizingCommitteMaster, on_delete=models.CASCADE,null=True)
    login_id = models.CharField(max_length=30)
    login_password = models.CharField(max_length=250)
    user_type_id = models.ForeignKey(UserType, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=20, null=True)
    modified_on = models.DateTimeField(null=True)
    modified_by = models.CharField(max_length=20, null=True)

    def __str__(self):
        return f"UserMaster - {self.id}"

class MenuHeader(models.Model):
    name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=20, null=True)
    modified_on = models.DateTimeField(null=True)
    modified_by = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.name

class MenuChild(models.Model):
    menu_header_id = models.ForeignKey(MenuHeader, on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=50)
    url = models.CharField(max_length=50, null=True)
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=20, null=True)
    modified_on = models.DateTimeField(null=True)
    modified_by = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.name
