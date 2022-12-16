#!/usr/bin/env python3

import pygal

line_chart = pygal.Pie()
line_chart.title = "Desgloce por protocolo"
line_chart.add('TCP', 15)
line_chart.add('UDP', 30)
line_chart.add('ICMP', 45)
line_chart.add('Otros', 10)
line_chart.render_to_file('pygal_ejemplo_3.svg')



