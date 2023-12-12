import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

GPIO.setwarnings(False)

leitor = SimpleMFRC522()

texto = "12 / 32"
# dois ultimos digitos do numero usp de cada aluno

print ("Aproxime a tag do leitor para gravar")

leitor.write(texto)

print("Concluído")

#Gabriel Aguilar Soares de Melo  N 11915432
#João Pedro Suzuki de Figueiredo N 11800712
