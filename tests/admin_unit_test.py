import unittest

from django.contrib.admin.views.main import ChangeList

from django_admin_inline_paginator_plus.admin import (
    InlineChangeList,
    PaginationFormSetBase,
)


class TestInlineChangeList(unittest.TestCase):
    """Test cases for InlineChangeList admin"""

    def test_default_values(self):
        self.assertEqual(InlineChangeList.can_show_all, True)
        self.assertEqual(InlineChangeList.multi_page, True)
        self.assertEqual(InlineChangeList.get_query_string, ChangeList.__dict__['get_query_string'])

    def test_init_values(self):
        """Test case for correct initialization class"""
        pass

    #     cl = InlineChangeList(request, page_num, paginator)
    #     cl.page_num = page_num
    #     cl.paginator = paginator
    #     cl.result_count = paginator.count

    #     cl.show_all = 'all' in request.GET
    #     cl.params = dict(request.GET.items())


class TestPaginationFormSetBase(unittest.TestCase):
    def test_default_values(self):
        """Test case to check if the default was a value set"""
        self.assertEqual(PaginationFormSetBase.queryset, None)
        self.assertEqual(PaginationFormSetBase.request, None)
        self.assertEqual(PaginationFormSetBase.per_page, 20)

    def test_get_page_num(self):
        """Test case to check correct getting page number"""
        pass

    def test_get_page(self):
        """Test case to check correct getting page"""
        pass

    def test_mount_paginator(self):
        """Test case for method mount_paginator"""
        pass

    def test_mount_queryset(self):
        """Test case for method mount_queryset"""
        pass

    def test_init(self):
        """Test case for correct initialization class"""
        pass
