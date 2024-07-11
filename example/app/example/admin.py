from django.contrib.admin import ModelAdmin, register
from django_admin_inline_paginator_plus.admin import (
    StackedInlinePaginated,
    TabularInlinePaginated,
)

from .models import Country, Region, State


class StateAdminInline(TabularInlinePaginated):
    model = State
    fields = ('name', 'active')
    per_page = 5
    pagination_key = 'state_page'


class CollapsedStateAdminInline(StateAdminInline):
    verbose_name = 'State Collapsed'
    verbose_name_plural = 'States Collapsed'
    pagination_key = 'state_collapsed_page'
    classes = ['collapse']


class RegionAdminInline(StackedInlinePaginated):
    model = Region
    fields = ('name', 'active')
    per_page = 2
    pagination_key = 'region_page'


@register(Country)
class CountryAdmin(ModelAdmin):
    model = Country
    fields = ('name', 'active')
    inlines = (StateAdminInline, CollapsedStateAdminInline, RegionAdminInline)
