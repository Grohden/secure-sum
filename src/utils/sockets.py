import struct


def send_msg(tcp_socket, msg):
    # Prefix each message with a 4-byte length (network byte order)
    msg = struct.pack('>I', len(msg)) + msg
    tcp_socket.sendall(msg)


def receive_message(tcp_socket):
    # Read message length and unpack it into an integer
    raw_msg_len = receive_value(tcp_socket, 4)
    if not raw_msg_len:
        return None
    msg_len = struct.unpack('>I', raw_msg_len)[0]
    # Read the message data
    return receive_value(tcp_socket, msg_len)


def receive_value(tcp_socket, n):
    # Helper function to recv n bytes or return None if EOF is hit
    data = b''
    while len(data) < n:
        packet = tcp_socket.recv(n - len(data))
        if not packet:
            return None
        data += packet
    return data
