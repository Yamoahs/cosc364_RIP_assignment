    #Create the sockets
    try:
        sender_in_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    except socket.error as e:
        print(str(e))
    try:
        sender_out_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    except socket.error as e:
        print(str(e))

    #Bind the sockets
    try:
        sender_in_socket.bind((HOST,sender_in_port))
    except socket.error as e:
        print(str(e))
    try:
        sender_out_socket.bind((HOST,sender_out_port))
    except socket.error as e:
        print(str(e))

    #Connect the sockets
    try:
        sender_out_socket.connect((HOST,chan_send_in_port))
    except socket.error as e:
        print(str(e))
