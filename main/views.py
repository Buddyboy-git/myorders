from pickle import FALSE
from django.shortcuts import render
from django.core.files import File
from django.shortcuts import HttpResponse
from django.http import JsonResponse
from django import template
from django.views.generic import TemplateView
from django.views.decorators.csrf import requires_csrf_token

from django.core.serializers import serialize
import datetime
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from main.models import store_history, thumanns_product_import, store
#@csrf_exempt
@requires_csrf_token

class HomePageView(TemplateView):
    template_name = "order_input.html"

def index(request):
    return HttpResponse("<p>Hello Django <a href='/hw' >Hello World </a></p>")

def homePageView(request):
    return HttpResponse("<p>Hello Django <a href='/hw' >Hello World </a></p>")

def today_is(request):
    now = datetime.datetime.now()
    html = "<html><body>Current date and time: {0}</body></html>".format(now)
    return HttpResponse(html)

def profile(request):
    return HttpResponse("<p>Profile page of user</p>")

def order_input(request):
    t = template.loader.get_template('main/order_input.html')
    #c = template.Context({'now': now})
    html = t.render()
    return HttpResponse(html)

def helloworld(request):
    t = template.loader.get_template('main/helloworld.html')
    #c = template.Context({'now': now})
    html = t.render()
    return HttpResponse(html)
# Create your views here.

def clearfile(request):
    thumanns_product_import.objects.all().delete()
    return HttpResponse('Done!')   


def readfile(request):
    thumanns_product_import.objects.all().delete()
    f = open('main/product_imports/thumasteritems-current.csv', 'r')
    for line in f:  
        line =  line.split(',')  
        product = thumanns_product_import()  
        product.itemnum = line[0]  
        product.description = line[1]  
        product.price = line[2]  
        product.priceunit = line[3]  
        product.pickunit = line[4]  
        product.avgweight = line[5]  
        product.save()  

    f.close()  
#    if f.mode == 'r':
#       contents =f.read()
#       print (contents)
    return HttpResponse('Done!')   

def writefile(request):
    f = open('test.txt', 'w')
    testfile = File(f)
    testfile.write('Welcome to this country')
    testfile.close
    f.close
    return HttpResponse()

def ajax_view(request):
    myvar = request.GET['search']
    queryset = thumanns_product_import.objects.filter(description__contains=myvar)
    mycount = queryset.count()
#    data = {"msg": "It worked!!",}
    myserialized = serialize('json',list(queryset), fields=('itemnum','description'))
#    return HttpResponse(data, content_type="application/json")
#    return JsonResponse(request, safe=False)
#    return JsonResponse(myserialized, safe=False)
    return JsonResponse(myserialized,safe=False)

def ajax_getstore(request):
    myvar = request.GET['store']
    queryset = store.objects.filter(nickname__startswith=myvar)
    mycount = queryset.count()
    if mycount > 0:
        return_msg = "found"
    else :
        return_msg = "HTTP/1.1 404 Not Found"
        return render(request,"HTTP/1.1 404 Not Found")
    myserialized = serialize('json',list(queryset), fields=('id','name','nickname'))
    return JsonResponse(myserialized,safe=False)
#    return HttpResponse(return_msg)

def ajax_getproduct(request):
    thisstore = request.GET['store_id']
    thisqty = request.GET['qty']
    thisnickname = request.GET['product_nickname']
    thisnicknamelen = len(thisnickname)
    mycount = 0
    queryset = store_history.objects.filter(store_id = thisstore, product_nickname=thisnickname[-thisnicknamelen:])
    mycount = queryset.count()
    while thisnicknamelen >= 1 and mycount == 0:
        queryset = store_history.objects.filter(store_id = thisstore, product_nickname__contains=thisnickname[-thisnicknamelen:])
        mycount = queryset.count()
        thisnicknamelen = thisnicknamelen - 1

    if mycount > 0:
        myserialized = serialize('json',list(queryset), fields=('store_id','name','product_itemnum','product_name','product_default_uom_code','supplier_name'))
        return JsonResponse(myserialized,safe=False)
    else :
#        myserialized = serialize('json',list(queryset), fields=('store_id','name','product_itemnum','product_name','product_default_uom_code','supplier_name'))
        return HttpResponse("We Not Found")
#        return render(request,"HTTP/1.1 404 Not Found")

def ajax_getproducts(request):
    print("HELLO")
    myarray = json.loads(request.POST.get('dataArray'))
    queryset = store.objects.filter(nickname__startswith=myarray[0])
    mycount = queryset.count()
    if mycount > 0:
        for i in queryset:
            print("nickname: "+i.nickname+" name:"+i.name)
        myserialized = serialize('json',list(queryset), fields=('nickname','name'))
        return JsonResponse(myserialized,safe=False)
    print("GOODBYE")
    return HttpResponse(" Store Not Found...")
#    reqArray = json.loads(request.args.get('dataArray'))
#    if mycount > 0:
#        myserialized = serialize('json',list(queryset), fields=('store_id','name','product_itemnum','product_name','product_default_uom_code','supplier_name'))
#    return JsonResponse(myserialized,safe=False)
