'''
Created on Apr 3, 2014
@author: TuanNA
'''
# from dateutil.relativedelta import relativedelta
from datetime import datetime
import math

from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from mongoengine.django.auth import User

from myapp.models.CusDebit import CusDebit
from myapp.models.CusDebitDetail import CusDebitDetail
from myapp.models.Customer import Customer
from myapp.views.CreateDms import CusDebit,CusDebitDetail,Customer ,\
	createcusdebit


# @login_required(login_url='/signin')
def index(request):
	if request.method == 'GET':
		try:
			print(pow(2, 5));
			type=''
			user_name='anhphongkiem'
			debt_owner=User.objects.get(username=user_name)
			lsCusomer=Customer.objects(debt_owner=debt_owner.id)
			
			lsCusDebit = CusDebit.objects(status=1).order_by('loan_date')
			
			if 'type' in request.GET:
				if request.GET['type']=='chovay':
					type = 'chovay'
					
				elif request.GET['type']=='trano':
					type = 'trano'
		except Exception as ex:
			print(ex)
		finally:
			context = {'type':type,'lsCusomer':lsCusomer,'lsCusDebit':lsCusDebit}
		return render(request,'myapp/d-CustomerDebitDetail.html', context)
	elif request.method == 'POST':
		if request.POST['type'] == "cusLoan":
			try:
				cus_id = request.POST['hd_cus_id']
				cusDebit_debit =float(request.POST['hd_cus_amount'])
				cusDebit_loan_date=datetime.strptime(request.POST['cus_loan_date'],'%m/%d/%Y')
				cusDebit_rate = float(request.POST['hd_cus_rate'])
				cus=Customer.objects.get(id=cus_id)
				
				createcusdebit(cus,cusDebit_loan_date,cusDebit_debit,cusDebit_rate)
				
				print('add cusdebit ')
				type = "chovay"
				user_name='anhphongkiem'
				debt_owner=User.objects.get(username=user_name)
				lsCusomer=Customer.objects(debt_owner=debt_owner.id)
				
			except Exception as ex:
				print(ex)
			finally:
				context = {'type':type,'lsCusomer':lsCusomer}
				return render(request,'myapp/d-CustomerDebitDetail.html', context)