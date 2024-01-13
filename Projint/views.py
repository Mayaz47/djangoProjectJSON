import urllib

import seaborn as sns
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import json
import pandas as pd
import matplotlib
from matplotlib import pyplot as plt
from io import BytesIO
import base64

from sklearn.preprocessing import PowerTransformer

from Projint.models import MyData


def chart(request):
    data = MyData.objects.all()
    queryset = MyData.objects.all()


    df = pd.DataFrame.from_records(queryset.values())

    df['close'] = pd.to_numeric(df['close'], errors='coerce')
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    df['volume'] = pd.to_numeric(df['volume'], errors='coerce')
    df['open'] = pd.to_numeric(df['open'], errors='coerce')

    fig, ax1 = plt.subplots()


    ax1.plot(df['date'], df['close'], marker='o', linestyle='-', color='blue', label='Close')
    ax1.set_xlabel('Date')
    ax1.set_ylabel('Close', color='blue')
    ax1.tick_params('y', colors='blue')


    ax2 = ax1.twinx()
    ax2.bar(df['date'], df['volume'], alpha=0.5, color='green', label='Volume')
    ax2.set_ylabel('Volume', color='green')
    ax2.tick_params('y', colors='green')


    fig.legend(loc='upper left')

    fig2, ax3 = plt.subplots()


    ax3.plot(df['trade_code'], df['close'], marker='o', linestyle='-', color='blue', label='Close')
    ax3.set_xlabel('Trade Code')
    ax3.set_ylabel('Close', color='blue')
    ax3.tick_params('y', colors='blue')


    ax4 = ax3.twinx()
    ax4.bar(df['trade_code'], df['volume'], alpha=0.5, color='green', label='Volume')
    ax4.set_ylabel('Volume', color='green')
    ax4.tick_params('y', colors='green')

    plt2, ax = plt.subplots(figsize=(10, 6))


    sns.scatterplot(x='volume', y='close', data=df, hue='date', ax=ax)
    ax.set_title('Relation Plot between Close and Volume by date')

    plt3, ax1 = plt.subplots(figsize=(10, 6))


    scaler = PowerTransformer(method='yeo-johnson')


    df['normalized_close'] = scaler.fit_transform(df[['close']])
    df['normalized_volume'] = scaler.fit_transform(df[['volume']])
    sns.boxplot(x='normalized_close', y='date', ax=ax1, data=df)
    ax1.set_title('Normalize Boxplot')

    plt4, ax2 = plt.subplots(figsize=(10, 6))
    df['normalized_open'] = scaler.fit_transform(df[['open']])
    sns.regplot(x='normalized_close', y='normalized_open', data=df, ax=ax2)
    ax2.set_title('Regression between Open and Close')

    buffer = BytesIO()
    fig.savefig(buffer, format='png')
    buffer.seek(0)
    img_data = base64.b64encode(buffer.read()).decode('utf-8')
    buffer.close()

    buffer = BytesIO()
    fig2.savefig(buffer, format='png')
    buffer.seek(0)
    img_data2 = base64.b64encode(buffer.read()).decode('utf-8')
    buffer.close()

    buffer = BytesIO()
    plt2.savefig(buffer, format='png')
    buffer.seek(0)
    img_data3 = base64.b64encode(buffer.read()).decode('utf-8')
    buffer.close()

    buffer = BytesIO()
    plt3.savefig(buffer, format='png')
    buffer.seek(0)
    img_data4 = base64.b64encode(buffer.read()).decode('utf-8')
    buffer.close()

    buffer = BytesIO()
    plt4.savefig(buffer, format='png')
    buffer.seek(0)
    img_data5 = base64.b64encode(buffer.read()).decode('utf-8')
    buffer.close()


    return render(request, 'index.html', {'img1': img_data, 'img2': img_data2,'img3': img_data3,'img4': img_data4,'img5': img_data5,'data': data })

def index2(request):
    if request.method == 'POST':
        # Get data from the form submission
        date = request.POST['addDate']
        trade_code = request.POST['addTradeCode']
        high = request.POST['high']
        low = request.POST['low']
        open_value = request.POST['open']
        close = request.POST['close']
        volume = request.POST['volume']


        new_data = MyData(
            date=date,
            trade_code=trade_code,
            high=high,
            low=low,
            open=open_value,
            close=close,
            volume=volume
        )

        # Save the new data to the database
        new_data.save()

        # Redirect to the display_data view after adding data
        return HttpResponse("Success")

    else:

        return render(request, 'index2.html')

def delete(request):
    if request.method == 'POST':

        date = request.POST['deleteDate']
        trade_code = request.POST['deleteTradeCode']
        matching_data = MyData.objects.filter(date=date, trade_code=trade_code)
        try:
            # Try to get the record with the specified Date and Trade Code

            data_to_delete = matching_data.first()
            data_to_delete.delete()
            return HttpResponse("Data deleted successfully.")
        except MyData.DoesNotExist:
            return HttpResponse("Data not found.")

    else:
        # If the form is not submitted using POST, return a default response
        return render(request, 'delete.html')
def update(request):
    if request.method == 'POST':

        date = request.POST['upDate']
        trade_code = request.POST['upTradeCode']
        matching_data = MyData.objects.filter(date=date, trade_code=trade_code)
        try:
            # Try to get the record with the specified Date and Trade Code

            data_to_update = matching_data.first()
            # Update the fields based on the form input
            data_to_update.high = request.POST.get('upHigh', data_to_update.high)
            data_to_update.low = request.POST.get('upLow', data_to_update.low)
            data_to_update.open = request.POST.get('upOpen', data_to_update.open)
            data_to_update.close = request.POST.get('upClose', data_to_update.close)
            data_to_update.volume = request.POST.get('upVolume', data_to_update.volume)

            # Save the updated data
            data_to_update.save()

            return HttpResponse("Data updated successfully.")
        except MyData.DoesNotExist:
            return HttpResponse("Data not found.")

    else:
        # If the form is not submitted using POST, return a default response
        return render(request, 'update.html')





