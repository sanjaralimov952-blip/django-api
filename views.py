from django.shortcuts import render, redirect
from .models import Movie, Category
from .forms import MovieForm


# GET (фильтрация + query params)
def movie_list(request):
    movies = Movie.objects.all()
    
    category = request.GET.get('category')
    year = request.GET.get('year')

    if category:
        movies = movies.filter(category__name=category)

    if year:
        movies = movies.filter(year=year)

    categories = Category.objects.all()

    return render(request, 'movie_list.html', {
        'movies': movies,
        'categories': categories
    })


# POST (создание фильма)
def create_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('movie_list')
    else:
        form = MovieForm()

    return render(request, 'create_movie.html', {'form': form})