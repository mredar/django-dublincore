from django.contrib import admin
import django.forms as forms
from django.contrib.contenttypes import generic
from dublincore.models import QualifiedDublinCoreElement
from test_dublincore.models import Thing

class QDCElementInlineForm(forms.ModelForm):
    class Meta:
        model = QualifiedDublinCoreElement
    def __init__(self, *args, **kwargs):
        super(QDCElementInlineForm, self).__init__(*args, **kwargs)
        self.fields['term'] = forms.ChoiceField(choices=(('-','------'),)+QualifiedDublinCoreElement.DCELEMENTS)

class QDCElementInline(generic.GenericTabularInline):
    model = QualifiedDublinCoreElement
    extra = 0
    form = QDCElementInlineForm

class ThingAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'description', 'subject', 'creator')
    inlines = (QDCElementInline,)

admin.site.register(Thing, ThingAdmin)
