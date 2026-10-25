#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 22:46:58 2021

@author: emidom
"""

# CIP3ServidorUDP.py
# Emplea conexión UDP
import socket

try :

    # Crea un UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # Conecta el socket al puerto
    # Puertos con dirección por encima de 1024 de lo contrario no permite la conexión
    # La dirección del servidor es la propia dirección IP del equipo
    
    address = '172.20.1.167'
    port = 5555
    buffer_size = 1024

    server_address = (address, port)
    print('Iniciando conexión UDP desde Servidor... ', server_address)
    sock.bind(server_address)


    while True:
     
        # Recibe los datos y los retransmite
        data, address = sock.recvfrom(buffer_size)
        print('Recibido... ', data.decode())
          
        if data.decode() == 'salir':
            sock.close()
            break
        else :
            print('Enviando datos al cliente... ', data.decode())

    
except :
     # Cierra la conexión
     sock.close()






    