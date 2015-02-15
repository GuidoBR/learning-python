# -*- coding: utf-8 -*-
from django.shortcuts import render
from driblando.app.api import Dribbble


def home(request):
    oAPI = Dribbble()
    pagina = request.GET.get('page', 1)
    shots = oAPI.getInformacoesShotPopulares(pagina)
    return render(request, "index.html", {'shots': shots, 'pagina': pagina})
