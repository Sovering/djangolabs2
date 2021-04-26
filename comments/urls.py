from django.urls import path

from . import views

urlpatterns = [
    path("", views.ServMonView.as_view(), name='serv_mon_list'),
    path("<slug:slug>", views.ServDetail.as_view(), name='serv_mon_detail'),
    path("create/", views.ServCreateView.as_view(), name='serv_mon_add'),
    path("export/<int:pk>", views.export, name='serv_mon_download'),
    path("pdf_list/", views.PdfMakerView.as_view(), name='pdf_list'),
    path("pdf_list/<slug:slug>/", views.PdfMakerDetail.as_view(), name='pdf_detail'),
    path("pdf_create/", views.PdfMakerCreateView.as_view(), name='pdf_create'),
    path("pdf_list/pdf_export/<int:pk>/", views.pdf_export, name='pdf_export'),
]
