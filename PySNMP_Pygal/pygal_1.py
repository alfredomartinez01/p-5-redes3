#!/usr/bin/env python3

import pygal

x_time = []
out_octets = []
out_packets = []
in_octets = []
in_packets = []

with open('resultados.txt', 'r') as f:
    for line in f.readlines():
        # eval(line) lee cada linea como diccionario no como cadena
        line = eval(line)
        x_time.append(line['Tiempo'])
        out_packets.append(float(line['Fa0-0_Out_uPackets']))
        out_octets.append(float(line['Fa0-0_Out_Octet']))
        in_packets.append(float(line['Fa0-0_In_uPackets']))
        in_octets.append(float(line['Fa0-0_In_Octet']))

line_chart = pygal.Line()
line_chart.title = "R1 Fa0/0"
line_chart.x_labels = x_time
line_chart.add('Oct. salida', out_octets)
line_chart.add('Paq. salida', out_packets)
line_chart.add('Oct. entrada', in_octets)
line_chart.add('Paq. entrada', in_packets)
line_chart.render_to_file('pygal_ejemplo_2.svg')



