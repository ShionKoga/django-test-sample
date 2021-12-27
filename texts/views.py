from django.shortcuts import render

def write_alphabets(request):
    context = {
        'alphabets': ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    }
    return render(request, 'alphabets.html', context)
