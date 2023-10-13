from django.shortcuts import render, redirect
from .models import Keyword, Trend
from .forms import KeywordForm, TrendForm
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from matplotlib import pyplot as plt
from io import BytesIO
import base64


# Create your views here.

def keyword(request):
    keywords = Keyword.objects.all()
    if request.method == 'POST':
        form = KeywordForm(request.POST)
        form.save()
        return redirect('trends:keyword')
    else:
        form = KeywordForm()
    context = {
        'form': form,
        'keywords': keywords,
    }
    return render(request, 'trends/keyword.html', context)

def keyword_detail(request, pk):
    keyword = Keyword.objects.get(pk=pk)
    keyword.delete()
    return redirect('trends:keyword')

def crawling(request):
    keywords = Keyword.objects.values_list('name', flat=True)
    trends = Trend.objects.all()
    trends_name = Trend.objects.values_list('name',flat=True)
    
    driver = webdriver.Chrome()
    for keyword in keywords:
        url = f'https://www.google.com/search?q={keyword}'
        driver.get(url)
        html = driver.page_source
        soup = bs(html, "html.parser")
        result_stats = soup.select_one("div#result-stats")
        result = int(result_stats.text.split()[2].replace(',', '').rstrip('개'))
        tmp = Trend()
        if keyword not in trends_name:
            tmp.name = keyword
            tmp.result = result
            tmp.search_period = "all"
            tmp.save()
    period_all = Trend.objects.filter(search_period = 'all')
    plt.clf()
    plt.grid(True)
    trends_names = period_all.values_list('name',flat=True)
    trends_results = period_all.values_list('name',flat=True)
    plt.figure()
    plt.hist(trends_names, trends_results)
    plt.title('Technology Trend Analysis')
    plt.xlabel('Keyword')
    plt.xticks(rotation=0)
    plt.ylabel('Result')
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n','')
    buffer.close()
    context = {
        'keywords': keywords,
        'trends': trends,
        'chart_image': f'data:image/png;base64,{image_base64}',
    }
    return render(request, 'trends/crawling.html', context)

def crawling_histogram(request):
    return render(request, 'trends/crawling_histogram.html')

def crawling_advanced(request):
    return render(request, 'trends/crawling_advanced.html')