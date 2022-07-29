from django.urls import path
from . import views

urlpatterns = [
    path('',views.home_view,name='home'),
    path('home',views.home_view,name='home'),
    path('sign-up',views.sign_up,name='sign_up'),
    path('create-post',views.create_post,name='create_post'),
    path('preview-post/<int:my_id>',views.preview_post,name='preview_post'),
    path('all-post',views.all_post,name='all_post'),
    #path('post-pdf/<int:my_id>',views.post_pdf,name='pdf_post'),
    path('pdf/<int:my_id>', views.GeneratePdf.as_view()),
    path('edit-post/<int:my_id>',views.edit_post,name='edit_post'),
]
