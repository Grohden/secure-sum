import socket
import random
from security.diffie_hellman import calculate_key
from utils.constants import DATA_SIZE, ADDRESS, MAX_RANDOM, SHARED_BASE, SHARED_PRIME
from utils.sockets import send_msg, receive_message

tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def main():
    tcp_socket.bind(ADDRESS)
    tcp_socket.listen(1)

    print 'Socket listening at %s:%s' % ADDRESS
    while True:
        connection, client_address = tcp_socket.accept()
        secret_server_key = random.randint(0, MAX_RANDOM)

        server_diff_hellman = calculate_key(SHARED_BASE, SHARED_PRIME, secret_server_key)
        send_msg(connection, str(server_diff_hellman))
        b_value = receive_message(connection)

        shared_secret = calculate_key(b_value, SHARED_PRIME, secret_server_key)
        print "Shared key:", shared_secret


main()
