from django.shortcuts import render, redirect, get_object_or_404
from .models import User
from django.contrib import messages
from .models import JournalEntry
from datetime import datetime












def submit_journal(request):
    if request.method == 'POST':
        text = request.POST.get('journal_entry')
        image = request.FILES.get('journal_image')  # Handle uploaded image
        JournalEntry.objects.create(entry_text=text, entry_image=image)
        return redirect('success-page')  # Replace with your success URL
    return render(request, 'journal.html')
def home(request):
        user_id = request.session.get('user_id')
        if not user_id:
            return redirect('login')
        user = get_object_or_404(User, id=user_id)
        return render(request, 'home.html', {'user': user})

def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not User.objects.filter(username=username).exists():
            User.objects.create(
                username=username,
                password=password,

            )
            messages.success(request, "Registration successful!")
            return redirect('login')
        else:
            messages.error(request, "Username already exists!")

    return render(request, 'register.html')



def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.filter(username=username, password=password).first()
        if user:
            request.session['user_id'] = user.id  # Store user ID in session
            messages.success(request, f"Welcome, {user.username}!")
            return redirect('home')  # Redirect to home after login
        else:
            messages.error(request, "Invalid credentials")

    return render(request, 'login.html')

def journal(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        text = request.POST.get('journal_entry')
        image = request.FILES.get('journal_image')
        JournalEntry.objects.create(title=title, entry_text=text, entry_image=image)
        return redirect('archives')  # Redirect to the archives page after submission
    return render(request, 'journal.html', {'title': 'Journal'})
def archives(request):
    entries = JournalEntry.objects.order_by('-created_at')  # Show newest entries first
    return render(request, 'archives.html', {'entries': entries, 'title': 'Archives'})


# chatbot/views.py

def quote_view(request):
    # List of mental health quotes
    quotes = [
        "Happiness is not out there, it's in you. - Unknown",
        "Mental health is not a destination, but a process. - Noam Shpancer",
        "Your present circumstances don’t determine where you can go. - Nido Qubein",
        "You don’t have to control your thoughts. - Dan Millman",
        "Recovery is hard. Regret is harder. - Brittany Burgunder",
        "Self-care is not a luxury, it’s a necessity. - Audre Lorde",
        "Mental health needs a great deal of attention. - Adam Ant",
        "Your mental health is a priority. - Unknown",
        "It’s okay to not be okay. - Unknown",
        "Happiness can be found even in the darkest of times. - Albus Dumbledore",
        "The only journey is the one within. - Rainer Maria Rilke",
        "Healing takes time, and asking for help is a courageous step. - Mariska Hargitay",
        "There is hope, even when your brain tells you there isn’t. - John Green",
        "Be patient with yourself. - Unknown",
        "You are not your illness. - Julian Seifter",
        "What mental health needs is more sunlight, more candor, and more unashamed conversation. - Glenn Close",
        "No matter how hard the past is, you can always begin again. - Buddha",
        "Out of difficulties grow miracles. - Jean de La Bruyere",
        "Embrace uncertainty. - Unknown",
        "Rest and self-care are so important. - Kris Carr",
    ]

    # Use the day of the year to pick a quote
    today = datetime.now()
    day_of_year = today.timetuple().tm_yday
    daily_quote = quotes[day_of_year % len(quotes)]  # Rotate quotes based on day

    return render(request, 'quote.html', {'quote': daily_quote})







from transformers import BlenderbotTokenizer, BlenderbotForConditionalGeneration
from django.http import JsonResponse
from django.shortcuts import render
import json

# Load the pre-trained BlenderBot model and tokenizer
model_name = "facebook/blenderbot-400M-distill"
tokenizer = BlenderbotTokenizer.from_pretrained(model_name)
model = BlenderbotForConditionalGeneration.from_pretrained(model_name)

def chatbot(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user_message = data.get("message", "")

        if not user_message.strip():
            return JsonResponse({"reply": "Please say something!"})

        try:
            # Generate a response
            inputs = tokenizer(user_message, return_tensors="pt")
            reply_ids = model.generate(inputs["input_ids"], max_length=100)
            bot_reply = tokenizer.decode(reply_ids[0], skip_special_tokens=True)

            return JsonResponse({"reply": bot_reply})

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    # Render chatbot UI
    return render(request, 'chatbot.html')




def nami_home(request):


    return render(request, "resources.html",)



from .models import AnxietyTestResponse



from .models import AnxietyTestResponse


def submit_test(request):
    if request.method == "POST":
        response = AnxietyTestResponse(
            q1=int(request.POST.get('q1')),
            q2=int(request.POST.get('q2')),
            q3=int(request.POST.get('q3')),
            q4=int(request.POST.get('q4')),
            q5=int(request.POST.get('q5')),
            q6=int(request.POST.get('q6')),
            q7=int(request.POST.get('q7')),
            q8=int(request.POST.get('q8')),
            q9=int(request.POST.get('q9')),
            q10=int(request.POST.get('q10')),
        )
        response.save()
        response.calculate_score_and_level()
        # Store response ID in session for redirection
        request.session['last_response_id'] = response.id
        return redirect('results')

    return render(request, 'anxiety_test.html')

def results(request):
    # Get response ID from session and validate
    response_id = request.session.get('last_response_id')
    if not response_id:
        return redirect('anxiety_test')  # Redirect to test page if no response ID
    response = get_object_or_404(AnxietyTestResponse, id=response_id)
    return render(request, 'results.html', {
        'total_score': response.total_score,
        'anxiety_level': response.anxiety_level
    })







