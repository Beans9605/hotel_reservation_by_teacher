from django.shortcuts import render, redirect, get_object_or_404
from .models import Reservation, Room
from user.models import CustomUser
from datetime import date, datetime, timedelta

# Create your views here.

class ReservationBaseAlgorithm :
    # 필요한 데이터 생성자에서 받아옴
    def __init__ (self, start_day, end_day, night_num, people) :
        self.start_day = start_day
        self.end_day = end_day
        self.night_num = night_num
        self.people = people
    
    # 선택한 방이 빈 방인지 확인해주는 함수
    def selected_room_is_empty(self, room) :
        empty_rooms = self.reservation_base()

        for empty_room in empty_rooms :
            if empty_room is not None and empty_room == room :
                return True
            elif empty_room is None :
                return None
            
        return False

    # 예약 수정해주는 함수
    def modify_reservation (self, room) :
        if self.selected_room_is_empty(room) is True :
            return room
        else :
            return False

    # 예약 저장 함수
    def save_reservation(self, room, user) :
        new_reservation = Reservation (
            user = user,
            room = room,
            reservation_start_day = self.start_day,
            reservation_end_day = self.end_day,
            night_num = self.night_num,
            users_num = self.people
        )

        new_reservation.save()

    # 해당 날짜에 빈 모든 방을 보여줌
    def reservation_base(self) :
        # 빈 방을 찾기위한 여정 시작
        # 일단 모든 방을 다 가져와봄
        find_room = Room.objects.all()
        # 사용 중인 방을 받을 리스트 받기
        find_room_to_list = []

        # 내가 예약한 날짜를 기점으로 겹쳐서 예약이 되어있는지 확인하고, 방의 예약이 겹쳐있다면 리스트에 넣어서 정리
        for i in range(0, self.night_num) :
            reservate_that_day = Reservation.objects.filter(reservation_start_day = (self.start_day + timedelta(days=i)))
            if reservate_that_day :
                for reservate in reservate_that_day :
                    # 지우는거에서 퀴리셋 지랄 나서 못하는중 해결함 ^오^
                    find_room_to_list.append(reservate.room)

        # 예약된 방 리스트와 모든 방에 대한 객체를 확인해서 제외시킴
        for search in find_room_to_list :
            find_room = find_room.exclude(id = search.id)
        return find_room

    # 불러온 여러 개의 방에서 하나의 방만 골라서 return 해줌
    def reservation_find_empty_room (self) :
        empty_room_find = None

        find_room = self.reservation_base()

        if find_room :
            for find in find_room :
                if (empty_room_find == None) and (find.how_many_accept >= self.people) :
                    empty_room_find = find
                elif (empty_room_find is not None) and empty_room_find.how_many_accept > find.how_many_accept and find.how_many_accept >= self.people :
                    empty_room_find = find

        return empty_room_find
    



def reservation (request) :
    if request.method == "POST" and request.session.get('user') is not None :
        
        start_day = request.POST['start_day']
        end_day = request.POST['end_day']
        people = int(request.POST['adult']) + int(request.POST['child'])

        user = get_object_or_404(CustomUser, username=request.session['user'])

        start_day = datetime.strptime(start_day, "%Y-%m-%d")
        end_day = datetime.strptime(end_day, "%Y-%m-%d")

        night_num = int((end_day-start_day).days) - 1
        
        
        # 자동배정 예약에 대한 알고리즘을 구현화한 클래스 선언
        reservation_class = ReservationBaseAlgorithm(start_day, end_day, night_num, people)
        # 자동배정 예약 기능 사용, 비어있는 룸 확인
        empty_room_find = reservation_class.reservation_find_empty_room()
        
        if empty_room_find == None :
            context = {"err" : "이미 모든 객실이 사용중입니다. 다른 날짜를 선택해주세요"}
            return render(request, "reservation/reservation.html", context)
        else :
            # 예약 저장하는 함수
            reservation_class.save_reservation(empty_room_find, user)
        
        return redirect("home")
    elif request.session.get('user') is None  :
        return redirect('home')
    else :
        return render(request, "reservation/reservation.html")

