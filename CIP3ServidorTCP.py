#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""asasx
Created on Sat Oct  9 22:46:58 2021

@author: emidom
"""

# CIP3ServidorTCP.py
# Emplea conexión TCP


import socket

socket.Add

try: 

    
    # Crea un TCP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Conecta el socket al puerto
    # Puertos con dirección por encima de 1024 de lo contrario no permite la conexión
    # La dirección del servidor es la propia dirección IP del equipo
    
    address = '127.0.0.1'
    port = 5555
    buffer_size = 1024
    
    server_address = (address, port)
    print('Iniciando conexión TCP desde Servidor... ', server_address)
    sock.bind(server_address)
    
    sock.listen(1)
    
    while True:
        # Espera para conectar
        print('Esperando a una conexión... ')
        connection, client_address = sock.accept()
        
        print('Conexión desde... ', client_address)
    
        # Recibe los datos y los retransmite
        while True:
            data = connection.recv(buffer_size)
            print('Recibido... ', data.decode())
            if data.decode() == 'salir':
                sock.close()
                break
            else :
                print('Enviando datos al cliente... ', data.decode())
                connection.sendall(data)
                
except:
    # Cierra la conexión
    sock.close()
    connection.close()
 






    