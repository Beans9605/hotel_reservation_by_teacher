from django.shortcuts import render

# Create your views here.
def home(request):
    if request.session.get('modify_reservation') :
        request.session.modified = True
        del request.session['modify_reservation']
        return render(request, "mainsite/home.html", {"success" : "성공적으로 예약이 변경됐습니다."})
    elif request.session.get('reservation') :
        request.session.modified = True
        del request.session['reservation']
        return render(request, "mainsite/home.html", {"success": "성공적으로 예약했습니다."})
    else :
        return render(request, "mainsite/home.html")