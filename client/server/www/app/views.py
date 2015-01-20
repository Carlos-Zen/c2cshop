from django.shortcuts import render
from app.models import HrGoods as Goods
from django.http import HttpResponse
import json
from pysimplesoap import client
from common.webclient import FromSoap
import logging
import simplejson as smjson
# Create your views here.
logger = logging.getLogger(__name__)

inList = ['check_user']
def index(request,seg):

	data=Goods.objects.get(goods_id=6)
	response = HttpResponse('''[{
    "firstName": "Barack",
    "lastName": "Obama",
    "occupation": "President"
  }
,{
    "firstName": "Barsdfacks",
    "lastName": "Obama",
    "occupation": "President"
  }]''')


	return response
def api(request,seg):
	fs = FromSoap()
	method = request.REQUEST.get('method')
	params = request.REQUEST.get('params')
	print 'params==>',params
	j_params = smjson.loads(params)
	if method in inList:
		if method is 'check_user':
			from common.controller import check_user_password
			data = check_user_password(params['a'],params['b'])
			return HttpResponse(smjson.dumps(data))
		
	else:	
		rst = apply(fs.call_func,(str(method),),j_params)
		try:	
			call_back = request.GET.get('jsonpCallback')
		except:
			call_back=''
		return HttpResponse(rst.strip("'"))

def test(request,seg):
	from common.controller import check_user_password
	data = check_user_password('duucoo','lianme')
	return HttpResponse(smjson.dumps(data[0])+request.REQUEST.get('a'))

	