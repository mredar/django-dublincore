from DublinCore.models import  QualifiedDublinCoreElement

class QDCElementTestCase(TestCase):
    fixtures = ['xtf.qualifieddublincoreelementTest.json',]# 'xtf.arkobjecttestcase.json', 'auth.json', ] # 'sites.json']

####    def setUp(self):
####        super(QDCElementTestCase, self).setUp()
####        os.environ['XTF_DATA'] = os.path.abspath(os.path.join(os.path.dirname(__file__), "data/xtf/data/"))
####        try:
####            dc = QualifiedDublinCoreElement.objects.get(pk=1)
####        except QualifiedDublinCoreElement.DoesNotExist:
####            print "++++++ LOADING QDC Elements +++++"
####            print "++++++ DCTerms currently:", DublinCoreTerm.objects.count()
####            from django.core.management import call_command
####            call_command("migrate", 'xtf', '0011', fake=True)#need to fake all but relevant, they've been run but not recorded?
####            call_command("migrate", 'xtf', '0012_copy_existing_DCT_to_DCElements')
####            print "+++++ LOADED ", QualifiedDublinCoreElement.objects.count(), " QDCElements from existing DCTerms (elements)+++++"

    def testQDC(self):
        dc = QualifiedDublinCoreElement.objects.get(pk=76)
        if QualifiedDublinCoreElement.objects.count()==76:
            self.assertEqual(dc.qdc, '<subject q="series">Pomona Public Library - The Frasher Foto Postcard Collection</subject>')
        else:
            self.assertEqual(dc.qdc, '<title>Ruins of Ray\'s Famous Dance Hall at Compton Calif.</title>') 

    def testQDCE_extended_term_save(self):
        '''Test the saving of an extended term from the DCTERMS'''
        q=QualifiedDublinCoreElement()
        q.term = 'RH'
        q.content = 'XXXXX  TEXT XXXXX'
        q.object_id = 9
        q.content_type = ContentType.objects.get(app_label='xtf', model='arkobject')
        self.assertRaises(ValueError, q.save)
        q.term = 'T'
        q.save()

    def test_dc_xml_saved(self):
        '''Check that the dc.xml file is saved when a qdc element is saved'''
        dc = QualifiedDublinCoreElement.objects.get(pk=427)
        print "XTF_DATA", os.environ['XTF_DATA']
        a = dc.content_object
        if not os.path.exists(a.dc_xml_filepath):
            os.makedirs(os.path.dirname(a.dc_xml_filepath))
        orig_time = os.path.getmtime(a.dc_xml_filepath) if os.path.isfile(a.dc_xml_filepath) else time.time()
        dc.content = 'XXXXXX'
        dc.save()
        new_time = os.path.getmtime(a.dc_xml_filepath)
        self.assertTrue(new_time > orig_time)
