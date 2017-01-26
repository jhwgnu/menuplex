from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from board.models import School, Meal
from django.http import HttpResponse

def index(request):
    school_list = School.objects.all()
    context = {'school_list': school_list}
    return render(request, 'board/index.html', context)


def detail(request, school_short):
    school = get_object_or_404(School, pk=school_short)
    school_list = School.objects.all()
    context = {'school_list': school_list}
    return render(request, 'board/detail.html', context)
