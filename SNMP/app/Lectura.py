import threading,time
from datetime import datetime

def imprime():
   i = 0
   while(1):
      time.sleep(3)
      with open('status.txt', 'r') as f:
         estado = f.read()
         f.close()

      result = {}
      x=datetime.now().strftime('%I:%M:%S')
      result['Tiempo'] = x
      if estado == 'up':
         result['estado'] = '1'
      else: 
         result['estado'] = '0'
      
      if i == 40:
         with open('estado.txt', 'w') as f:
            f.write(str(result))
            f.write('\n')
            f.close()
         i = 0
      else:
         with open('estado.txt', 'a') as f:
            f.write(str(result))
            f.write('\n')
            f.close()
         i= i+1

if __name__ == '__main__':
   hilo = threading.Thread(target=imprime)
   hilo.start()