from pysnmp.entity.rfc3413.oneliner import cmdgen
from datetime import datetime
import time

def snmp_query():
    while(1):
        time.sleep(5)
        result = {}
        errorIndication, errorStatus, errorIndex, varBinds = cmdgen.CommandGenerator().getCmd(
            cmdgen.CommunityData('comunidad'),
            cmdgen.UdpTransportTarget(('192.168.0.254', 161)),
            '1.3.6.1.2.1.2.2.1.10.1'
        )

        if errorIndication:
            print(errorIndication)
            x=datetime.now().strftime('%I:%M:%S')
            result['Tiempo'] = x
            result['Fa0-0_In_uPackets'] = '0'
        else:
            if errorStatus:
                print('%s at %s' % (
                    errorStatus.prettyPrint(),
                    errorIndex and varBinds[int(errorIndex)-1] or '?'
                    )
                )
                x=datetime.now().strftime('%I:%M:%S')
                result['Tiempo'] = x
                result['Fa0-0_In_uPackets'] = '0'
            else:
                for name, val in varBinds:
                    x=datetime.now().strftime('%I:%M:%S')
                    result['Tiempo'] = x
                    result['Fa0-0_In_uPackets'] = str(val)

        with open('resultados.txt', 'a') as f:
            f.write(str(result))
            f.write('\n')
            f.close()


