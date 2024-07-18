from django.urls import path

from app.views import *

urlpatterns = [
    path('', index, name='index'),
    path('blog/', blog, name='blog'),
    path('about/', about, name='about'),
    path('conact/', contact, name='contact'),
    path('class_/', class_, name='class'),
    path('feature/', feature, name='feature'),
    path('blog/<slug:slug>/', single_view, name='single'),

]