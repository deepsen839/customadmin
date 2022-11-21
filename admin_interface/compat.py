# -*- coding: utf-8 -*-

import django
from django.core.validators import FileExtensionValidator
from django.urls import NoReverseMatch, reverse

from django.utils.encoding import force_str
from django.utils.translation import gettext_lazy
