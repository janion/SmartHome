import json
from socket import *

import smart_home.common.Constants as Constants


class NewDeviceAnnouncer:

    def connect_to_server(self):
        response = None
        while response is None:
            self._anounce_ip_to_server()
            response = self._await_server_response()

        return response

    def _anounce_ip_to_server(self):
        # Send UDP broadcast to give IP address to server
        print("Requesting server connection")
        cs = socket(AF_INET, SOCK_DGRAM)
        cs.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        cs.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
        cs.sendto(str.encode(self._create_json()), ('255.255.255.255', Constants.UDP_PORT_NUMBER))
        cs.close()

    def _create_json(self):
        data = {Constants.JSON_IP_ADDRESS: gethostbyname(gethostname()), Constants.JSON_CLIENT_NAME: "NAME"}
        return json.dumps(data)

    def _await_server_response(self):
        try:
            # Await the server to give its IP address
            addr = getaddrinfo('0.0.0.0', Constants.SERVER_CONNECTION_PORT_NUMBER)[0][-1]

            s = socket()
            s.settimeout(10)
            s.bind(addr)
            s.listen(1)

            print('Awaiting server response')

            cl, connected_addr = s.accept()
            data = cl.recv(256).decode()
            cl.close()

            json_data = json.loads(data)
            ip = json_data[Constants.JSON_IP_ADDRESS]
            name = json_data[Constants.JSON_CLIENT_NAME]
            print('Server connected from', ip)

            return ip, name
        except timeout:
            pass
