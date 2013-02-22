#import logging
#logger = logging.getLogger(__name__)

###import codecs #for writing utf-8 files
###import lxml.etree as ET
###import json
import xml.sax.saxutils as saxutils
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.utils.safestring import mark_safe
###from django.utils.datastructures import SortedDict
###import south.modelsinspector
###

class AbstractQualifiedDublinCoreTerm(models.Model):
    ''' Abstract class for encapsulating Dublin Core metadata element. We support the extended terms list of DC.
    '''
    class Meta:
        abstract = True
        ordering = ['term',]

    DCTERMS = (\
                ('AB', 'Abstract'),
                ('AR', 'AccessRights'),
                ('AM', 'AccrualMethod'),
                ('AP', 'AccrualPeriodicity'),
                ('APL', 'AccrualPolicy'),
                ('ALT', 'Alternative'),
                ('AUD', 'Audience'),
                ('AVL', 'Available'),
                ('BIB', 'BibliographicCitation'),
                ('COT', 'ConformsTo'),
                ('CN', 'Contributor'),
                ('CVR', 'Coverage'),
                ('CRD', 'Created'),
                ('CR', 'Creator'),
                ('DT', 'Date'),
                ('DTA', 'DateAccepted'),
                ('DTC', 'DateCopyrighted'),
                ('DTS', 'DateSubmitted'),
                ('DSC', 'Description'),
                ('EL', 'EducationLevel'),
                ('EXT', 'Extent'),
                ('FMT', 'Format'),
                ('HFMT', 'HasFormat'),
                ('HPT', 'HasPart'),
                ('HVS', 'HasVersion'),
                ('ID', 'Identifier'),
                ('IM', 'InstructionalMethod'),
                ('IFMT', 'IsFormatOf'),
                ('IPT', 'IsPartOf'),
                ('IREF', 'IsReferencedBy'),
                ('IREP', 'IsReplacedBy'),
                ('IREQ', 'IsRequiredBy'),
                ('IS', 'Issued'),
                ('IVSN', 'IsVersionOf'),
                ('LG', 'Language'),
                ('LI', 'License'),
                ('ME', 'Mediator'),
                ('MED', 'Medium'),
                ('MOD', 'Modified'),
                ('PRV', 'Provenance'),
                ('PBL', 'Publisher'),
                ('REF', 'References'),
                ('REL', 'Relation'),
                ('REP', 'Replaces'),
                ('REQ', 'Requires'),
                ('RT', 'Rights'),
                ('RH', 'RightsHolder'),
                ('SRC', 'Source'),
                ('SP', 'Spatial'),
                ('SUB', 'Subject'),
                ('TOC', 'TableOfContents'),
                ('TE', 'Temporal'),
                ('T', 'Title'),
                ('TYP', 'Type'),
                ('VA', 'Valid'),
    )
    DCTERM_MAP = dict([(x[1].lower(), x[0]) for x in DCTERMS])
    DCTERM_CODE_MAP = dict([(x[0], x[1].lower()) for x in DCTERMS])
    DCTERM_LIST = [x[1].lower() for x in DCTERMS]

    object_id = models.CharField(max_length=255)
    content_type = models.ForeignKey(ContentType)
    # Don't want this constraint here. The history terms can't be related directly
    #content_object = generic.GenericForeignKey('content_type', 'object_id')
    term = models.CharField(max_length=4, choices=DCTERMS)
    qualifier = models.CharField(max_length=40, null=True, blank=True)
    content = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return ''.join([self.get_term_display(), ':', self.qualifier, ' = ', self.content[0:50], '...' if len(self.content)>50 else '' ]) if self.qualifier else ''.join([self.get_term_display(), ' = ', self.content[0:50], '...' if len(self.content) > 50 else '' ])

    @property
    def qdc(self):
        '''Return the qdc tag for the term
        '''
        start_tag = ''.join(('<', self.get_term_display().lower(), ' q="',
            self.qualifier, '">',)) if self.qualifier else ''.join(('<', self.get_term_display().lower(), '>', ))
        qdc = ''.join((start_tag, saxutils.escape(self.content), '</', self.get_term_display().lower(), '>',))
        return mark_safe(qdc)

    @property
    def objset_data(self):
        '''Return the terms representation for our objset interface.
        If there is no qualifier, return just the string content value.
        If there is a qualifier, return a dict of {q:qualifier, v:content}
        '''
        if not self.qualifier:
            return unicode(self.content)
        else:
            return dict(q=unicode(self.qualifier), v=unicode(self.content))


class QualifiedDublinCoreElement(AbstractQualifiedDublinCoreTerm):
    '''Dublin Core metadata element. Used to store ARKObject metadata
    using the Django content-type framework
    Needs to point at a live object.
    History terms will hold history for deleted objects
    '''
    content_object = generic.GenericForeignKey('content_type', 'object_id')

    def DCELEMENTS():
        element_codes = ('T', 'CR', 'SUB', 'DSC', 'PBL', 'CN', 'DT', 'TYP', 'FMT', 'ID', 'SRC', 'LG', 'REL', 'CVR', 'RT', )
        dce_ordered = []
        for code in element_codes:
            for ttuple in AbstractQualifiedDublinCoreTerm.DCTERMS:
                if ttuple[0] == code:
                    dce_ordered.append(ttuple)
        return tuple(dce_ordered)
    DCELEMENTS = DCELEMENTS()
    DCELEMENT_MAP = dict([(x[1].lower(), x[0]) for x in DCELEMENTS])
    DCELEMENT_CODE_MAP = dict([(x[0], x[1].lower()) for x in DCELEMENTS])
    DCELEMENT_LIST = [x[1].lower() for x in DCELEMENTS]

    def __init__(self, *args, **kwargs):
        if len(self.DCELEMENTS) != 15:
            raise Exception('QualifiedDublinCoreElement DCELEMENTS has'+str(len(self.DCELEMENTS))+'. It should have 15')
        super(QualifiedDublinCoreElement, self).__init__(*args, **kwargs)

    #TODO: on save, save related object dc if it has function...
    def save(self, *args, **kwargs):
        '''Make sure that the term is valid.
        If changed, create a QualifiedDublinCoreElementHistory object and save it.
        '''
        if not self.term in self.DCELEMENT_CODE_MAP:
            raise ValueError('Extended Dublin Core Terms such as '+self.DCTERM_CODE_MAP[self.term]+' are not allowed. Please use only Dublin Core Elements')
        #HOW TO TELL IF OBJECT CHANGED? RETRIEVE FROM DB and COMPARE
        changed = False
        if self.pk:# existing object
            db_self = QualifiedDublinCoreElement.objects.get(pk=self.pk)
            #compare values, if changed set changed!
            if self.term != db_self.term:
                raise ValueError('Can not change DC element')
            if self.content != db_self.content:
                changed = True
            if self.qualifier != db_self.qualifier:
                changed = True
            if changed:
                hist = QualifiedDublinCoreElementHistory()
                hist.qdce = self
                hist.object_id = db_self.object_id
                hist.content_type = db_self.content_type
                hist.term = db_self.term
                hist.qualifier = db_self.qualifier
                hist.content  = db_self.content
                hist.save()
        super(QualifiedDublinCoreElement, self).save(*args, **kwargs)
        obj = self.content_object
        if hasattr(obj, '_save_dc_xml_file'):
            obj._save_dc_xml_file()

    def delete(self, *args, **kwargs):
        hist = QualifiedDublinCoreElementHistory()
        hist.qdce = self
        hist.object_id = self.object_id
        hist.content_type = self.content_type
        hist.term = self.term
        hist.qualifier = self.qualifier
        hist.content  = self.content
        hist.save()
        super(QualifiedDublinCoreElement, self).delete(*args, **kwargs)


class QualifiedDublinCoreElementHistory(AbstractQualifiedDublinCoreTerm):
    ''' Store previous values of QualifiedDublinCoreElement with this.
    Subclassing is not the most db efficient but makes alot of stuff
    easier'''
    DCELEMENTS = QualifiedDublinCoreElement.DCELEMENTS
    DCELEMENT_MAP = QualifiedDublinCoreElement.DCELEMENT_MAP
    DCELEMENT_CODE_MAP = QualifiedDublinCoreElement.DCELEMENT_CODE_MAP
    DCELEMENT_LIST = QualifiedDublinCoreElement.DCELEMENT_LIST
    qdce = models.ForeignKey(QualifiedDublinCoreElement, null=True, on_delete=models.SET_NULL, related_name='history') 
    qdce_id_stored = models.PositiveIntegerField(help_text='Stores the id if the QulifiedDublinCoreElement the history points to is deleted.')#For when Foreign key deleted

    def save(self, *args, **kwargs):
        if self.qdce:
            self.qdce_id_stored = self.qdce.id
        super(QualifiedDublinCoreElementHistory, self).save(*args, **kwargs)
