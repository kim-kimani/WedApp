from django.contrib import admin
from .models import WeddingDetails, Media, RSVP, Message, Gallery

# Register your models here.
class WeddingDetailsAdmin(admin.ModelAdmin):
    list_display = ('bride', 'groom', 'date', 'ceremony_time')
    
class RSVPAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'attendance', 'message', 'guest_count')
    
class MessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'recipient', 'text', 'approved')
    list_filter = ('approved', 'recipient')
    actions = ['approve_messages']

    def approve_messages(self, request, queryset):
        queryset.update(approved=True)
    approve_messages.short_description = "Approve selected messages"
    
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('name', 'uploaded_on')

admin.site.register(WeddingDetails, WeddingDetailsAdmin)
admin.site.register(Media)
admin.site.register(RSVP, RSVPAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(Gallery, GalleryAdmin)