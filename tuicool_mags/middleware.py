from proxy import PROXIES
from agents import AGENTS

class TuicoolHttpProxyMiddleware(object):
  def process_request(self,request,spider):
    proxy_str=""
    if len(proxy_str)!=0:
      try:
        request.mata["proxy"]=proxy_str
      except Exception,e:
        log.msg("Exception %s" % e,_level=log.CRITICAL)

  '''
    change request header nealy every time
  '''
  class TuicoolUserAgentMiddleware(object):
    def process_request(self,request,spider):
      agent="Mozilla/5.0 (Windows NT 6.1; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0"
      request.headers["User-Agent"]=agent
