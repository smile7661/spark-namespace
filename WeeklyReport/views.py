from datetime import datetime

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, HttpResponse

from WeeklyReport.models import Users, report


# Create your views here.


# def index(request):
#     if request.method == 'POST':
#         # 获取当前登录用户通过request.user
#         report_name = request.user
#         weeklyreport = request.POST
#         report_redflag = weeklyreport.get('redFlag')
#         report_achievements = weeklyreport.get('Achievements')
#         report_SupportNeeded = weeklyreport.get('SupportNeeded')
#         report_date = weeklyreport.get('report_date')
#         report_date = datetime.strptime(report_date, '%Y%m%d').date()
#         report.objects.create(report_name=report_name, report_date=report_date, report_redflag=report_redflag,
#                               report_achievements=report_achievements, report_supportNeeded=report_SupportNeeded)
#         return render(request, 'WeeklyReport/list.html')
#
#     return render(request, 'WeeklyReport/index1.html')
#
#
# def report_login(request):
#     # 如果用户填写表单，登陆系统，就需要进行用户登录验证，否则返回登陆表单。
#     if request.method == 'POST':
#         postcontent = request.POST
#         user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
#         if user is None:
#             return render(request, 'WeeklyReport/login1.html', {'login_error': '用户名或密码错误,请重新登陆'})
#         else:
#             login(request, user)
#             return redirect('WeeklyReport:主页')
#     else:
#         return render(request, 'WeeklyReport/login1.html')
#
#
# def register(request):
#     if request.method == 'POST':
#         register_form = UserCreationForm(request.POST)
#         if register_form.is_valid():
#             register_form.save()
#             user = authenticate(request, username=register_form.cleaned_data['username'],
#                                     password=register_form.cleaned_data['password1'])
#             login(request, user)
#             return redirect('WeeklyReport:主页')
#         else:
#             register_form = UserCreationForm()
#
#     content = {'register_form': register_form}
#     return render(request, 'WeeklyReport/register1.html', context=content)
#
#
# def report_logout(request):
#     logout(request)
#     return redirect('WeeklyReport:登陆')
#
#
# def query(request):
#     username = request.GET.get('username')
#     password = request.GET.get('password')
#     user_result = Users.objects.filter(user_name=username, user_password=password)
#     if len(user_result) > 0:
#        return redirect('/index')
#     else:
#        return HttpResponse("该用户不存在")
#
#
# def view(request):
#     redirect('WeeklyReport:man')
