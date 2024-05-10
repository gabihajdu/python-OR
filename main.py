from django.shortcuts import redirect

foo = {
    "bar": "baz"
}

def test1(request):
    tainted = request.GET.get("next")
    tainted2 = request.GET.get("next2")

    redirect_url = f'{tainted2}?foo={tainted}' 

    return redirect(redirect_url) 

def test2(request):
    tainted = request.GET.get("next")
    tainted2 = request.GET.get("next2")
    tainted3 = request.GET.get("next3")

    redirect_url = f'{tainted3}?foo={tainted}&bar={tainted2}'

    return redirect(redirect_url)

def test3(request):
    tainted = request.GET.get("next")
    tainted2 = request.GET.get("next2")
    tainted3 = request.GET.get("next3")

    redirect_url = f'{foo.bar}AAA{tainted3}?foo={tainted}'

    return redirect(redirect_url) 


def test4(request):
    tainted = request.GET.get("next")
    tainted2 = request.GET.get("next2")
    tainted3 = request.GET.get("next3")

    redirect_url = f'{foo.bar}{tainted3}?foo={tainted}&bar={tainted2}' 

    return redirect(redirect_url) 

def test5(request):
    tainted = request.GET.get("next")
    tainted2 = request.GET.get("next2")
    tainted3 = request.GET.get("next3")

    redirect_url = f'{foo.bar}{foo.bar}{tainted3}?foo={tainted}&bar={tainted2}'

    return redirect(redirect_url) 

def test6(request):
    tainted = request.GET.get("next")
    tainted2 = request.GET.get("next2")
    tainted3 = request.GET.get("next3")

    redirect_url = f'{foo.bar}{foo.bar}{foo.bar}something{tainted3}?foo={tainted}&bar={tainted2}'

    return redirect(redirect_url) 


def test7(request):
    tainted = request.GET.get("next")
    tainted2 = request.GET.get("next2")
    tainted3 = request.GET.get("next3")

    redirect_url = f'{foo.bar}{foo.bar}{foo.bar}{foo.bar}something{tainted3}?foo={tainted}&bar={tainted2}'

    return redirect(redirect_url) 

def test8(request):
    tainted = request.GET.get("next")
    tainted2 = request.GET.get("next2")
    tainted3 = request.GET.get("next3")

    redirect_url = f'{foo.bar}{foo.bar}{foo.bar}{foo.bar}{foo.bar}AAA{tainted3}?foo={tainted}'

    return redirect(redirect_url) 

def test9(request):
    tainted = request.GET.get("next")
    tainted2 = request.GET.get("next2")
    tainted3 = request.GET.get("next3")

    redirect_url = f'{tainted3}{foo.bar}{foo.bar}{foo.bar}{foo.bar}{foo.bar}{foo.bar}?foo={tainted}'
    return redirect(redirect_url) 

def test10(request):
    tainted = request.GET.get("next")
    tainted2 = request.GET.get("next2")
    tainted3 = request.GET.get("next3")
    tainted4 = request.GET.get("next4")

    redirect_url = f'{foo.bar}{foo.bar}{foo.bar}{foo.bar}{foo.bar}{foo.bar}{tainted3}?foo={tainted}'

    return redirect(redirect_url) 

def test11(request):
    tainted = request.GET.get("next")
    tainted2 = request.GET.get("next2")
    tainted3 = request.GET.get("next3")

    redirect_url = f'{tainted3}{foo.bar}?foo={tainted}'

    return redirect(redirect_url) 


def test12(request):
    tainted = request.GET.get("next")
    tainted2 = request.GET.get("next2")
    tainted3 = request.GET.get("next3")

    redirect_url = f'{tainted3}{foo.bar}{foo.bar}{foo.bar}something?foo={tainted}'

    return redirect(redirect_url) 


def test13(request):
    tainted = request.GET.get("next")

    redirect_url = f'{tainted}{foo.bar}?foo={foo.bar}' 

    return redirect(redirect_url) 


def test14(request):
    tainted = request.GET.get("next")
    tainted2 = request.GET.get("next2")

    proto = "https://"
    tld = ".com"

    redirect_url = f'{proto}{tainted2}{tld}?foo={tainted}'

    return redirect(redirect_url) 


def test15(request):
    tainted = request.GET.get("next")
    tainted2 = request.GET.get("next2")

    redirect_url = f'http://example.com{tainted2}{foo.bar}something?foo={tainted}'

    return redirect(redirect_url) 


def test16(request):
    tainted = request.GET.get("next")
    tainted2 = request.GET.get("next2")
    tainted3 = request.GET.get("next3")

    redirect_url = f'{tainted3}example.com?foo={tainted}'
    
    return redirect(redirect_url) 
