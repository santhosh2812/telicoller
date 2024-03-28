from django.http import HttpResponse
from rest_framework.response import Response
import datetime
import time
from django.views import View
from rest_framework.views import APIView
from .models import *
from .utils import *



class DataUpload(APIView):
    def post(self,request):
        try:
            file_name = request.FILES.get("file_name")
            print(file_name)
            file = open("C:\\"+file_name, "r")
            content = file.read()
            print(content)
            file.close()

            # need to write logic here....
        except Exception as e:
            return sendresponse(
                data=str(e), message="Something went wrong", status_code=400
            )




class GetCallData(APIView):
    def get(self,request):
        try:
            call_list = Callhisory.objects.all().values()
            if len(Data) != 0:
                return sendresponse(
                    message="Successfully fetched data",
                    data=call_list,
                    status_code=200,
                )
            else:
                return sendresponse(
                        message="No data found",
                        status_code=400,
                    )
        
        except Exception as e:
            return sendresponse(
                data=str(e), message="Something went wrong", status_code=400
            )


class GetCallAggregateData(APIView):
    def get(self,request):
        try:
            data = request.GET.dict()# add filters here...
            call_list = Callhisory.objects.all(**data).values()
            if len(Data) != 0:
                return sendresponse(
                    message="Successfully fetched data",
                    data=call_list,
                    status_code=200,
                )
            else:
                return sendresponse(
                        message="No data found",
                        status_code=400,
                    )
        
        except Exception as e:
            return sendresponse(
                data=str(e), message="Something went wrong", status_code=400
            )






