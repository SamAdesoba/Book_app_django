from django.contrib.admin.apps import AdminConfig


class MyDjangoProjectAdminConfig(AdminConfig):
    default_site = "my_django_project.admin.MyDjangoProjectAdminSite"
