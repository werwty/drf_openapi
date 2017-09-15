# coding=utf-8
from django.contrib.admin.views.decorators import staff_member_required
from rest_framework import response
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import CoreJSONRenderer
from rest_framework.settings import import_from_string

from drf_openapi.codec import OpenAPIRenderer, SwaggerUIRenderer
from drf_openapi.entities import OpenApiSchemaGenerator
from drf_openapi.settings import DOC_SCHEMA_PERMISSION_DECORATOR

def get_schema_view(url, title):

    @api_view()
    @renderer_classes([CoreJSONRenderer, SwaggerUIRenderer, OpenAPIRenderer])
    def schema_view(request, version):
        generator = OpenApiSchemaGenerator(
            version=version,
            url=url,
            title=title
        )
        return response.Response(generator.get_schema(request))

    return import_from_string(DOC_SCHEMA_PERMISSION_DECORATOR,
                              'DOC_SCHEMA_PERMISSION_DECORATOR')(schema_view)
