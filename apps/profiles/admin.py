from django.contrib import admin
# my models
from . models import *

# show in admin panel
admin.site.register(Progress)
admin.site.register(ExtraUser)
admin.site.register(ArchiveUser)
admin.site.register(ThoughtUser)
admin.site.register(CommentThinkUser)
admin.site.register(FavoriteUser)
admin.site.register(FavoritePost)
admin.site.register(AlreadyIp)

