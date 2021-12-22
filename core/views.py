from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request, nome, idade):
    return HttpResponse(f'<h1>Hello {nome} {idade} anos</h1>')

def soma(request, soma1,  soma2):
    return HttpResponse(f'<h2>{soma1} + {soma2} = {soma1 + soma2} </h2>')

def subtracao(request, sub1, sub2):
    return HttpResponse(f'<h2>{sub1} - {sub2} = {sub1 - sub2}</h2>')

def multiplicacao(request, mult1, mult2):
    return  HttpResponse(f'<h2>{mult1} * {mult2} = {mult1 * mult2} </h2>')

def divisao(request, div1, div2):
    return HttpResponse(f'<h2>{div1} / {div2} = {div1 / div2}')