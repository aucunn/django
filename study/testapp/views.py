from django.shortcuts import render
from testapp.models import Regist

def LoginChek(request):
    #try:
    if True:
        uid = request.POST.get('id')
        upass = request.POST.get('pass')

        result = Regist.objects.filter(uId=uid, uPass=upass)[0]
	
        if result.uNo > 0:
            request.session['userId'] = uid
            request.session['userName'] = result.uName
            page = '<script type="text/javascript"> location.href="../main";</script><br />'
            return HttpResponse(page)
        else :
            return render(request, 'myapp/login.html', { 'text': "로그인실패1"})
   # except Exception:
   #     return render(request, 'myapp/login.html', { 'text': "로그인실패2"})

def RegistChek(request):
    try:
        uid = request.POST.get('id')
        upass = request.POST.get('pass')
        urepass = request.POST.get('repass')
        uname = request.POST.get('name')

        if (upass == urepass):
            uname = uname.strip()
            Regist(uId = uid, uPass = upass, uName = uname, uEmail="기본").save()
            page = 'script type="text/javascript"> location.href="../main";</script><br />'
        return HttpResponse(page)
    except:
        return render(request, 'myapp/regist.html')

def MainPage(request):
    
    return render(request, 'myapp/main.html', { 'neame': request.session['name']})
# Create your views here.
