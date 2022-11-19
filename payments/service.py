from dataclasses import dataclass
from .models import Order
from sslcommerz_python.payment import SSLCSession
from decimal import Decimal

@dataclass
class SslEcommerceProcess:
    obj : Order

    def __call__(self) -> dict:
        data = {}
        mypayment = SSLCSession(sslc_is_sandbox=True, sslc_store_id='arbre6373f11aa43c5', sslc_store_pass='arbre6373f11aa43c5@ssl')
        mypayment.set_urls(success_url='http://127.0.0.1:8000/status/', fail_url='http://127.0.0.1:8000/status/', cancel_url='http://127.0.0.1:8000/status/', ipn_url='http://127.0.0.1:8000/status/')
        mypayment.set_product_integration(total_amount=Decimal(self.obj.total_price), currency='BDT', product_category='Laptop', product_name=self.obj.product, num_of_item=1, shipping_method='YES', product_profile='None')
        mypayment.set_customer_info(name='sabbir ahemd', email='sabbirdev45@email.com', address1='demo address', address2='demo address 2', city='Dhaka', postcode='1207', country='Bangladesh', phone='01758514752')
        mypayment.set_shipping_info(shipping_to='demo customer', address='demo address', city='Dhaka', postcode='1209', country='Bangladesh')
        mypayment.set_additional_values(value_a=self.obj.id)
        response_data = mypayment.init_payment()
        data['url'] = response_data['GatewayPageURL']
        return data



@dataclass
class RedirectURLProcess:
    requests_data : dict
    def __call__(self) -> dict:
        data = {}
        if self.requests_data.get('status') == "VALID":
            order = Order.objects.filter(id=self.requests_data.get('value_a')).first()
            order.status = "success"
            order.payment_status = "success"
            order.trans_id = self.requests_data.get('tran_id')
            data['url'] = 'http://localhost:3000/status-success/'
            data['status'] = 'valid'

        if self.requests_data.get('status') == "FAILED":
            order = Order.objects.filter(id=self.requests_data.get('value_a')).first()
            order.payment_status = "faild"
            order.trans_id = self.requests_data.get('tran_id')
            data['url'] = 'http://localhost:3000/status-failed/'
            data['status'] = 'failed'

        if self.requests_data.get('status') == "CANCELLED":
            order = Order.objects.filter(id=self.requests_data.get('value_a')).first()
            order.payment_status = "cancel"
            order.trans_id = self.requests_data.get('tran_id')
            data['url'] = 'http://localhost:3000/status-cancel/'
            data['status'] = 'cancel'

        order.save()
        
        return data