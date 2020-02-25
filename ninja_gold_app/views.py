from django.shortcuts import render, HttpResponse, redirect
import random
from datetime import datetime

# Create your views here.

now = datetime.now()


def index(request):
    if "total_gold" not in request.session or "activities" not in request.session:
        request.session["total_gold"] = 0
        request.session["activities"] = []
    return render(request, "index.html")


def process_money(request):
    if request.method == "POST":
        if request.POST["processing"] == "farm":
            gold = random.randint(10, 21)
            request.session["activities"].append(
                "You've earned ✨ "
                + str(gold)
                + " golds from the "
                + request.POST["processing"]
                + " 🌽🍇"
                + "("
                + str(now.strftime("%Y-%m-%d %H:%M %P"))
                + ")"
            )

        elif request.POST["processing"] == "cave":
            gold = random.randint(5, 11)
            request.session["activities"].append(
                "You've earned ✨ "
                + str(gold)
                + " golds from the "
                + request.POST["processing"]
                + " 🗿"
                + "("
                + str(now.strftime("%Y-%m-%d %H:%M %P"))
                + ")"
            )

        elif request.POST["processing"] == "house":
            gold = random.randint(2, 6)
            request.session["activities"].append(
                "You've earned ✨ "
                + str(gold)
                + " golds from the "
                + request.POST["processing"]
                + " 🏠"
                + "("
                + str(now.strftime("%Y-%m-%d %H:%M %P"))
                + ")"
            )

        elif request.POST["processing"] == "casino":
            gold = random.randint(-50, 51)
            if gold >= 0:
                request.session["activities"].append(
                    "Entered 🎰 casino and earned ✨ "
                    + str(gold)
                    + " gold"
                    + " "
                    + "("
                    + str(now.strftime("%Y-%m-%d %H:%M %P"))
                    + ")"
                )
            else:
                request.session["activities"].append(
                    "Entered 🎰 casino and lost 😩"
                    + str(gold)
                    + " gold..... Ouch!..."
                    + " "
                    + "("
                    + str(now.strftime("%Y-%m-%d %H:%M %P"))
                    + ")"
                )
        print(request.POST)
        request.session["total_gold"] += gold

    return redirect("/")


def reset(request):
    if request.method == "POST":
        request.session["total_gold"] = 0
        request.session["activities"] = []
    return redirect("/")
