from django.views import View
from django.http.response import HttpResponse
from django.shortcuts import render
from collections import deque


# line_of_cars = deque()
for_change_oil_line = deque()
for_inflate_tires_line = deque()
for_diagnostic_line = deque()
next_number = 1


def get_estimated_time(service):
    # n_change_oil = 0
    # n_inflate_tires = 0
    # n_diagnostic = 0
    # for car in line_of_cars:
    #     if 'oil' in car:
    #         n_change_oil += 1
    #     elif 'tires' in car:
    #         n_inflate_tires += 1
    #     elif 'diagnostic' in car:
    #         n_diagnostic += 1

    minutes = 0
    minutes += len(for_change_oil_line) * 2
    if service == 'change_oil':
        return minutes
    minutes += len(for_inflate_tires_line) * 5
    if service == 'inflate_tires':
        return minutes
    minutes += len(for_diagnostic_line) * 30
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
        global for_change_oil_line
        minutes = get_estimated_time('change_oil')
        number = next_number
        next_number += 1
        for_change_oil_line.append(number)
        return render(request, 'your_ticket.html', context={'number': number, 'minutes': minutes})


class InflateTiresTicketView(View):
    def get(self, request, *args, **kwargs):
        global next_number
        global for_inflate_tires_line
        minutes = get_estimated_time('inflate_tires')
        number = next_number
        next_number += 1
        for_inflate_tires_line.append(number)
        return render(request, 'your_ticket.html', context={'number': number, 'minutes': minutes})


class DiagnosticTicketView(View):
    def get(self, request, *args, **kwargs):
        global next_number
        global for_diagnostic_line
        minutes = get_estimated_time('diagnostic')
        number = next_number
        next_number += 1
        for_diagnostic_line.append(number)
        return render(request, 'your_ticket.html', context={'number': number, 'minutes': minutes})


class ProcessingView(View):
    def get(self, request, *args, **kwargs):
        global for_change_oil_line
        global for_inflate_tires_line
        global for_diagnostic_line
        return render(request,
                      'processing.html',
                      context={
                          'n_change_oil': len(for_change_oil_line),
                          'n_inflate_tires': len(for_inflate_tires_line),
                          'n_diagnostic': len(for_diagnostic_line)
                      }
                      )
