from pyzabbix import ZabbixAPI
from pprint import pprint

zapi = ZabbixAPI("http://10.10.10.108")
zapi.login("zapper", "zapper")
print "Connected to Zabbix API Version %s" % zapi.api_version()

for h in zapi.host.get(output="extend"):
    pprint(h)
