# Copyright 2015 Matt Taube
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from django.contrib import admin
from django import forms

from redactor.widgets import RedactorEditor

from mtaube.apps.common.models import MediaPanel, Page, Quote


class PageForm(forms.ModelForm):
    """Base ModelForm for Page and all subclasses"""

    class Meta:
        exclude = ['slug']
        model = Page
        widgets = {
            'content': RedactorEditor(),
            'content_secondary': RedactorEditor()
        }


class PageAdmin(admin.ModelAdmin):
    """Base ModelAdmin for Page and all subclasses"""
    form = PageForm
    list_display = [
        'title',
        'slug',
    ]


admin.site.register(MediaPanel)
admin.site.register(Page, PageAdmin)
admin.site.register(Quote)
