#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 23:04:38 2021

@author: emidom
"""

# CIP3ClienteTCP.py
# Emplea conexión TCP


import socket

try: 

    # La dirección loopback es 127.0.0.1
    # El puerto debe ser el mismo que el del servidor por encima de 1024 hasta 65535
    # El cliente tiene que tener la dirección IP del servidor
    
    address = '127.0.0.1'
    port = 5555
    buffer_size = 1024
    
    server_address = (address, port)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(server_address)
    print('Cliente TCP... Conectado a Servidor: ',server_address)
    
    while True: 
           
        cmd = input("Pulsa intro para enviar el mensaje  o 'salir': ")
        
        if cmd == 'salir':
            s.send(cmd.encode())
            s.close()
            break
                        	
        s.send(cmd.encode())
        recibe  = s.recv(buffer_size).decode()
        print("Recibido después de enviar: ", recibe)
        
except:
    print("Saliendo")    
    s.close()