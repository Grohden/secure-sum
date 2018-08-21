import socket
import random

from security.aes import AESCipher
from Crypto.Cipher import AES
from security.diffie_hellman import calculate_key
from utils.constants import DATA_SIZE, ADDRESS, MAX_RANDOM, SHARED_BASE, SHARED_PRIME
from utils.sockets import receive_message, send_msg

secret_client_key = random.randint(0, MAX_RANDOM)
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def main():
    tcp_socket.connect(ADDRESS)

    first = input("Type the first number: ")
    second = input("Type the second number: ")

    client_diff_hellman = calculate_key(SHARED_BASE, SHARED_PRIME, secret_client_key)
    send_msg(tcp_socket, str(client_diff_hellman))
    a_value = receive_message(tcp_socket)

    shared_secret = calculate_key(a_value, SHARED_PRIME, secret_client_key)
    print "The diffie hellman key is ", shared_secret, ", but don't tell anyone pls"

    cipher = AESCipher(shared_secret)

    # Creates the encrypted message
    message = cipher.encrypt(str(first) + ":" + str(second))
    print "The message to send is ", message

    # Sends it to the server
    send_msg(tcp_socket, message)

    # Receives the message from the server
    response = receive_message(tcp_socket)
    print "The message received is ", response

    # Decrypt the message
    requested_sum = cipher.decrypt(response)
    print "Your sum is: ", requested_sum


main()
