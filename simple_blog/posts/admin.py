"""simple_blog/posts/admin.py"""

# Django modules
from django.contrib import admin

# My modules
from posts.models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Post admin"""

    list_display = ('id', 'user', 'title', 'image_header')
    search_fields = ('title', 'user__username', 'user__email')
    list_filter = ('created', 'modified')

    def get_form(self, request, obj=None, **kwargs):
        self.exclude = ('url',)
        form = super(PostAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['user'].initial = request.user
        form.base_fields['profile'].initial = request.user.profile
        return form