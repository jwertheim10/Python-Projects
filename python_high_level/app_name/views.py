from django.urls import path
from django.shortcuts import HttpResponse, render
from . import urls

def index(request):
    return HttpResponse("Hello, world")

def add(request, num1, num2):
    sum = num1 + num2
    return HttpResponse(f"The sum of {num1} and {num2} is {sum}.")

def operation(request):
    action = request.GET.get('action')  # For str: action
    num1 = int(request.GET.get('num1'))  # For int: num1
    num2 = int(request.GET.get('num2'))  # For int: num2
    result = 0
    if action == 'add':
        result = num1 + num2
    elif action == 'sub':
        result = num1 - num2
    elif action == 'mult':
        result = num1 * num2
    elif action == 'div':
        result = num1 / num2
    else:
        result = 'operator not found, please use one of: add, sub, mult, or div'
    return HttpResponse(f"The result of {action}ing {num1} and {num2} is {result}.")

def sum_multiples(request):
    num1 = int(request.GET.get('num1'))  # For int: num1
    num2 = int(request.GET.get('num2'))  # For int: num2
    if num1 > num2:
        return HttpResponse('Your second number must be greater than or equal to your first number')
    result = 0
    i = num1
    while i <= num2:
        result += i
        i += num1
    return HttpResponse(f"The sum of all multiples of {num1} below {num2} is {result}")