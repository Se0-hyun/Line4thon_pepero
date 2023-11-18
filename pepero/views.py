from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Pepero
import json

# 첫 시작 화면 렌더
def pepero_make_home_view(request):
    if request.method == 'GET':
        return render(request, 'peperos/main.html')
    return render(request, 'peperos/main.html')

# 그..홈 화면에서 빼빼로 1단계 넘어가기 전 효과 뷰 렌더
def pepero_make_start_view(request):
    if request.method == 'GET':
        return render(request, 'peperos/loading-start.html')
    elif request.method == 'POST':
        return render(request, 'peperos/loading-start.html')
    return render(request, 'peperos/loading-start.html')

# 빼빼로 1단계 만들기
def pepero_make_choco_view(request):
    if request.method == 'GET':
        print("빼빼로 1단계 시작")
        return render(request, 'peperos/pepero_make1.html')
    elif request.method == 'POST':
        try:
            post_data = json.loads(request.body.decode('utf-8'))
            selected_choco = post_data.get("selected_choco")
            if selected_choco:
                print("사용자 선택 초코 값 : "+selected_choco)
                request.session['selected_choco'] = selected_choco
                return JsonResponse({'message': 'Success'})
        except json.JSONDecodeError as e:
            return JsonResponse({'message': 'Error', 'error': str(e)})
    return render(request, 'peperos/pepero_make1.html')

# 빼빼로 2단계
def pepero_make_sauce_view(request):
    if request.method == 'GET':
        print("1단계에서 선택한 값 체크 :" + request.session['selected_choco'])
        print("빼빼로 2단계 시작")
        return render(request, 'peperos/pepero_make2.html')
    elif request.method == 'POST':
        try:
            post_data = json.loads(request.body.decode('utf-8'))
            selected_sauce = post_data.get('selected_sauce')
            if selected_sauce:
                print("사용자 선택 소스 값 : "+selected_sauce)
                request.session['selected_sauce'] = selected_sauce
                return JsonResponse({'message': 'Success'})
        except json.JSONDecodeError as e:
            return JsonResponse({'message': 'Error', 'error': str(e)})
        return render(request, 'peperos/pepero_make3.html')
    
# 빼빼로 3단계
def pepero_make_deco_view(request):
    if request.method == 'GET':
        print("1단계에서 선택한 값 체크 :" + request.session['selected_choco'])
        print("2단계에서 선택한 값 체크 :" + request.session['selected_sauce'])
        print("빼빼로 3단계 시작")
        return render(request, 'peperos/pepero_make3.html')
    elif request.method == 'POST':
        try:
            post_data = json.loads(request.body.decode('utf-8'))
            selected_deco = post_data.get('selected_deco')
            if selected_deco:
                print("사용자 선택 데코 값 : "+selected_deco)
                request.session['selected_deco'] = selected_deco
                return JsonResponse({'message': 'Success'})
        except json.JSONDecodeError as e:
            return JsonResponse({'message': 'Error', 'error': str(e)})
        return render(request, 'peperos/pepero_letter.html')

    
    
def pepero_make_letter_view(request):
    if request.method == 'GET':
        print("1단계에서 선택한 값 체크 :" + request.session['selected_choco'])
        print("2단계에서 선택한 값 체크 :" + request.session['selected_sauce'])
        print("3단계에서 선택한 값 체크 :" + request.session['selected_deco'])
        print("빼빼로 편지 쓰기 시작")
        return render(request, 'peperos/pepero_letter.html')
    elif request.method == 'POST':
        selected_choco = request.session['selected_choco']
        selected_sauce = request.session['selected_sauce']
        selected_deco = request.session['selected_deco']
        title = request.POST.get('title')
        content = request.POST.get('message')
        print(content)
        pepero = Pepero(choco=selected_choco, sauce=selected_sauce, deco=selected_deco, title=title, content=content)
        pepero.save()
        print("빼빼로 편지 완성 확인")
        return render(request, 'peperos/loading-ing.html')

    
    
# 빼빼로 전송하기 뷰 ( 효과 )
def pepero_make_ing_view(request):
    if request.method == 'GET':
        return render(request, 'peperos/loading-ing.html')
    return render(request, 'peperos/loading-ing.html')
# 빼빼로 전송완료 뷰 ( 효과 )
def pepero_make_end_view(request):
    if request.method == 'GET':
        return render(request, 'peperos/loading-end.html')
    return render(request, 'peperos/main.html')

# 빼빼로 리스트
def pepero_pepero_list(request):
    pepero_lists = Pepero.objects.all().order_by('-created_at')
    return render(request, 'peperos/pepero_list1.html', {'pepero_lists': pepero_lists})
    # return render(request, 'peperos/pepero_list1.html')

# 빼빼로 디테일
# 몇 번째(id) 편지인지 인자로 받음
def pepero_letter_detail(request, letter_id):
    letter_detail = get_object_or_404(Pepero, pk=letter_id)
    return render(request, 'peperos/pepero_detail1.html', {'letter_detail':letter_detail})
    # return render(request, 'peperos/pepero_detail1.html')
    

# 빼빼로 편지 리스트
def pepero_letters_list(request):
    pepero_lists = Pepero.objects.all().order_by('-created_at')
    return render(request, 'peperos/pepero_list.html', {'pepero_lists': pepero_lists})

def pepero_letters_detail(request,letter_id):
    letter_detail = get_object_or_404(Pepero, pk = letter_id)
    return render(request, 'peperos/pepero_detail.html', {'letter_detail':letter_detail})

