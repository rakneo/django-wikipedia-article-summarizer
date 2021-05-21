from django.shortcuts import render
from .forms import SummarizerForm
from .summarizer import TextSummarizer
# Create your views here.


def home(request):
    form = SummarizerForm()
    if request.method == "POST":
        form = SummarizerForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['wikipedia_url']
            summarizer_type = form.cleaned_data['summarizer_type']
            summarizer = TextSummarizer(url, summarizer_type)
            summary = summarizer.get_summary()
            return render(request, 'home.html', {'form': form, 'is_result': True, 'result': summary})
    return render(request, 'home.html', {'form': form})
