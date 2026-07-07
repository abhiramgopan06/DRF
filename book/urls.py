from django.urls import path,include
from .views import BookViewSet,BookAPIView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r"books",BookViewSet)

urlpatterns = [
 path('',include(router.urls)),
 path('books-api/',BookAPIView.as_view())
]

#http://127.0.0.1:0000/api/books      POST    =   Book is added to Book table
#http://127.0.0.1:0000/api/books      GET     =   All books from Book table is retreived
#http://127.0.0.1:0000/api/books/1/   GET     =   Book with id 1 is retreaved
#http://127.0.0.1:0000/api/books/1/   PUT     =   Book with id 1 is updated fully
#http://127.0.0.1:0000/api/books/1/   PATCH   =   Book with id 1 is updated partially
#http://127.0.0.1:0000/api/books/1/   DELETE  =   Book with id 1 is removed



