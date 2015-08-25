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

from mtaube.apps.portfolio.models import Project


class ProjectForm(forms.ModelForm):

    class Meta:
        exclude = ['slug']
        model = Project


class ProjectAdmin(admin.ModelAdmin):
    exclude = ['slug']
    form = ProjectForm
    list_display = [
        'title',
        'client_name',
        'is_active',
        'is_locked',
        'order',
    ]


admin.site.register(Project, ProjectAdmin)
