
from django.urls import path
from .views import *
urlpatterns = [
    path('createBook/',createBook.as_view(),name="createBook"),
    path('listOutBook/',listOutBook.as_view(),name="listOutBook"),
    path('updateBook/<int:id>/',updateBook.as_view(),name="updateBook"),
    path("retriveBook/<int:id>/",retriveBook.as_view(),name="retriveBook"),
    path("deleteBook/<int:id>/",deleteBook.as_view(),name="deleteBook"),  
    path("borrowBook/<int:id>/",borrowBook.as_view(),name="borrowBook"),
    path("returnBook/<int:id>/",returnBook.as_view(),name="returnBook"),

    
]
