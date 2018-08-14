import socket
import random

from security.diffie_hellman import calculate_key
from utils.constants import DATA_SIZE, ADDRESS, MAX_RANDOM, SHARED_BASE, SHARED_PRIME
from utils.sockets import receive_message, send_msg

secret_client_key = random.randint(0, MAX_RANDOM)
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def main():
    tcp_socket.connect(ADDRESS)

    client_diff_hellman = calculate_key(SHARED_BASE, SHARED_PRIME, secret_client_key)
    send_msg(tcp_socket, str(client_diff_hellman))
    a_value = receive_message(tcp_socket)

    shared_secret = calculate_key(a_value, SHARED_PRIME, secret_client_key)
    print "Shared key:", shared_secret


main()
