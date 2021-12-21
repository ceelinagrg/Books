from django.urls import path,include
from books import views
from books.views import BookViewset, HeroInfoViewset
from rest_framework.routers import DefaultRouter

apps = 'books'

# list_action = {
#      'get' : 'list',
#     'post' : 'create'
# }

# detail_action = {
#     'get':'retrieve',
#     'put': 'update',
#     'patch':'partial_update',
#     'delete': 'destroy'
# }

# readonly_action ={
#     'get': 'retrieve'
# }
# book_list = BookViewset.as_view(list_action)

# book_detail = BookViewset.as_view(detail_action)

# heroinfo_list = HeroInfoViewset.as_view(list_action)

# heroinfo_detail = HeroInfoViewset.as_view(readonly_action)


router = DefaultRouter()
router.register(r'books', views.BookViewset)
router.register(r'heroinfo', views.HeroInfoViewset)

urlpatterns = [
    path('', include(router.urls)),
]