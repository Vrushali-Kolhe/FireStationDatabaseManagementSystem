"""fireStationDatabase URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from . import views
from . import headofficer_views
urlpatterns = [
    #path('',views.homePage),
    path('', views.showLoginPage),
    path('dologin',views.doLogin),
    path('admin_home',headofficer_views.admin_home),
    path('add_staff',headofficer_views.add_staff),
    path('manage_staff',headofficer_views.manage_staff),
    path('edit_staff/<str:staff_id>',headofficer_views.edit_staff),
    path('edit_staff_save',headofficer_views.edit_staff_save),
    path('add_staff_save',headofficer_views.add_staff_save),
    path('add_station',headofficer_views.add_station),
    path('add_station_save',headofficer_views.add_station_save),
    path('manage_station', headofficer_views.manage_station),
    path('edit_station/<str:station_id>', headofficer_views.edit_station),
    path('edit_station_save', headofficer_views.edit_station_save),
    path('add_vehicle_type', headofficer_views.add_vehicle_type),
    path('add_vehicle_type_save', headofficer_views.add_vehicle_type_save),
    path('manage_vehicle_type', headofficer_views.manage_vehicle_type),
    path('edit_vehicle_type/<str:vehicle_type_id>', headofficer_views.edit_vehicle_type),
    path('edit_vehicle_type_save', headofficer_views.edit_vehicle_type_save),
    path('add_vehicle', headofficer_views.add_vehicle),
    path('add_vehicle_save', headofficer_views.add_vehicle_save),
    path('manage_vehicle', headofficer_views.manage_vehicle),
    path('edit_vehicle/<str:vehicle_id>', headofficer_views.edit_vehicle),
    path('edit_vehicle_save', headofficer_views.edit_vehicle_save),
    path('make_report', headofficer_views.make_report),
    path('make_report_save',headofficer_views.make_report_save),
    path('add_complainer',headofficer_views.add_complainer),
    path('add_complainer_save',headofficer_views.add_complainer_save),
    path('add_action',headofficer_views.add_action),
    path('add_action_save',headofficer_views.add_action_save),
    path('get_user_details', views.getUserDetails),
    path('logout_user', views.logoutUser),
    path('demo',views.showDemoPage),
]
