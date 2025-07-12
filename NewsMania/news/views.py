from django.shortcuts import render, get_object_or_404 , redirect
from .models import News, Category
from django.db.models import Q



# Homepage view
def home(request):
    query = request.GET.get('q')
    if query:
        all_news = News.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        ).order_by('-date')
    else:
        all_news = News.objects.all().order_by('-date')
    
    return render(request, 'news/home.html', {'all_news': all_news, 'query': query})

# Detail view (fix for your error)
def news_detail(request, news_id):
    news = get_object_or_404(News, id=news_id)
    return render(request, 'news/news_detail.html', {'news': news})


def filter_by_category(request, category_id):
    selected_category = get_object_or_404(Category, id=category_id)
    news_in_category = News.objects.filter(category=selected_category).order_by('-date')
    all_categories = Category.objects.all()
    return render(request, 'news/category_filter.html', {
        'category': selected_category,
        'news_list': news_in_category,
        'all_categories': all_categories
    })

from django.contrib.auth.decorators import login_required
from .forms import NewsForm

@login_required
def upload_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            news = form.save(commit=False)
            news.author = request.user  # ✅ Set the logged-in user
            news.save()
            return redirect('home')
    else:
        form = NewsForm()
    return render(request, 'news/upload_news.html', {'form': form})
