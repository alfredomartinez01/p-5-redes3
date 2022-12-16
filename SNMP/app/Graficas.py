import pygal

def graficar_paquetes():
    x_time = []
    in_packets = []
    i=0
    temp=0.0
    
    with open('resultados.txt', 'r') as f:
        for line in f.readlines():
            i=i+1
            line = eval(line)
            tiempo = line['Tiempo']
            paquetes = float(line['Fa0-0_In_uPackets'])
            if i==2:
                temp = paquetes-temp
                x_time.append(tiempo)
                in_packets.append(temp)
                i=0
            else:
                temp = paquetes
    
    line_chart = pygal.Line(x_label_rotation=25)
    line_chart.title = "R1 Fa2/0"
    line_chart.x_labels = x_time
    line_chart.add('Paq. entrada', in_packets)
    line_chart.render_to_file('/home/javatt/Desktop/SNMP/app/static/grafica_paquetes.svg')
    
def graficar_estado():
    x_time = []
    estado = []
    
    with open('estado.txt', 'r') as f:
        for line in f.readlines():
            line = eval(line)
            x_time.append(line['Tiempo'])
            estado.append(float(line['estado']))
    
    line_chart = pygal.StackedLine(height=300,fill=True,x_label_rotation=25)
    line_chart.title = "R1 Fa2/0"
    line_chart.x_labels = x_time
    line_chart.add('Conexion de la interfaz', estado)
    line_chart.render_to_file('/home/javatt/Desktop/SNMP/app/static/grafica_estado.svg')

