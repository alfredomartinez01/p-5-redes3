#!/usr/bin/env/python3

from pysnmp.entity.rfc3413.oneliner import cmdgen

cmdGen = cmdgen.CommandGenerator()

system_name = '1.3.6.1.2.1.1.5.0'
system_uptime = '1.3.6.1.2.1.1.3.0'

errorIndication, errorStatus, errorIndex, varBinds = cmdGen.getCmd(
    cmdgen.CommunityData('secreta'),
    cmdgen.UdpTransportTarget(('192.168.1.1', 161)),
    system_name,
    system_uptime
)

# Revisamos errores e imprimimos la salida
if errorIndication:
    print(errorIndication)
else:
    if errorStatus:
        print('%s en %s' % (
            errorStatus.prettyPrint(),
            errorIndex and varBinds[int(errorIndex)-1] or '?'
            )
        )
    else:
        for name, val in varBinds:
            print('%s = %s' % (name.prettyPrint(), str(val)))

