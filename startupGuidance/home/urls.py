from django.urls import path
from . import views
from forum import views as forum_view
urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('join_us', views.join_us, name='join_us'),
    path('to_forum', forum_view.post_list, name='to_forum'),
    path('to_predict', views.predict, name="to_predict"),
    path('find_unique', views.find_unique, name="find_unique"),
    # path('predict', views.predict, name="predict"),
]
