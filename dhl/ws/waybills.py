from .common import WSCommon
from ..helpers import shipping_guide


class DHLShipmentValidation(WSCommon):

    url = 'http://xmlpitest-ea.dhl.com/XMLShippingServlet'

    def __init__(self, service_name, **kwargs):
        super(DHLShipmentValidation, self).__init__(service_name, **kwargs)

    def xml_request(self, data):
        data['site_id'] = self.site_id
        data['password'] = self.password
        data['account_number'] = self.account_number
        return shipping_guide(data)

    def request(self):
        xml_request = self.xml_request(self.kwargs)
        print 'pp'
        print xml_request
        response = self.requests.post(self.url, data=xml_request)
        print 'bb'
        print response._content
        try:
            res_dict = self.jxmlease.parse(response._content)
        except:
            res_dict = {}
        return xml_request, res_dict
