from django.shortcuts import render, redirect
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
# 입출력 연산을 위한 Python 표준 라이브러리
from io import BytesIO
# 텍스트 <-> 이진 데이터 변환
import base64


# Create your views here.
matplotlib.use('Agg')
df = pd.read_csv('data/austin_weather.csv')
df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.month
df['Year'] = df['Date'].dt.year
df2 = df.groupby(['Year','Month'])
df2 = df2[['TempHighF', 'TempAvgF', 'TempLowF']].mean()
df2.index = df2.index.map(lambda x: f"{x[0]}-{x[1]:02d}")
df2.index = pd.to_datetime(df2.index, format='%Y-%m')


def problem1(request):
    context = {
        'df': df,
    }
    return render(request, 'weathers/problem1.html', context)

def problem2(request):
    plt.clf()
    plt.grid(True)
    plt.plot(df['Date'], df['TempHighF'], label='High Temperature')
    plt.plot(df['Date'], df['TempAvgF'], label='Average Temperature')
    plt.plot(df['Date'], df['TempLowF'], label='Low Temperature')
    plt.title('Temperature Variation')
    plt.xlabel('Date')
    plt.ylabel('Temperature(Fahrenheit)')
    plt.legend(loc = 'lower center')
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n','')

    buffer.close()
    context = {
        'chart_image': f'data:image/png;base64,{image_base64}',
    }
    return render(request, 'weathers/problem2.html', context)

def problem3(request):
    plt.clf()
    plt.grid(True)
    plt.plot(df2.index, df2['TempHighF'], label='High Temperature')
    plt.plot(df2.index, df2['TempAvgF'], label='Average Temperature')
    plt.plot(df2.index, df2['TempLowF'], label='Low Temperature')
    plt.title('Temperature Variation')
    plt.xlabel('Date')
    plt.ylabel('Temperature(Fahrenheit)')
    plt.legend(loc = 'lower right')
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n','')

    buffer.close()
    context = {
        'chart_image': f'data:image/png;base64,{image_base64}',
    }
    return render(request, 'weathers/problem3.html', context)

def problem4(request):
    event_counts = df['Events'].str.split(',').explode().str.strip()
    event_counts = event_counts.replace('', 'No events')
    event_counts = event_counts.value_counts()
    plt.clf()
    event_counts.plot(kind='bar', width=0.8)
    plt.grid(True)
    plt.title('Event Counts')
    plt.xlabel('Events')
    plt.xticks(rotation=0)
    plt.ylabel('Count')
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n','')
    buffer.close()
    context = {
        'chart_image': f'data:image/png;base64,{image_base64}',
    }
    return render(request, 'weathers/problem4.html', context)
    
