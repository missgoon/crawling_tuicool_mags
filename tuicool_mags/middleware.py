# -*- coding: utf-8 -*-
class TuicoolHttpProxyMiddleware(object):
  def process_request(self,request,spider):
    proxy_str="http://54.223.78.5:80"
    if len(proxy_str)!=0:
      try:
        request.meta["proxy"]=proxy_str
      except Exception,e:
      	print(e)
        print("proxy is error................................")

  '''
    change request header nealy every time
  '''
class TuicoolUserAgentMiddleware(object):
  def process_request(self,request,spider):
    agent="Mozilla/5.0 (Windows NT 6.1; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0"
    request.headers["User-Agent"]=agent
