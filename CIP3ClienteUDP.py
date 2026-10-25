#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 23:04:38 2021

@author: emidom
"""
# CIP3ClienteUDP.py
# Emplea conexión UDP

import socket

try : 

    # La dirección loopback es 127.0.0.1
    # El puerto debe ser el mismo que el del servidor por encima de 1024 hasta 65535
    # El cliente tiene que tener la dirección IP del servidor
    address = '172.20.1.129'
    port = 8080
    buffer_size = 1024
    
    server_address = (address, port)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print('Cliente UDP... Conectado a Servidor: ',server_address)
    
    while True: 
           
        cmd = input("Pulsa intro para enviar el mensaje  o 'salir': ")
        
        if cmd == 'salir':
            sent = sock.sendto(cmd.encode(), server_address)
            sock.close()
            break
             	
        sent = sock.sendto(cmd.encode(), server_address)
        recibe, server  = sock.recvfrom(buffer_size)
        print("Recibido después de enviar: ", recibe.decode())
        
except :
    print("Saliendo")    
    sock.close()