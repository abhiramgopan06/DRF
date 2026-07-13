from django.urls import path,include
from .views import BookViewSet,BookAPIView,UserViewSet,PermissionDemoViewSet, TaskViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r"books",BookViewSet)
router.register(r'auth',UserViewSet, basename='auth')
router.register(r"demo",PermissionDemoViewSet,basename='demo')
router.register(r"tasks",TaskViewSet, basename='tasks')

urlpatterns = [
 path('',include(router.urls)), # http://127.0.0.1:0000/api/
 path('books-api/',BookAPIView.as_view())
]

#http://127.0.0.1:0000/api/books      POST    =   Book is added to Book table
#http://127.0.0.1:0000/api/books      GET     =   All books from Book table is retreived
#http://127.0.0.1:0000/api/books/1/   GET     =   Book with id 1 is retreaved
#http://127.0.0.1:0000/api/books/1/   PUT     =   Book with id 1 is updated fully
#http://127.0.0.1:0000/api/books/1/   PATCH   =   Book with id 1 is updated partially
#http://127.0.0.1:0000/api/books/1/   DELETE  =   Book with id 1 is removed


#http://127.0.0.1:0000/api/books-api      POST    =   Book is added to Book table
#http://127.0.0.1:0000/api/books-api      GET     =   All books from Book table is retreived

# http://127.0.0.1:0000/api/auth/register/    POST
# http://127.0.0.1:0000/api/auth/login/       POST
# http://127.0.0.1:0000/api/auth/me/          GET , POST
# http://127.0.0.1:0000/api/auth/logout/      POST



# http://127.0.0.1:0000/api/demo/open_route/      GET