"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),   
    path('auth/registration/', include('dj_rest_auth.registration.urls')), 

    path('api/auth/', include(('Authentication.urls' , 'Authentication'), namespace='auth')),
    path('api/students/', include(('Students.urls' , 'Students'), namespace='students')),
    path('api/instructors/', include(('Instructors.urls' , 'Instructors'), namespace='instructors')),
    path('api/courses/', include(('Courses.urls' , 'Courses' ), namespace='courses')),
    path('api/sessions/', include(('Sessions.urls' , 'Sessions' ), namespace='sessions')),
    path('api/enrollments/', include(('Enrollments.urls' ,'Enrollments'), namespace='enrollments')),
    path('api/assignments/', include(('Assignments.urls' , 'Assignments' ), namespace='assignments')),
    path('api/reports/', include(('Reports.urls' , 'Reports' ) , namespace='reports')),
    path('api/notifications/', include(('Notifications.urls', 'Notifications'), namespace='notifications')),

]
