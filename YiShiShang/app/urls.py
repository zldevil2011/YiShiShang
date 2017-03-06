from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
from app.views import data_collect

urlpatterns = [
    url(r'^index/', TemplateView.as_view(template_name="app/index.html")),
    url(r'^introduction/', TemplateView.as_view(template_name="app/introduction.html")),
    url(r'^data_collect/', data_collect, name="data_collect"),
    url(r'^result_share/', TemplateView.as_view(template_name="app/result_share.html")),
]