# -*- coding: utf-8 -*-
from paddingoracle import BadPaddingException, PaddingOracle
from base64 import b64encode, b64decode
from urllib import quote, unquote
import requests
import socket
import time


class PadBuster(PaddingOracle):
    def __init__(self, **kwargs):
        super(PadBuster, self).__init__(**kwargs)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect(("localhost",1337))

    def oracle(self, data, **kwargs):
        print("Trying: {}".format(b64encode(data)))

        r = ''
        while 1:
            try:
            	if r == '':
                    self.sock.send(b64encode(data) + '\n')
                time.sleep(0.1)
                r += self.sock.resv(1024)
                if not '\n' in r:
                	continue
                if 'error' in r or 'Padding' in r: 
                	raise BadPaddingException
                else:
                	return
            except (socket.error):
                logging.exception('Retrying request in %.2f seconds...',
                                  self.wait)
                time.sleep(self.wait)
                continue


if __name__ == '__main__':
    import logging
    import sys

    
    logging.basicConfig(level=logging.DEBUG)

    encrypted_value = 'irRmWB7oJSMbtBC4QuoB13DC08NI06MbcWEOc94q0OXPbfgRm+l9xHkPQ7r7NdFjo6hSo6togqLYITGGpPsXdg=='
    padbuster = PadBuster()

    value = padbuster.decrypt(b64decode(encrypted_value), block_size=16, iv=bytearray(16))

    print('Decrypted somecookie: %s => %r' % (value))

