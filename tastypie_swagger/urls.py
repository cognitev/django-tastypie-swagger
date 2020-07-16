from .views import SwaggerView, ResourcesView, SchemaView
try:
    from django.urls import include, re_path

    urlpatterns = [
        re_path(r'^$', SwaggerView.as_view(), name='index'),
        re_path(r'^resources/$', ResourcesView.as_view(), name='resources'),
        re_path(r'^schema/(?P<resource>\S+)$', SchemaView.as_view()),
        re_path(r'^schema/$', SchemaView.as_view(), name='schema'),
    ]
except ImportError:
    from django.conf.urls import include, url

    urlpatterns = [
        url(r'^$', SwaggerView.as_view(), name='index'),
        url(r'^resources/$', ResourcesView.as_view(), name='resources'),
        url(r'^schema/(?P<resource>\S+)$', SchemaView.as_view()),
        url(r'^schema/$', SchemaView.as_view(), name='schema'),
    ]

