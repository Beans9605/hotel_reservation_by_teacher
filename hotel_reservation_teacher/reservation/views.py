from django.shortcuts import render, redirect, get_object_or_404
from .models import Reservation, Room
from user.models import CustomUser
from datetime import date, datetime, timedelta
from django.forms.models import model_to_dict

# Create your views here.

def reservation (request) :
    if request.method == "POST" and request.session.get('user', False) :
        start_day = request.POST['start_day']
        end_day = request.POST['end_day']
        people = int(request.POST['adult']) + int(request.POST['child'])

        user = get_object_or_404(CustomUser, username=request.session['user'])

        start_day = datetime.strptime(start_day, "%Y-%m-%d")
        end_day = datetime.strptime(end_day, "%Y-%m-%d")

        night_num = int((end_day-start_day).days) - 1

        empty_room_find = None
        find_room = Room.objects.all()
        find_room_to_list = []
        print(find_room)

        for i in range(0, night_num) :
            reservate_that_day = Reservation.objects.filter(reservation_start_day = (start_day + timedelta(days=i)))
            if reservate_that_day :
                for reservate in reservate_that_day :
                    # 지우는거에서 퀴리셋 지랄 나서 못하는중
                    find_room_to_list.append(reservate.room)
        

        if find_room :
            for find in find_room :
                if empty_room_find is None :
                    empty_room_find = find
                elif empty_room_find.how_many_accept > find.how_many_accept and find.how_many_accept > people :
                    empty_room_find = find
        
        if empty_room_find is None :
            context = {"err" : "이미 모든 객실이 사용중입니다. 다른 날짜를 선택해주세요"}
            return render(request, "reservation/reservation.html", context)
        else :
            new_reservation = Reservation (
                user = user,
                room = empty_room_find,
                reservation_start_day = start_day,
                reservation_end_day = end_day,
                night_num = night_num,
                users_num = people
            )

            new_reservation.save()
        
        return redirect("home")
    
    else :
        return render(request, "reservation/reservation.html")