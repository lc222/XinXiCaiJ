# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render_to_response
from caiji.models import XinXiCaiJi
# 表单
def search_form(request):
	return render_to_response('search_form.html')

# 接收请求数据
def search(request):
	request.encoding='utf-8'
	if 'q' in request.GET:
		message = '你搜索的内容为: ' + request.GET['q'].encode('utf-8')
	else:
		message = '你提交了空表单'
	return HttpResponse(message)

def caijiwancheng(request):
	request.encoding = 'utf-8'
	message = ''
	for key in request.GET:
		if request.GET[key] == '':
			message = '请填写完整信息'
			break
	if 'xingming' in request.GET and message == '':
		message = request.GET['xingming'].encode('utf-8') + '同学，你的信息录入完成。谢谢配合~'
		test1 = XinXiCaiJi(xingming = request.GET['xingming'], xuehao = request.GET['xuehao'], daoshi = request.GET['daoshi'],
						   dsdianhua = request.GET['dsdianhua'], brdianhua = request.GET['brdianhua'], eMail = request.GET['eMail'],
						   weixin = request.GET['weixin'], QQ = request.GET['QQ'], weight = request.GET['weight'], height = request.GET['height'],
						   size = request.GET['size'], huochezhan = request.GET['huochezhan'], habit = request.GET['habit'],
						   money = request.GET['money'], baba = request.GET['baba'], babaGongzuo = request.GET['babaGongzuo'], babatel = request.GET['babatel'],
						   mama = request.GET['mama'], mamaGongzuo = request.GET['mamaGongzuo'], mamatel = request.GET['mamatel'], hometel = request.GET['hometel'],
						   homeadd = request.GET['homeadd'], beijing = request.GET['beijing'], beijingGongzuo = request.GET['beijingGongzuo'],
						   beijingtel = request.GET['beijingtel'], dor = request.GET['dor'], dorP = request.GET['dorP'])
		test1.save()
	return HttpResponse(message)