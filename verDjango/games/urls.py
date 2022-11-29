from django.urls import path
from . import views

app_name = 'games'

urlpatterns = [
    path('', views.main_page, name='main'),
    path('othello/', views.othello, name='othello'),
    path('othello/ai/<int:room_id>/', views.othello_ai, name='othello_ai'),
    path('othello/white/<int:room_id>/', views.othello_white, name='othello_white'),
    path('othello/black/<int:room_id>/', views.othello_black, name='othello_black'),
    path('tictactoe/', views.tictactoe, name='tictactoe'),
    path('tictactoe/ai/<int:room_id>/', views.tictactoe_ai, name='tictactoe_ai'),
    path('tictactoe/X/<int:room_id>/', views.tictactoe_x, name='tictactoe_X'),
    path('tictactoe/O/<int:room_id>/', views.tictactoe_o, name='tictactoe_O'),
    path('ganz-schon-clever/', views.ganz, name='ganz'),
]
