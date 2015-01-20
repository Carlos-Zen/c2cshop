import json
from pysimplesoap import client
from xml.dom import minidom
from common.setting import loc,uri

c = client.SoapClient(location=loc,action=uri)

class FromSoap:
    
    def __getattr__(self,seg):
        rst = lambda self=self,*args,**kwargs:c.call(seg,*args,**kwargs)

        return rst
    def call_func(self,seg,*args,**kwargs):
        print 'call_func seg ',seg,' args',args
        print 'call_func seg ',seg,' kwargs',kwargs
        return c.call(seg,(),**kwargs)
        