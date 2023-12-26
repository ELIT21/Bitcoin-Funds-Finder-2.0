import socket

def start_server():
    server_address = "2001:56b:de72:8400:f4a5:21d0:f059:2ebd"
    server_port = 5000

    with socket.socket(socket.AF_INET6, socket.SOCK_STREAM) as s:
        s.bind((server_address, server_port))
        s.listen()

        print(f"Server listening on {server_address}:{server_port}")

        while True:
            conn, addr = s.accept()
            with conn:
                print(f"Connection from {addr}")
                data = conn.recv(1024).decode('utf-8')
                if data:
                    print(f"Received data: {data}")
                    process_received_data(data)

def process_received_data(data):
    # Split the received data into individual values
    values = data.split(',')

    if len(values) == 4:
        private_key_wif = values[0]
        private_key_hex = values[1]
        bitcoin_address = values[2]
        balance = float(values[3])  # Convert balance to float

        # Save the data to the find.txt file
        with open('find.txt', 'a') as file:
            file.write("Received Data:\n")
            file.write(f"Private Key WIF: {private_key_wif}\n")
            file.write(f"Private Key Hex: {private_key_hex}\n")
            file.write(f"Bitcoin Address: {bitcoin_address}\n")
            file.write(f"Balance: {balance} BTC\n\n")

        # Perform other desired processing
        print("Processing received data:")
        print(f"Private Key WIF: {private_key_wif}")
        print(f"Private Key Hex: {private_key_hex}")
        print(f"Bitcoin Address: {bitcoin_address}")
        print(f"Balance: {balance} BTC")

        # Example: Save the data to a file or database, perform further actions, etc.

if __name__ == "__main__":
    start_server()