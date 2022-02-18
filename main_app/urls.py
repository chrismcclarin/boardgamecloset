from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('games/', views.games_index, name='games'),
# Games
    path('games/<int:game_id>/', views.games_detail, name='detail'),
    path('games/create/', views.GameCreate.as_view(), name='games_create'),
    path('games/<int:pk>/update', views.GameUpdate.as_view(), name='games_update'),
    path('games/<int:pk>/delete', views.GameDelete.as_view(), name='games_delete'),
# Many to many
    path('games/<int:game_id>/assoc_sale/<int:sale_id>', views.assoc_sale, name='assoc_sale'),
    path('games/<int:game_id>/rm_assoc_sale/<int:sale_id>', views.rm_assoc_sale, name='rm_assoc_sale'),
# Game Time - OTM
    path('games/<int:game_id>/new_gametime', views.new_gametime, name='new_gametime'),
# Sale Location
    path('salelocation/', views.sale_index, name='sale'),
    path('salelocation/<int:sale_id>/', views.sale_detail, name='sale_detail'),
    path('salelocation/create/', views.SaleCreate.as_view(), name='sale_create'),
    path('salelocation/<int:pk>/update/', views.SaleUpdate.as_view(), name='sale_update'),
    path('salelocation/<int:pk>/delete/', views.SaleDelete.as_view(), name='sale_delete'),

]