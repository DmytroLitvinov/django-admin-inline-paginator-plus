import unittest

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

from django_admin_inline_paginator_plus.apps import DjangoAdminInlinePaginatorPlusConfig


class TestDjangoAppConfig(unittest.TestCase):
    def test_valid_subclass_appconfig(self):
        self.assertEqual(issubclass(DjangoAdminInlinePaginatorPlusConfig, AppConfig), True)

    def test_valid_name(self):
        name = DjangoAdminInlinePaginatorPlusConfig.name
        self.assertEqual(isinstance(name, str), True)
        self.assertEqual(name, 'django_admin_inline_paginator_plus')

    def test_valid_verbose_name(self):
        verbose_name = DjangoAdminInlinePaginatorPlusConfig.verbose_name
        self.assertEqual(verbose_name, _('Django Admin Inline Paginator'))
