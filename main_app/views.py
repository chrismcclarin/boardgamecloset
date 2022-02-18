from django.shortcuts import render, redirect
from .models import Games, SaleLocation
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import GameTimeForm

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def games_index(request):
    games = Games.objects.all()
    return render(request, 'games/index.html', {'games': games})

def games_detail(request, game_id):
    game = Games.objects.get(id=game_id)
    gametimeform = GameTimeForm()
    where_a_sale_is = SaleLocation.objects.exclude(id__in = game.sale.all().values_list('id'))
    return render(request, 'games/detail.html', {
        'games': game,
        'gametimeform':gametimeform,
        'sales': where_a_sale_is,
        })

class GameCreate(CreateView):
    model = Games
    fields = ('name', 'genre', 'preferredplayers', 'timetoplay', 'description')

class GameUpdate(UpdateView):
    model = Games
    fields = ('preferredplayers', 'timetoplay', 'description')

class GameDelete(DeleteView):
    model = Games
    success_url='/games/'

def new_gametime(request, game_id):
    form = GameTimeForm(request.POST)
    if form.is_valid():
        new_gametime = form.save(commit=False)
        new_gametime.game_id=game_id
        new_gametime.save()
    return redirect('detail', game_id=game_id)

def sale_index(request):
    sales = SaleLocation.objects.all()
    return render(request, 'salelocation/index.html', {'sales': sales})

def sale_detail(request, sale_id):
    sale = SaleLocation.objects.get(id=sale_id)
    return render(request, 'salelocation/detail.html', {'sale': sale})

class SaleCreate(CreateView):
    model = SaleLocation
    fields = '__all__'

class SaleUpdate(UpdateView):
    model = SaleLocation
    fields = '__all__'

class SaleDelete(DeleteView):
    model = SaleLocation
    success_url='/'

def assoc_sale(request, game_id, sale_id):
    Games.objects.get(id=game_id).sale.add(sale_id)
    return redirect('detail', game_id=game_id)

def rm_assoc_sale(request, game_id, sale_id):
    Games.objects.get(id=game_id).sale.remove(sale_id)
    return redirect('detail', game_id=game_id)

