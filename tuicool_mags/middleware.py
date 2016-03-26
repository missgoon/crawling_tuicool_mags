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
