
from django.urls import path
from .views import *
urlpatterns = [
    path('signup/',Registration.as_view(),name="signup"),
    path('login/',MyTokenObtainPairView.as_view(),name="login"),

    path('createMember/',createMember.as_view(),name="createMember"),
    path('listOutMember/',listOutMember.as_view(),name="listOutMember"),
    path('updateMember/<int:id>/',updateMember.as_view(),name="updateMember"),
    path("retriveMember/<int:id>/",retriveMember.as_view(),name="retriveMember"),
    path("deleteMember/<int:id>/",deleteMember.as_view(),name="deleteMember"),
    path("deleteMyAccount/",deleteMyAccount.as_view(),name="deleteMyAccount"),

]
