'''
Created on Apr 3, 2014
@author: TuanNA
'''
from datetime import date, datetime, time
from dateutil.relativedelta import relativedelta

from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from mongoengine.django.auth import User
from mongoengine.fields import ReferenceField

from myapp.models.CusDebit import CusDebit
from myapp.models.CusDebitDetail import CusDebitDetail
from myapp.models.Customer import Customer

@login_required(login_url='/signin')
def index(request):
	if request.method == 'GET':
		try:
			user=request.user
			#createcustomer(user)
			#createcusdebit(user)
			close_cycle()
		except Exception as ex:
			print(ex)
		context = {'msg':'done'}
		return render(request,'myapp/CreateDms.html', context)
def createcustomer(user):
		try:
			vtoday = date.today()
			ct = Customer()
			ct.cus_id= user
			ct.cus_code = user.username
			ct.first_name = user.first_name
			ct.last_name = user.last_name
			ct.full_name = user.first_name + user.last_name
			ct.id_no = '111519954'
			ct.address = 'Ha Noi'
			ct.home_address = ''
			ct.fone_number = '0977868788'
			ct.create_date = vtoday
			ct.status = 1
			ct.about = 'This is cuongNM infomation'
			ct.save()
		except Exception as ex:
			print(ex)
def createcusdebit(user):
		try:
			vtoday = date.today()
			cd = CusDebit()
			cd.cus_id  = user
			cd.month = vtoday
			cd.debit = 100000
			cd.create_date = vtoday
			cd.loan_date = vtoday
			cd.status = 1
			cd.note =''
			cd.save()
			createcusdebitdetail(user,cd)
		except Exception as ex:
			print(ex)
def createcusdebitdetail(userid,cusdebitid):
		try:
			vtoday = date.today()
			cdt = CusDebitDetail()
			
			cdt.cus_id  = userid
			cdt.cus_debit_id  = cusdebitid
			cdt.from_date= vtoday
			cdt.to_date= vtoday + relativedelta(months=+1) 
			cdt.rate = 1
			cdt.start_cycle = 10
			cdt.amount = float(str((cdt.to_date - cdt.from_date).days))*cdt.rate
			cdt.payment = 0
			cdt.end_cycle = cdt.start_cycle + cdt.amount - cdt.payment
			cdt.debit = 0
			cdt.status = 1
			cdt.save()
		except Exception as ex:
			print(ex)
def close_cycle():
		try:
			vtoday = date.today()
			vnow = datetime.now().strftime("%y-%m-%d-%H-%M-%S")
			print(vnow)
			cd = CusDebit.objects()
			lsCdt = CusDebitDetail.objects()
			numofdate = 0
			for cdt in lsCdt:
				
				print()
				print(vnow)
				print(datetime.strptime(vnow,"%y-%m-%d-%H-%M-%S"))
				print((cdt.to_date - datetime.strptime(vnow,"%y-%m-%d-%H-%M-%S")).days)
				
				
				if (cdt.to_date - datetime.strptime(vnow,"%y-%m-%d-%H-%M-%S")).days > 0 :
					cdt.amount = float(str((datetime.strptime(vnow,"%y-%m-%d-%H-%M-%S") - cdt.from_date).days))*cdt.rate
					cdt.to_date = vtoday
				else:
					cdt.amount = float(str((cdt.to_date - cdt.from_date).days))*cdt.rate
				
				cdt.end_cycle = cdt.start_cycle + cdt.amount - cdt.payment
				cdt.debit = 0
				cdt.status = 1
				cdt.save()
				
		except Exception as ex:
			print(ex)