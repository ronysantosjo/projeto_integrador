from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from .models import Amostra

def index(request):
    amostras = Amostra.objects.all()

    context = { 'amostras': amostras }

    if 'edit_id' in request.GET:
        context = { **context, 'message': 'edit', 'message_id': request.GET['edit_id'] }
    
    if 'delete_id' in request.GET:
        context = { **context, 'message': 'delete', 'message_id': request.GET['delete_id'] }

    template = loader.get_template('amostras/index.html')
    return HttpResponse(template.render(context, request))


def create_new(request):

    if request.method == 'POST':
        amostra = Amostra(
            data_recebimento=request.POST['data_recebimento'],
            nome_amostra=request.POST['nome_amostra'],
            data_liberacao=request.POST['data_liberacao'],
            exame_direto=request.POST['exame_direto'],
            metodo_sheaters=request.POST['metodo_sheaters']
        )
        amostra.save()
        return HttpResponseRedirect(reverse('amostras_index') + '?edit_id=' + str(amostra.id))

    context = {}
    template = loader.get_template('amostras/create.html')
    return HttpResponse(template.render(context, request))


def view(request, amostra_id=None):
    amostra = Amostra.objects.filter(id=amostra_id).first()
    context = { 'amostra': amostra }
    template = loader.get_template('amostras/view.html')
    return HttpResponse(template.render(context, request))


def edit(request, amostra_id=None):
    amostra = Amostra.objects.filter(id=amostra_id).first()

    if request.method == 'POST':
        amostra.data_recebimento=request.POST['data_recebimento']
        amostra.nome_amostra=request.POST['nome_amostra']
        amostra.data_liberacao=request.POST['data_liberacao']
        amostra.exame_direto=request.POST['exame_direto']
        amostra.metodo_sheaters=request.POST['metodo_sheaters']
        amostra.save()
        return HttpResponseRedirect(reverse('amostras_index') + '?edit_id=' + str(amostra.id))

    context = { 'amostra': amostra }
    template = loader.get_template('amostras/edit.html')
    return HttpResponse(template.render(context, request))


def delete(request, amostra_id=None):
    amostra = Amostra.objects.filter(id=amostra_id).first()

    if request.method == 'POST':
        amostra = Amostra.objects.filter(id=amostra_id).delete()
        return HttpResponseRedirect(reverse('amostras_index') + '?delete_id=' + str(amostra_id))

    context = { 'amostra': amostra }
    template = loader.get_template('amostras/delete.html')
    return HttpResponse(template.render(context, request))