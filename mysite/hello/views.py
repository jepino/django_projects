from django.http import HttpResponse

def myview(request):
    num_visits = request.session.get('num_visits', 0) + 1
    request.session['num_visits'] = num_visits
    if num_visits > 4 :
        del(request.session['num_visits'])
    response = HttpResponse("View count=" +str(num_visits))
    response.set_cookie('dj4e_cookie', '2e3d6c85', max_age=1000)
    return response