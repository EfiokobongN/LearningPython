from django.shortcuts import render
import random
import string

def home(request):
    lengths = [10, 15, 20, 25, 30, 35, 40]

    # Default context — no password shown on first load
    context = {
        'password': None,
        'selected_length': None,
        'lengths': lengths,
        'digits': True,
        'symbols': True,
        'uppercase': True,
        'lowercase': True,
    }

    if request.method == 'POST':
        selected_length = int(request.POST.get('length', 15))
        use_digits    = request.POST.get('digits')    == 'on'
        use_symbols   = request.POST.get('symbols')   == 'on'
        use_uppercase = request.POST.get('uppercase') == 'on'
        use_lowercase = request.POST.get('lowercase') == 'on'

        # Build character pool
        chart = []
        if use_digits:    chart += list(string.digits)
        if use_symbols:   chart += list(string.punctuation)
        if use_uppercase: chart += list(string.ascii_uppercase)
        if use_lowercase: chart += list(string.ascii_lowercase)

        # Fallback if nothing selected
        if not chart:
            chart = list(string.ascii_letters + string.digits)

        password = ''.join(random.choice(chart) for _ in range(selected_length))

        context.update({
            'password': password,
            'selected_length': selected_length,
            'digits': use_digits,
            'symbols': use_symbols,
            'uppercase': use_uppercase,
            'lowercase': use_lowercase,
        })

    return render(request, 'home.html', context)