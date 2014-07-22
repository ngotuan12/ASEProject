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
def getCustomerInfo():
	username=request.user
	user=User.objects.get(username=str(request.user))
	customer = Customer.objects(ownner = user.id)
	return customer
def getCustomerDebitInfo():
	username=request.user
	user=User.objects.get(username=str(request.user))
	customerdebit = CusDebit.objects(ownner = user.id)
	return customerdebit
def getCustomerDebitDetail():
	username=request.user
	user=User.objects.get(username=str(request.user))
	customerdebitdetail = Customer.objects.get(ownner = user.id)
	return customerdebitdetail
def getPaymentHistory():
	username=request.user
	user=User.objects.get(username=str(request.user))
	customerdebitdetail = CusDebitDetail.objects(ownner = user.id)
	return customerdebitdetail
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
			createcusdebitdetail(user,cd,)
		except Exception as ex:
			print(ex)
def createcusdebitdetail(vUser,vCus_debit,vLoan_date,vAmount,vRate):
		try:
			cdt = CusDebitDetail()
			cdt.cus_id  = vUser_id
			cdt.cus_debit_id  = vCus_debit
			cdt.from_date= vLoan_date
			cdt.to_date= vLoan_date + relativedelta(months=+1) 
			cdt.rate = vRate
			cdt.start_cycle = vAmount
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
				close_cycle_cus(cd.cus_id) 
		except Exception as ex:
			print(ex)

def close_cycle_cus(vcus_id):
		try:
			lscd = CusDebit.objects(cus_id = vcus_id,status=1).order_by('loan_date')
			for cd in lscd:
				analyze_debit_detail(vCus_id,cd.id,vLoan_date)
				
		except Exception as ex:
			print(ex)
def analyze_debit_detail(vcus_debit_id):
		try:
			vtoday = datetime.now().strftime("%y-%m-%d-%H-%M-%S")
			lsCdt = CusDebitDetail.objects().get(cus_debit_id = vCus_debit_id).order_by('from_date')
			
			vLoan_months = (datetime.strptime(vtoday,"%y-%m-%d-%H-%M-%S") - vLoan_date).months
			if vLoan_months >=  lsCdt.length:
				#Thieu ban ghi chi tiet
				insert_missing_debit_detail(vCus_id,vCus_debit_id,vFrom_date,vEnd_cycle,vRate)
			lsCdt = CusDebitDetail.objects().get(cus_debit_id = vCus_debit_id).order_by('from_date')
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
				if float(str((datetime.strptime(vtoday,"%y-%m-%d-%H-%M-%S") - last_cycle).days)) > 0:
					cdt.is_current_month = 0
				else:
					cdt.is_current_month = 1
				cdt.save()
				total_debit += cdt.end_cycle
			# insert them ban ghi chi tiet neu thieu
			vMissing = float(str((datetime.strptime(vtoday,"%y-%m-%d-%H-%M-%S") - last_cycle).days)) 
			if  vMissing > 0:
				print('Thieu chu ky cuoc: Insert them' + vMissing)
			else:
				print('Du chu ky cuoc')
			#Update total debit
			cd = CusDebit.objects(id = vcus_debit_id)
			cd.total_debit = total_debit
			cd.save()
			
		except Exception as ex:
			print(ex)
def make_payment(vCus_id,vAmount,vPay_date):
		try:
			vtoday = datetime.now().strftime("%y-%m-%d-%H-%M-%S")
			#vuser = User.objects.get(id=vCus_id)
			vCustomer = Customer.objects(cus_id = vCus_id)
			lscd = CusDebit.objects(cus_id = vCus_id,status=1).order_by('loan_date')
			#Insert data in to Payment
			#-------------------------------------------------------------------------
			pt = Payment.objects()
			
			pt.cus_id  = vCustomer
			pt.create_date= vtoday
			pt.pay_date= vPay_date
			pt.amount = vAmount
			pt.status = 1
			#-------------------------------------------------------------------------
			for cd in lscd:
				analyze_payment(vCus_id,cd.id,vAmount,pt.id)
				
		except Exception as ex:
			print(ex)
def analyze_payment(vCus_id,vcus_debit_id,vAmount,vPayment_id):
	try:
		vToday = datetime.now().strftime("%y-%m-%d-%H-%M-%S")
		vRemainAmount = vAmount
		lscdt = CusDebitDetail.objects(cus_debit_id = vcus_debit_id,status=1).order_by('loan_date')
		pdt = PaymentDetail.objects()
		
		for cd in lscdt:
			payment_amount = 0.00
			current_debit = cd.end_cycle
			if vRemainAmount > 0:
				if cd.end_cycle >= vAmount:
					payment_amount = vAmount
					cd.payment = payment_amount
					remain_debit = cd.end_cycle - payment_amount
					cd.end_cycle = remain_debit
					vRemainAmount = 0.00
				else:
					payment_amount = cd.end_cycle
					cd.payment = payment_amount
					remain_debit = cd.end_cycle - payment_amount
					cd.end_cycle = remain_debit
					vRemainAmount = vAmount - payment_amount
				#Insert into payment detail
				
				pdt.payment_id = vPayment_id
				pdt.cus_debit_id = vcus_debit_id
				pdt.cus_id  = vCus_id
				pdt.create_date= vToday
				pdt.debit = current_debit
				pdt.payment = payment_amount
				pdt.remain = pdt.debit - pdt.payment 
				pdt.status = 1
				pdt.save()
		#End for
		if vRemainAmount > 0:
			analyze_payment(vCus_id,vcus_debit_id,vRemainAmount,vPayment_id)
	except Exception as ex:
		print(ex)
def insert_missing_debit_detail(vCus_id,vCus_debit_id,vFrom_date,vStart_cycle,vRate):
	try:
		vToday = datetime.now().strftime("%y-%m-%d-%H-%M-%S")
		vTodate = vFrom_date + relativedelta(months=+1)
		
		while (datetime.strptime(vToday,"%y-%m-%d-%H-%M-%S") - vTodate ).months >= 0:
			cdt = CusDebitDetail()
			cdt.cus_id  = vCus_id
			cdt.cus_debit_id  = vCus_debit_id
			cdt.from_date= vFrom_date
			cdt.to_date= vTodate 
			cdt.rate = vRate
			cdt.start_cycle = vStart_cycle

			if (cdt.to_date - datetime.strptime(vToday,"%y-%m-%d-%H-%M-%S")).months >= 0 :
				cdt.amount = float(str((datetime.strptime(vToday,"%y-%m-%d-%H-%M-%S") - cdt.from_date).days))*cdt.rate
				cdt.to_date = vtoday
			else:
				cdt.amount = float(str((cdt.to_date - cdt.from_date).days))*cdt.rate
			cdt.payment = 0
			cdt.end_cycle = cdt.start_cycle + cdt.amount - cdt.payment
			cdt.debit = 0
			cdt.status = 1
			#---------------------------------------------------------------------
			# Assign for next cycle
			vFrom_date = cdt.to_date
			vTodate = vFrom_date + relativedelta(months=+1)
			vStart_cycle = cdt.end_cycle
			#---------------------------------------------------------------------
			cdt.save()
			
	except Exception as ex:
		print(ex)
		