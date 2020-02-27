from django.db import models
from django.utils.translation import ugettext_lazy as _


class Student(models.Model):
    STATUS_PRESENT = 'p'
    STATUS_MISSING = 'm'

    STATUS_CHOICES = (
        (STATUS_PRESENT, _('Present')),
        (STATUS_MISSING, _('Missing'))
    )
    first_name = models.CharField(max_length=30, verbose_name=_('First name'))
    last_name = models.CharField(max_length=30, verbose_name=_('Last name'))
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, verbose_name=_('Status'))
    date = models.DateTimeField(verbose_name=_('Date'))

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name, self.status, self.date)

    def get_status_display(self):
        return next([status for status in self.STATUS_CHOICES if status == self.status])

    class Meta:
        verbose_name_plural = _('Students')
        verbose_name = _('Student')

