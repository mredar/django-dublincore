from django.contrib import admin
from DublinCore.models import QualifiedDublinCoreElement, QualifiedDublinCoreElementHistory

class QDCElementAdmin(admin.ModelAdmin):
    list_display = ('id', 'term', 'qualifier', 'content_', 'content_type', 'updated_at', 'created_at', 'content_object')
    search_fields = ('content', 'term', 'qualifier'  )
    list_filter = ('content_type', 'term' )
    save_on_top = True

    def content_(self, obj):
        return obj.content[0:50] if len(obj.content) <50 else obj.content[0:50]+'...'
    content_.admin_order_field = 'content'

admin.site.register(QualifiedDublinCoreElement, QDCElementAdmin)

class QDCElementHistoryAdmin(QDCElementAdmin):
    list_display = QDCElementAdmin.list_display[:-1] + ( 'qdce', 'qdce_id_stored')
admin.site.register(QualifiedDublinCoreElementHistory, QDCElementHistoryAdmin)
