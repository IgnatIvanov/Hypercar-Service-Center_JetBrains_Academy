from django.views import View
from django.http.response import HttpResponse
from django.shortcuts import render
from collections import deque


line_of_cars = deque()
next_number = 1


def GetEstimatedTime(service):
    n_change_oil = 0
    n_inflate_tires = 0
    n_diagnostic = 0
    for car in line_of_cars:
        if 'oil' in car:
            n_change_oil += 1
        elif 'tires' in car:
            n_inflate_tires += 1
        elif 'diagnostic' in car:
            n_diagnostic += 1

    minutes = 0
    minutes += n_change_oil * 2
    if service == 'change_oil':
        return minutes
    minutes += n_inflate_tires * 5
    if service == 'inflate_tires':
        return minutes
    minutes += n_diagnostic * 30
    return minutes


class WelcomeView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('<h2>Welcome to the Hypercar Service!</h2>')


class MenuView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'menu.html')


class ChangeOilTicketView(View):
    def get(self, request, *args, **kwargs):
        global next_number
        global line_of_cars
        minutes = GetEstimatedTime('change_oil')
        number = next_number
        next_number += 1
        line_of_cars.append('change_oil')
        return render(request, 'your_ticket.html', context={'number': number, 'minutes': minutes})


class InflateTiresTicketView(View):
    def get(self, request, *args, **kwargs):
        global next_number
        global line_of_cars
        minutes = GetEstimatedTime('inflate_tires')
        number = next_number
        next_number += 1
        line_of_cars.append('inflate_tires')
        return render(request, 'your_ticket.html', context={'number': number, 'minutes': minutes})


class DiagnosticTicketView(View):
    def get(self, request, *args, **kwargs):
        global next_number
        global line_of_cars
        minutes = GetEstimatedTime('diagnostic')
        number = next_number
        next_number += 1
        line_of_cars.append('diagnostic')
        return render(request, 'your_ticket.html', context={'number': number, 'minutes': minutes})