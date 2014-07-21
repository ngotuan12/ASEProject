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
			close_cycle_all()
		except Exception as ex:
			print(ex)
		context = {'msg':'done'}
		return render(request,'myapp/CreateDms.html', context)
def createcustomer(user,id_no, address,home_address, fone_number, about):
		try:
			vtoday = date.today()
			ct = Customer()
			ct.cus_id= user
			ct.cus_code = user.username
			ct.first_name = user.first_name
			ct.last_name = user.last_name
			ct.full_name = user.first_name + user.last_name
			ct.id_no = id_no
			ct.address = address
			ct.home_address = home_address
			ct.fone_number = fone_number
			ct.create_date = vtoday
			ct.status = 1
			ct.about = about
			ct.save()
		except Exception as ex:
			print(ex)
def createcusdebit(user,amount, loan_date,amount,rate):
		try:
			vtoday = date.today()
			cd = CusDebit()
			cd.cus_id  = user
			cd.month = loan_date
			cd.debit = amount
			cd.total_debit = amount
			cd.payment = 0.00
			cd.create_date = vtoday
			cd.loan_date = loan_date
			cd.status = 1
			cd.note =''
			cd.save()
			createcusdebitdetail(user,cd)
		except Exception as ex:
			print(ex)
def createcusdebitdetail(userid,cusdebitid,loan_date,amount,rate):
		try:
			cdt = CusDebitDetail()
			cdt.cus_id  = userid
			cdt.cus_debit_id  = cusdebitid
			cdt.from_date= loan_date
			cdt.to_date= vtoday + relativedelta(months=+1) 
			cdt.rate = rate
			cdt.start_cycle = amount
			cdt.amount = float(str((cdt.to_date - cdt.from_date).days))*cdt.rate
			cdt.payment = 0
			cdt.end_cycle = cdt.start_cycle + cdt.amount - cdt.payment
			cdt.debit = 0
			cdt.status = 1
			cdt.save()
		except Exception as ex:
			print(ex)
def close_cycle_all():
		try:
			lscd = CusDebit.objects()
			for cd in lscd:
				close_cycle_cus(cd.id) 
		except Exception as ex:
			print(ex)

def close_cycle_cus(user):
		try:
			vuser = User.objects.get(user=request.user)
			lscd = CusDebit.objects(cus_id = vuser.id,status=1).order_by('loan_date')
			for cd in lscd:
				analyze_debit(cd.id) 
				
		except Exception as ex:
			print(ex)
def analyze_debit(vcus_debit_id):
		try:
			vtoday = datetime.now().strftime("%y-%m-%d-%H-%M-%S")
			print(vnow)
			lsCdt = CusDebitDetail.objects().get(cus_debit_id = vcus_debit_id).order_by('from_date')
			#Du thang no
			total_debit = 0.00
			last_cycle = datetime.now().strftime("%y-%m-%d-%H-%M-%S")
			for cdt in lsCdt:
				if (cdt.to_date - datetime.strptime(vtoday,"%y-%m-%d-%H-%M-%S")).days > 0 :
					cdt.amount = float(str((datetime.strptime(vtoday,"%y-%m-%d-%H-%M-%S") - cdt.from_date).days))*cdt.rate
					cdt.to_date = vtoday
				else:
					cdt.amount = float(str((cdt.to_date - cdt.from_date).days))*cdt.rate
				last_cycle = cdt.end_date
				cdt.end_cycle = cdt.start_cycle + cdt.amount - cdt.payment
				cdt.debit = 0
				cdt.status = 1
				cdt.save()
				total_debit += cdt.end_cycle
			# insert them ban ghi chi tiet neu thieu
			vMissing = float(str((datetime.strptime(vtoday,"%y-%m-%d-%H-%M-%S") - last_cycle).days)) 
			if  vMissing > 0:
				print('Thieu chu ky cuoc: Insert them' + vMissing)
			else:
				print('Du chu ky cuoc') 
		except Exception as ex:
			print(ex)
		return 	total_debit