# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,render_to_response,HttpResponse
from django.http import HttpResponse
from django.views.generic import TemplateView
from polls.forms import hform
import requests,json
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut




# Create your views here.
class Homeview(TemplateView):
	
	temp_name1='index.html'
	temp_name2='index2.html'
	def get(self,request,**kwargs):
		form=hform()		
		return render(request,self.temp_name1,{'form':form})
	
	def post(self,request,**kwargs):
		form=hform()
		if request.method!='POST':
			return render(request,self.temp_name1,{'form':form})
		
		#if form.is_valid():

		ar = request.POST.get('area')
		print ar

		if ar==None:
			return render(request,self.temp_name1,{'form':form})
		url='https://api.instagram.com/v1/users/self/media/recent'
		payload={'access_token':'5428220330.c358b65.91f56b3fe65b4d42805d3d577a5aca7c'}
		headers={'content-type':'application/jsonp'}
		locator=Nominatim()
		try:
			geo=locator.geocode(ar)
		except GeocoderTimedOut:
			geo=locator.geocode(ar)
		except ValueError as err:
			print ("Error - Goecoding failed with following message",err)


		if geo!=None:
			lat=geo.latitude
			lon=geo.longitude
		else:
			print "Geocoding failed"

		resp=requests.get(url,params=payload,headers=headers)
		username=resp.json()['data'][0]['user']['username']
		profile_pic=resp.json()['data'][0]['user']['profile_picture']
		liked_pic=resp.json()['data'][0]['images']['low_resolution']['url']
		# print profile_pic
		# print liked_pic
		likes=resp.json()['data'][0]['likes']['count']
		caption=resp.json()['data'][0]['caption']['text']






		args={'caption':caption,'ar':ar,'profile_pic':profile_pic,'lat':lat,'lon':lon,'likes':likes,'liked_pic':liked_pic}
		return render_to_response('index2.html', args)

	


#client id-c358b65d5c674c3f8a9aa105e64fe57a
#client secret- d4022116bb794429b67cb92aea41403f



#http://instagram.com/oauth/authorize/?client_id=c358b65d5c674c3f8a9aa105e64fe57a&redirect_uri=http://localhost:8000&response_type=token

#access_token=5428220330.c358b65.91f56b3fe65b4d42805d3d577a5aca7c