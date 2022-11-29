from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.template import loader
from django.urls import reverse
from time import sleep
from .models import GameTicTacToe, GameOthello, GamesList

tictactoe_models = [GameTicTacToe(i) for i in range(7)]
othello_models = [GameOthello(i) for i in range(16)]


def main_page(request):
    list_of_game = GamesList.objects.order_by("-create_date")
    context = {"games": list_of_game}
    return render(request, "games/main.html", context=context)


def othello(request):
    return render(request, "games/othello/othello_main.html")


def othello_ai(request, room_id):
    if 8 <= room_id < 12:
        return HttpResponse("Not yet implemented!")

    model = othello_models[room_id]
    if model.ai:
        if room_id < 4:
            model.play_ai_greedy()
        else:
            model.play_ai_minimax()
        return render(request, "games/othello/othello_player.html", context={"model": model})
    else:
        if request.method == "POST":
            z = int(request.POST.get("action"))
            print(z)
            if z == -1:
                model.back()
            elif z == -2:
                model.initialize()
            else:
                model.update(z)
        return render(request, "games/othello/othello_ai.html", context={"model": model})


def othello_white(request, room_id):
    model = othello_models[room_id]
    if model.board.turn == 64:
        if request.method == "POST":
            z = int(request.POST.get("action"))
            print(z)
            if z == -1:
                model.back()
            elif z == -2:
                model.initialize()
            else:
                model.update(z)
            return render(request, "games/othello/othello_waiting.html", context={"model": model})
        else:
            return render(request, "games/othello/othello.html", context={"model": model})
    else:
        return render(request, "games/othello/othello_waiting.html", context={"model": model})


def othello_black(request, room_id):
    model = othello_models[room_id]
    if model.board.turn == 65:
        if request.method == "POST":
            z = int(request.POST.get("action"))
            print(z)
            if z == -1:
                model.back()
            elif z == -2:
                model.initialize()
            else:
                model.update(z)
            return render(request, "games/othello/othello_waiting.html", context={"model": model})
        else:
            return render(request, "games/othello/othello.html", context={"model": model})
    else:
        return render(request, "games/othello/othello_waiting.html", context={"model": model})


def tictactoe(request):
    return render(request, "games/tic-tac-toe/tic-tac-toe_main.html")


def tictactoe_ai(request, room_id):
    model = tictactoe_models[room_id]
    if model.ai:
        if room_id < 2:
            model.play_ai_dumb()
        else:
            model.play_ai_minimax()
        return render(request, "games/tic-tac-toe/tic-tac-toe_player.html", context={"model": model})
    else:
        if request.method == "POST":
            z = int(request.POST.get("action"))
            print(z)
            if z == -2:
                model.initialize()
            else:
                model.update(z)
        return render(request, "games/tic-tac-toe/tic-tac-toe_ai.html", context={"model": model})


def tictactoe_x(request, room_id):
    model = tictactoe_models[room_id]
    if model.turn == 'X':
        if request.method == "POST":
            z = int(request.POST.get("action"))
            print(z)
            if z == -2:
                model.initialize()
            else:
                model.update(z)
            return render(request, "games/tic-tac-toe/tic-tac-toe_waiting.html", context={"model": model})
        else:
            return render(request, "games/tic-tac-toe/tic-tac-toe.html", context={"model": model})
    else:
        return render(request, "games/tic-tac-toe/tic-tac-toe_waiting.html", context={"model": model})


def tictactoe_o(request, room_id):
    model = tictactoe_models[room_id]
    if model.turn == 'O':
        if request.method == "POST":
            z = int(request.POST.get("action"))
            print(z)
            if z == -2:
                model.initialize()
            else:
                model.update(z)
            return render(request, "games/tic-tac-toe/tic-tac-toe_waiting.html", context={"model": model})
        else:
            return render(request, "games/tic-tac-toe/tic-tac-toe.html", context={"model": model})
    else:
        return render(request, "games/tic-tac-toe/tic-tac-toe_waiting.html", context={"model": model})


def ganz(request):
    return render(request, "games/ganz-schon-clever/ganz-schon-clever.html")
