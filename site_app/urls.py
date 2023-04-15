from django.urls import path
import site_app.views as view


urlpatterns = [
    path('', view.main_view, name='main-page'),
    path('test_url/', view.test_url, name='test_url'),

]
