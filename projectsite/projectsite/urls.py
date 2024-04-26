from django.contrib import admin
from django.urls import path

from fire.views import HomePageView
from fire import views 
from fire.views import HomePageView, ChartView

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', HomePageView.as_view(), name='home'),
    path('dashboard_chart', ChartView.as_view(), name='dashboard-chart'),

]
