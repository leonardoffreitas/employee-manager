from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from employee.models import Employee
import json

@csrf_exempt
def api_employee(*params):
    '''Main method to use api CRUD'''
    response = API_REQUESTS[params[0].method](*params)
    return response

def list_employees(*params):
    '''Method to get list woth all employes and the self spec'''
    request   = params[0]
    e_id      = params[1]
    query_set = None
    if len(e_id) > 0:
        query_set = list(Employee.objects.filter(employee_id=e_id).values("name", "email", "department"))
    else:
        query_set = list(Employee.objects.values("employee_id", "name", "email", "department"))
    return JsonResponse(query_set, safe=False)

def create_employee(*params):
    '''Method to add a new employee with Name, Email and Department'''
    request = params[0]
    data    = json.loads(request.body)
    e       = Employee(name=data["name"], email=data["email"], department=data["department"])
    e.save()
    return HttpResponse("OK")

def delete_employee(*params):
    '''Remove a employee from database, by ID or Name'''
    request = params[0]
    e_id    = params[1]
    e = Employee.objects.all()
    if e_id.isdigit():
        e = Employee.objects.filter(employee_id=e_id)
    else:
        e = Employee.objects.filter(name__startswith=e_id)
    if e.count() == 0:
        return HttpResponse("Employee already not exists!")
    else:
        e.delete()
    return HttpResponse("OK")

def detail(request, e_id):
    try:
        e = Employee.objects.get(pk=e_id)
    except Employee.DoesNotExist:
        raise Http404("Page does not exist")
    return render(request, 'employee/detail.html')

API_REQUESTS = {
        "GET" : list_employees,
        "POST": create_employee,
        "DELETE" : delete_employee,
        }

from django.shortcuts import (
render_to_response
)
from django.template import RequestContext

# HTTP Error 400
def bad_request(request):
    response = render_to_response(
    '400.html',
    context_instance=RequestContext(request)
    )

    response.status_code = 400

    return response
