from flask import Flask
from pysnmp.entity.rfc3413.oneliner import cmdgen
import datetime


app = Flask(__name__)


def snmp_query(host, community, oid):
    errorIndication, errorStatus, errorIndex, varBinds = cmdGen.getCmd(
        cmdgen.CommunityData(community),
        cmdgen.UdpTransportTarget((host, 161)),
        oid
    )
    
    # Revisamos errores e imprimimos resultados
    if errorIndication:
        print(errorIndication)
    else:
        if errorStatus:
            print('%s at %s' % (
                errorStatus.prettyPrint(),
                errorIndex and varBinds[int(errorIndex)-1] or '?'
                )
            )
        else:
            for name, val in varBinds:
                return(str(val))

@app.route("/")
def escuchar():
    with open('./resultados.txt', 'a') as f:
        f.write(str(snmp_query("192.168.0.10", "comunidad", "1.3.6.1.2.1.2.2.1.10.1")))
        f.write('\n')