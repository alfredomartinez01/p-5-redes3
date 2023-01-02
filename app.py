from flask import Flask, jsonify
from pysnmp.entity.rfc3413.oneliner import cmdgen
import datetime

from pysnmp.entity import engine, config
from pysnmp.carrier.asyncore.dgram import udp
from pysnmp.entity.rfc3413 import ntfrcv
import threading

app = Flask(__name__)


def snmp_query(host, community, oid):
    errorIndication, errorStatus, errorIndex, varBinds = cmdgen.CommandGenerator().getCmd(
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
def iniciar():
    snmp_query("192.168.0.254", "comunidad", "1.3.6.1.2.1.2.2.1.10.1")
    # threading.Thread(target=trampa, args=('192.168.0.10', 'comunidad', 'vis_comunidad_read'))
    trampa('192.168.0.10', 'comunidad', 'vis_comunidad_read')
    return "Servidor corriendo"

def trampa(host, comunidad, vista):
    snmpEngine = engine.SnmpEngine()

    config.addTransport(
        snmpEngine, udp.domainName + (1,),
        udp.UdpTransport().openServerMode((host, 162))
    )

    config.addV1System(snmpEngine, vista, comunidad)

    def cbFun(snmpEngine, stateReference, contextEngineId, contextName, varBinds, cbCtx):
        valor = str((varBinds.pop())[-1])
        with open('status.txt', 'w') as f:
            f.write(valor+"\n")
            f.close()
        print(valor)

    ntfrcv.NotificationReceiver(snmpEngine, cbFun)
    snmpEngine.transportDispatcher.jobStarted(1)  

    try:
        snmpEngine.transportDispatcher.runDispatcher()
    except:
        snmpEngine.transportDispatcher.closeDispatcher()
        raise