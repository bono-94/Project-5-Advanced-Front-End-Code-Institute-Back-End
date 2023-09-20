# # POST ADMIN
# @admin.register(Post)
# class PostAdmin(SummernoteModelAdmin):

#     list_display = (
#         'post_type',
#         'title',
#         'industry',
#         'author',
#         'created_on',
#         'status',
#         'post_verification',
#     )

#     search_fields = [
#         'title',
#         'caption',
#         'author',
#         'project_owner',
#         'organization',
#         'project',
#         'product',
#         'service',
#         'post_location_city',
#         'post_location_country',
#         'post_location_continent',
#         'post_location_planet',
#         'business_knowledge',
#     ]

#     list_filter = (
#         'status',
#         'post_verification',
#         'public_privacy',
#         'post_type',
#         'funding_infinite_end_date',
#     )

#     summernote_fields = (
#         'business_knowledge',
#         'caption',
#         'introduction'
#     )

#     prepopulated_fields = {'slug': ('title',)}

#     # ACTIONS
#     actions = ['approved_post', 'frozen_post']

#     def approved_post(self, request, queryset):
#         queryset.update(status=1)

#     def frozen_post(self, request, queryset):
#         queryset.update(status=0)