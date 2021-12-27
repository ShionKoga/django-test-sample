from django.shortcuts import render

def buy_meats(request):
    context = {
        'meats': ['beaf', 'pork', 'chicken']
    }
    return render(request, 'meats.html', context)
