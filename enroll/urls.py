from django.urls import path
from .views import *
app_name='enroll'
urlpatterns = [
    path('',enroll_choose, name='enroll_choose'),
    path("create_class/",create_class_view,name='create_class'),
    path("my_class/",my_class_oprator_view,name='my_class'),
    path('my_class_student/',my_class_student_view,name='my_class_student'),
    path('report_student/<int:id_enroll>/',report_general_student_view,name='report'),
    path('report/point/detail/',report_point_detail_view,name='point_report_studnet')



]