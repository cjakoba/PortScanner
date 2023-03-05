# Author: Christian Jakob
# Created: 05 Mar 2023
# DESCRIPTION

import argparse
import sys, time
from socket import *


class PortScanner:
    def __init__(self, host, start_port, end_port, protocol):
        self.host = host
        self.start_port = start_port
        self.end_port = end_port
        self.protocol = protocol.lower()


    def scan_ports(self) -> None:
        # setup
        print(f"Scanning: {self.host} from port: {str(self.start_port)} to port: {str(self.end_port)}")

        # Creating a socket
        try:
            if 'tcp' in self.protocol:
                pass
            elif 'udp' in self.protocol:
                clientSocket = socket(AF_INET, SOCK_DGRAM)

            clientSocket.settimeout(timeout)
        except:
            pass


        # Set the IP
        remote_ip = self.host
        print(f"Scanning IP address: {remote_ip}")

        # Scan Ports
        self.end_port += 1

        # Loop over range of ports trying to connect to them
        for port in range(self.start_port, self.end_port):
            if 'tcp' in self.protocol:
                pass
            elif 'udp' in self.protocol:
                clientSocket.sendto(b'test', (self.host, port))
                msg, serverAddress = clientSocket.recvfrom(1)
                print(len(msg))
            else:
                pass


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'Remote Port Scanner')
    parser.add_argument('--host', action = "store", dest = "host", default = "127.0.0.1")
    parser.add_argument('--start-port', action = "store", dest = "start_port", default = 1, type = int)
    parser.add_argument('--end-port', action = "store", dest = "end_port", default = 100, type = int)
    parser.add_argument('--protocol', action = "store", dest = "protocol", default = "TCP")
    given_args = parser.parse_args()
    host, start_port, end_port, protocol = given_args.host, given_args.start_port, given_args.end_port, given_args.protocol

    portscanner = PortScanner(host, start_port, end_port, protocol)
    portscanner.scan_ports()
            

