from django.contrib import admin
from .models import ClientModel, MailModel, MessageModel, CodeMobileOperatorModel, TagModel


class DetailClientAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'code_mobile_operator', 'tag', 'timezone',)
    list_filter = ('phone_number', 'code_mobile_operator', 'tag', 'timezone',)
    search_fields = ('phone_number', 'code_mobile_operator', 'tag', 'timezone',)


class DetailMailAdmin(admin.ModelAdmin):
    list_display = ('start_date', 'end_date', 'text',)
    list_filter = ('start_date', 'end_date', 'text',)
    search_fields = ('start_date', 'end_date', 'text',)


class DetailMessageAdmin(admin.ModelAdmin):
    list_display = ('send_date', 'status', 'mail', 'client')
    list_filter = ('send_date', 'status', 'mail', 'client')
    search_fields = ('send_date', 'status', 'mail', 'client')


admin.site.register(ClientModel, DetailClientAdmin)
admin.site.register(MailModel, DetailMailAdmin)
admin.site.register(MessageModel, DetailMessageAdmin)
admin.site.register(CodeMobileOperatorModel)
admin.site.register(TagModel)

