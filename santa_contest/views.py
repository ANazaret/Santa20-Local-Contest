import multiprocessing
import uuid

from django.core.management import call_command
from django.shortcuts import render, redirect


def index(request):
    return render(request, 'index.html')


def run_games(request, num_games):
    uid = uuid.uuid4().hex[:16]
    process = multiprocessing.Process(target=call_command, args=("run_games",),
                                      kwargs={"num_games": num_games, "trigger": uid})
    process.start()
    return redirect("/admin/app/game/?trigger=%s" % uid)
