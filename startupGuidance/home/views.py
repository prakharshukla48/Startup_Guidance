from django.shortcuts import render
from django.http import HttpResponseRedirect

# from .form import PredictForm
from .prediction import Prediction
from .willusetfidf import Uniqueness

def home_page(request):
    return render(request, 'home/index.html', {})

def join_us(request):
    return render(request, 'home/join_us.html', {})

def to_predict(request):
    return render(request, 'home/to_predict.html', {})

def predict(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        print("\n\n\nIs a valid post request")
        print(request.POST.items())
        sector = request.POST['sector']
        sub_vertical = request.POST['sub_vertical']
        funding = request.POST['funding']
        print(sector+" "+sub_vertical+" "+funding)
        predicted_value = Prediction(sector, sub_vertical, funding)
        print("\n\n\npredicted value is")
        print(predicted_value)
        # create a form instance and populate it with data from the request:
        # form = PredictForm(request.POST)
        # check whether it's valid:
#        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
#            return render(request, 'home/predict.html', {})
#            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
        # form = PredictForm()

        return render(request, 'home/predict.html', {'value':predicted_value})
    else:
        return render(request, 'home/to_predict.html', {})

def find_unique(request):
    if request.method == 'POST':
        idea = request.POST['idea']
        print(idea)
        unique = Uniqueness(idea)
        print(unique)
        return render(request, 'home/predict.html', {'value':unique})
    else:
        return render(request, 'home/unique.html', {})
