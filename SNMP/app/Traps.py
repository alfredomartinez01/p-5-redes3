from pysnmp.entity import engine, config
from pysnmp.carrier.asyncore.dgram import udp
from pysnmp.entity.rfc3413 import ntfrcv

def traps():
    print("Analizando 192.168.2.1 en el puereto 162")
    snmpEngine = engine.SnmpEngine()

    config.addTransport(
        snmpEngine, udp.domainName + (1,),
        udp.UdpTransport().openServerMode(('192.168.0.10', 162))
    )

    config.addV1System(snmpEngine, 'vis_comunidad_read', 'comunidad')

    def cbFun(snmpEngine, stateReference, contextEngineId, contextName, varBinds, cbCtx):
        valor = str((varBinds.pop())[-1])
        with open('status.txt', 'w') as f:
            f.write(valor)
            f.close()
        print(valor)

    ntfrcv.NotificationReceiver(snmpEngine, cbFun)
    snmpEngine.transportDispatcher.jobStarted(1)  

    try:
        snmpEngine.transportDispatcher.runDispatcher()
    except:
        snmpEngine.transportDispatcher.closeDispatcher()
        raise

traps()