from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Order
from .serializers import OrderSerializer
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .service import SslEcommerceProcess, RedirectURLProcess
from django.http import HttpResponseRedirect
# Create your views here.

class Payment(APIView):
    def get(self, request, format=None):
        snippets = Order.objects.all()
        serializer = OrderSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data
        data['total_price'] = int(data['price']) * int(data['quantity'])
        data['status'] = 'due'
        serializer = OrderSerializer(data=data)

        if serializer.is_valid():
            obj = serializer.save()
            process_data = SslEcommerceProcess(obj)()            
            response = {
                "url" : process_data['url'],
                "data" : serializer.data
            }
            return Response(response, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@method_decorator(csrf_exempt, name='dispatch')
class Status(APIView):
    def post(self, request, format=None):
        data_dict = request.POST
        data = data_dict.dict()
        process_data = RedirectURLProcess(data)()
        response = process_data
        if response['status'] == 'valid':
            return HttpResponseRedirect(redirect_to=response['url'])
        if response['status'] == 'failed':
            return HttpResponseRedirect(redirect_to=response['url'])
        if response['status'] == 'cancel':
            return HttpResponseRedirect(redirect_to=response['url'])