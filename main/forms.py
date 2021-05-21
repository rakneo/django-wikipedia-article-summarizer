from django.forms import Form, URLField, ChoiceField


class SummarizerForm(Form):
    SUMMARIZER_TYPE_CHOICES = (
        ('random', 'Random'),
        ('luhn', 'Luhn'),
        ('lsa', 'Latent Semantic Analysis'),
        # ('edmundson', 'Edmundson'),
        ('lexrank', 'LexRank'),
        ('textrank', 'TextRank'),
        ('sumbasic', 'SumBasic'),
        ('kl', 'KL-SUM')

    )
    wikipedia_url = URLField(max_length=5000, required=True, label="Wikipedia URL")
    summarizer_type = ChoiceField(choices=SUMMARIZER_TYPE_CHOICES, required=True, label="Summarizer Type")
