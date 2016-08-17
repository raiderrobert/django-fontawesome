from django.db import models
from django.utils.translation import ugettext as _

from . import Icon
from forms import IconFormField

try:
    from django.db.models import SubfieldBase
    META_CLASS_TYPE = SubfieldBase
except ImportError:
    META_CLASS_TYPE = type


class IconField(models.Field):

    description = _('A fontawesome icon field')
    __metaclass__ = META_CLASS_TYPE

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 60
        kwargs['blank'] = True
        super(IconField, self).__init__(*args, **kwargs)

    def get_internal_type(self):
        return 'CharField'

    def to_python(self, value):
        if not value or value == 'None':
            return None

        if isinstance(value, Icon):
            return value

        # default => string
        return Icon(id=value)

    def get_prep_value(self, value):
        return str(value)

    def formfield(self, **kwargs):
        defaults = {
            'form_class':IconFormField,
            #'choices_form_class':IconFormField
        }

        defaults.update(kwargs)
        return super(IconField, self).formfield(**defaults)
