from django.conf.urls import url

from healing_chakra_app.views import SignUpRequest, LoginRequest, GetUser, SaveMedicieneDonation, GetDonatedMedicine, SaveEquipmentDonation, GetDonatedEquipment

urlpatterns = [
    # url(r'^send_questionnaire/$', NiceTcoQuestionnaire.as_view()),
    url(r'^sign-up/$', SignUpRequest.as_view()),
    url(r'^login/$', LoginRequest.as_view()),
    url(r'^get-user/$', GetUser.as_view()),
    url(r'^submit-medicine-donation/$', SaveMedicieneDonation.as_view()),
    url(r'^submit-equipment-donation/$', SaveEquipmentDonation.as_view()),
    url(r'^get-medicine-donations/$', GetDonatedMedicine.as_view()),
    url(r'^get-equipment-donations/$', GetDonatedEquipment.as_view())
]