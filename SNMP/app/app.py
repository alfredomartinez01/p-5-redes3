from flask import Flask , render_template
import SNMPget,Graficas,os,Lectura,threading

comand= " python3 /home/javatt/Desktop/SNMP/app/Traps.py "
app= Flask(__name__)

@app.route("/")
def hello():
   hilo1 = threading.Thread(target=Lectura.imprime)
   hilo2 = threading.Thread(target=SNMPget.snmp_query)
   hilo1.start()
   hilo2.start()
   os.popen("sudo -S %s"%(comand), 'w').write("1532")
   return "Servidor corriendo"
   
@app.route("/graficas")
def grafica():
   Graficas.graficar_paquetes()
   Graficas.graficar_estado()
   return render_template("index.html")


if __name__ == '__main__':
   app.run()


