"""
إعدادات الترقيم المخصصة للمشروع
تحدد الحد الأقصى لحجم الصفحة لمنع استرجاع كميات ضخمة من البيانات دفعة واحدة
"""

from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class StandardResultsSetPagination(PageNumberPagination):
    # الإصدار 11: تحديد الحد الأقصى لحجم الصفحة بـ 100 نتيجة لمنع استرجاع البيانات بكميات كبيرة
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 100

    def get_paginated_response(self, data):
        return Response({
            'count': self.page.paginator.count,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'results': data,
        })
