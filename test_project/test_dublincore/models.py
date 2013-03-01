from django.db import models
from django.contrib.contenttypes import generic

from dublincore.models import QualifiedDublinCoreElement

# Create your models here.
class Thing(models.Model):
    '''Test thing has no data just associated QDC'''
    QDCElements = generic.GenericRelation(QualifiedDublinCoreElement)

    def title(self):
        titles = self.QDCElements.filter(term='T')
        return titles[0] if titles else None

    def description(self):
        descriptions = self.QDCElements.filter(term='DSC')
        return descriptions[0] if descriptions else None

    def subject(self):
        subjects = self.QDCElements.filter(term='SUB')
        return subjects[0] if subjects else None

    def creator(self):
        creators = self.QDCElements.filter(term='CR')
        return creators[0] if creators else None
