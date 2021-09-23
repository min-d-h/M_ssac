from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from .models import User, Tproducts # Mynote
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.contrib.sessions.models import Session
import random

# Create your views here.

###############################################
# 실습 파일 업로드 부분
###############################################
# from .forms import UploadFileForm
# import os
# def upload_f(req):
#     if req.method == 'POST':
#         print (req.FILES['my_file'].name)
#         with open( os.path.abspath('./trip/static/' + req.FILES['my_file'].name), 'wb') as dest:
#             for chunk in req.FILES['my_file'].chunks():
#                 dest.write(chunk)
#         return render(req, 'index.html')
#     else :
#         return render(req, 'upload.html')
##############################################################################################

###############################################
# 메인
###############################################
def main (req) :
    sess = req.session.get('userid')
    try:
        check_c = User.objects.get(userid=sess)
        if sess :
            #유럽 랜덤 내용
            randNum1 = random.randint(1, 14)
            eu_pic = ['eu1', 'eu2', 'eu3', 'eu4', 'eu5', 'eu6', 'eu7',
                        'eu8', 'eu9', 'eu10', 'eu11', 'eu12', 'eu13', 'eu14']
            eu_name = ['독일', '독일', '네덜란드', '네덜란드', '스위스', '스위스', '영국',
                        '스코틀랜드', '터키', '터키', '체코', '체코', '스페인', '스페인']
            allPic1 = eu_pic[randNum1-1]
            allran1 = eu_name[randNum1-1]

            #아시아 랜덤 내용
            randNum2 = random.randint(1, 8)
            a_pic = ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8']
            a_name = ['싱가포르', '싱가포르', '태국', '태국', '터키', '터키', '대만', '대만']
            allPic2 = a_pic[randNum2-1]
            allran2 = a_name[randNum2-1]
            contact = {
                'cccc' : check_c,

                'eunum' : allPic1,
                'eupic' : allran1,

                'anum' : allPic2,
                'apic' : allran2
            }
            print("세션 시작! 여기는 메인입니다.", "아이디:", sess)
            return render (req, 'main.html', contact)
        return render(req, 'login.html')
    except :
        print("세선이 짤렸다고??")
        return redirect('../login/')

###############################################
# 로그인, 로그인완료, 로그아웃
###############################################
def login (req) :
        print("여기는 로그인입니다.")
        return render(req, 'login.html')

def login_s (req) :
    try:
        userid = req.POST.get('id')
        pwd = req.POST.get('pwd')
        log_s = User.objects.filter(userid = userid, password = pwd)
        if log_s :
            print ("로그인 성공")
            req.session["userid"] = req.POST.get('id')
            return redirect('../main/')
        else :
            print ("로그인 실패")
            return redirect('../login/')
    except ObjectDoesNotExist:
        print('기본 login 페이지')
        return render(req, 'login.html')

def logout (req) :
    req.session.pop('userid')
    return redirect('../login/')

###############################################
# 회원가입
###############################################
def signup (req) :
    print("여기는 회원가입입니다.")
    return render (req, 'signup.html')

def signup_s (req) :
    login_ss = User.objects.filter(userid=req.POST.get('id'))
    if login_ss :
        print ("회원가입 팅겼어요. 아이디중복")
        return render(req, 'signup.html', {'err':"아이디가 중복입니다. 확인해주세요."})
    else :
        print ("else탔다")
        login_sss = User (
            username=req.POST.get('name'),
            userid=req.POST.get('id'),
            password=req.POST.get('pwd'),
            gender=req.POST.get('gender'),
            email=req.POST.get('email'),
            text=req.POST.get('tt'),
            registered=req.POST.get('registered'),
        )
        login_sss.save ()
        print ("회원가입 완료")
        return render(req, 'login.html', {'suss':"회원가입이 완료되었습니다. 다시 로그인 해주세요"})

###############################################
# 회원 탈퇴
###############################################
def tal (req) :
    try:
        sess = req.session.get('userid')
        check_c = User.objects.get(userid=sess)
        print(sess)
        print(check_c)
        if sess :
            print(sess)
            req.session.pop('userid')
            check_c.delete()
            messages.info(req, '저희는 당신을 선택하지 않겠습니다.')
            return redirect('../login/')
    except ObjectDoesNotExist:
        print (" 탈퇴 실패 ")
        return redirect('../mypage/')

###############################################
# 마이페이지
###############################################
def mypage (req):
    try:
        sess = req.session.get('userid')
        check_c = User.objects.filter(userid=sess)
        if sess :
            print(" 마이페이지 들어갔다. ")
            return render(req, 'mypage.html', {'total_member':check_c})
    except ObjectDoesNotExist:
        return redirect('../mypage/')

###############################################
# 비밀번호 변경
###############################################
def reset (req) :
    print(" 리셋은 타냐? ")
    try:
        rr = User.objects.get(userid=req.POST.get('id'), password=req.POST.get('pwd'))
        if rr :
            print(" 비밀번호 변경 되었냐? ")
            rr.password=req.POST.get('npwd')
            rr.text=req.POST.get('ntt')
            print(rr, " 어 여기 ")
            rr.save()
            messages.success(req, '개인정보가 변경되었습니다.')
            return redirect('../main/')
    except ObjectDoesNotExist:
        print ("여기타는건 아니지????????")
        return render (req, 'mypage.html', {'pw_f':"개인정보 변경 실패"})

###############################################
# 비밀번호 찾기
###############################################
def search (req) :
    return render (req, 'search.html')

def pw_search1 (req) :
    search1 = User.objects.filter(userid=req.POST.get('id'), username=req.POST.get('name')).values_list(('password'), flat=True).first()  # {'course_code': 11}
    user_name = username=req.POST.get('name')
    if search1 :
        print(search1)
        return render (req, 'pw_search1.html', {'qqq':search1, 'www':user_name})
    else : 
        return  redirect('../search/')

###############################################
# 한줄 게시판 # 디테일 페이지 
###############################################
# def mynote (req):
#         sess = req.session.get('userid')
#         if not sess :
#             return redirect('../login/')
#         else :
#             mynotes = Mynote.objects
#             # noteid = req.GET.get('title')
#             print ("세션체크"+sess)
#             # method가 POST로 들어온게 있으면, 아래 내용을 실행할꺼야.
#             if req.method == "POST" : 
#                 note = Mynote (
#                     userid=req.POST.get('id'),
#                     title=req.POST.get('title'),
#                     body=req.POST.get('fulltext'),
#                 )
#                 # title 또는 fulltext가 none이면 되돌릴꺼야.
#                 if req.POST.get('title') is None or req.POST.get('fulltext') is None:
#                     print("프린트?")
#                     return redirect('../mynote/')
#                 # if str (req.POST.get('title')).strip() == "" and str (req.POST.get('fulltext')).strip() == "":
#                 #     print("프린트?")
#                 #     return redirect('../mynote/')
#                 else :
#                     print("저장이 되기 직전")
#                     note.save()
#                     print("저장이 됐다!")
#             return render (req, 'mynote.html', {'mynotes': mynotes, 'ssss':req.session["userid"]})
# def detail (req, mynote_id):
#     mynote_datail = get_object_or_404(Mynote, pk=mynote_id)
#     return render (req, 'detail.html', {'mynote':mynote_datail})
# def new(req):
#     full_text = req.GET['fulltext']
#     word_list = full_text.split()
#     word_dictionary = {}
#     for word in word_list:
#         if word in word_dictionary:
#             # Increase
#             word_dictionary[word] += 1
#         else:
#             # add to the dictionary
#             word_dictionary[word] = 1
#     return render(req, 'new.html', {'fulltext': full_text, 'total': len(word_list), 'dictionary': word_dictionary.items()} )


###############################################
# 장바구니
###############################################
def cart (req) :
    print("여기 타냐?")
    sess = req.session.get('userid')
    check_c = User.objects.get(userid=sess)
    # t_check = Tproducts.objects.get(tname=req.POST.get('tname'))
    if check_c :
        print("여기는 if야")
        ppp = Tproducts (
            start_date=req.POST.get('start_date'),
            tname=req.POST.get('tname1'),
            s_trip1=req.POST.get('s_trip1'),
            s_trip2=req.POST.get('s_trip2'),
            country=req.POST.get('country1'),
            count=req.POST.get('count1'),
        )
        print('ppp 끝났어')
        ppp.save ()
        print ("카트에 저장")
        # return render (req, 'cart.html', {'ssss':sess, 'nnnn':check_c})
        return redirect ('../cart/')
    else :
        print( '세션 확인하세요.' )
        return redirect ('../main/')

def m_ticket (req):
    return render(req, 'm_ticket.html')

# 날씨를 정합시다!!
def weather (req):
    try:
        sess = req.session.get('userid')
        check_c = User.objects.get(userid=sess)
        if check_c :
            print ("세션 확인")
            print(req.session["userid"])
        return render (req, 'weather.html', {'ssss':sess, 'nnnn':check_c})
    except :
        return render (req, 'weather.html')


###############################################
# 결제 페이지
###############################################
def payment (req):
        sess = req.session.get('userid')
        if sess :
            print("세션확인, payment페이지")
            check_c = User.objects.get(userid=sess)
            return render (req, 'payment.html', {'ssss':sess, 'nnnn':check_c})
        else :
            return redirect ('../main/')
    # return render(req, 'main.html')
