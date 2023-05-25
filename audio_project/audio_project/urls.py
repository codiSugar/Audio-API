from django.urls import path
from django.contrib import admin
from audio_api.views import get_audio_elements, create_audio_element, update_audio_element, delete_audio_element

urlpatterns = [
    path('admin/', admin.site.urls),
    path('projects/<int:project_id>/audio/', get_audio_elements),
    path('audio/', create_audio_element),
    path('audio/<int:audio_element_id>/', update_audio_element),
    path('audios/<int:audio_element_id>/', delete_audio_element),
]
