from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter



router=DefaultRouter()
router.register('employees',views.employeeviewset, basename='employee')

urlpatterns = [
    path('students/',views.studentsview),
    path('students/<int:pk>/',views.studentdetailview),

    #path('employees/',views.employees.as_view()),
    #path('employees/<int:pk>/',views.employeesdetail.as_view()),

    path('', include(router.urls)),
    path('blogs/',views.blogsviews.as_view()),
    path('comments/',views.commentviews.as_view()),


    path('blogs/<int:pk>/',views.blogdetailview.as_view()),
    path('comments/<int:pk>/',views.commentdetailview.as_view()),
]
