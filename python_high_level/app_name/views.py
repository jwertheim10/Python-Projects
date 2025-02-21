from django.shortcuts import HttpResponse, render
from . import sum_multiple_extracted

# This function returns hello world on the webpage
def index(request): 
    return HttpResponse("Hello, world")

# This function adds two numbers that are passed into the url
def add(request, num1, num2):
    sum = num1 + num2
    return HttpResponse(f"The sum of {num1} and {num2} is {sum}.")

# This function takes a string and depending on the string applies one of +-*/ to the two numbers
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

# Here we get the two numbers passed into the url and pass it onto a helped method
def sum_multiples(request): 
    num1 = int(request.GET.get('num1'))  # For int: num1
    num2 = int(request.GET.get('num2'))  # For int: num2
    return HttpResponse(sum_multiple_extracted.main(num1, num2))
