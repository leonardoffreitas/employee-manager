from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseNotFound
from django.http import JsonResponse
from employee.models import Employee
import json

@csrf_exempt
def api_employee(*params):
    '''Main method to use api'''
    response = API_REQUESTS[params[0].method](*params)
    return response

def list_employees(*params):
    '''Method to get list with all employes and them specs'''
    '''The search by a especific employ can be done with Name or Id'''
    request   = params[0]
    e_id      = params[1]
    query_set = None
    if e_id.isdigit():
        query_set = list(Employee.objects.filter(employee_id=e_id).values("name", "email", "department"))
    elif len(e_id) > 0:
        query_set = list(Employee.objects.filter(name__contains=e_id).values("name", "email", "department"))
    else:
        query_set = list(Employee.objects.values("employee_id", "name", "email", "department"))
    if len(query_set) == 0:
        return HttpResponseNotFound()
    return JsonResponse(query_set, safe=False)

def create_employee(*params):
    '''Method to add a new employee with Name, Email and Department'''
    request = params[0]
    data    = json.loads(request.body)
    e       = Employee(name=data["name"], email=data["email"], department=data["department"])
    e.save()
    return HttpResponse("OK", status=201)

def delete_employee(*params):
    '''Remove a employee from database, by ID or Name'''
    request = params[0]
    e_id    = params[1]
    e = Employee.objects.all()
    if e_id.isdigit():
        e = Employee.objects.filter(employee_id=e_id)
    elif len(e_id) > 0:
        e = Employee.objects.filter(name__contains=e_id)
    else:
        return HttpResponseNotFound()
    if e.count() == 0:
        return HttpResponseNotFound()
    else:
        e.delete()
    return HttpResponse("OK")

API_REQUESTS = {
        "GET" : list_employees,
        "POST": create_employee,
        "DELETE" : delete_employee,
        }
