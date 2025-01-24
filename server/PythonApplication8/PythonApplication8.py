
import socket
 
# Here we use localhost ip address
# and port number

LOCALHOST = "127.0.0.1"
PORT = 54321

# Calling server socket method with error handling
try:
    Server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket successfully created.")
except socket.error as e:
    print(f"Socket creation failed with error: {e}")
    exit(1)
    
    # Binding server with IP address and port number with error handling
try:
     Server.bind((LOCALHOST, PORT))
     print(f"Server bound to {LOCALHOST}:{PORT}")
except Exception as e:
    print(f"Binding failed: {e}")
    exit(1)

  
  # Start listening for incoming connections
try: 
    Server.listen(2)  # Allow up to 2 pending connections
    print("Server is listening for incoming connections...")
except Exception as e:
    print(f"Failed to start listening: {e}")
    exit(1)

print("Server started")
print("Waiting for client request..")

  # Here server socket is ready for getting input from the user



  # Accept a client connection
clientConnection, clientAddress = Server.accept()
print("Connected client :", clientAddress)
msg = ''
  

while True:
        try:
            # Receive data from the client
            data = clientConnection.recv(1024)

            # Decode and process the received data
            operation = data.decode('utf-8').strip()
            print(f"Received operation: {operation}")

            # Handle client disconnection request
            if operation.lower() == "over":
                print(f"Client {clientAddress} terminated the connection.")
                break

            # Parse the operation and compute the result
            try:
                operand1, operator, operand2 = operation.split()
                operand1 = float(operand1)
                operand2 = float(operand2)

                if operator == '+':
                    result = operand1 + operand2
                elif operator == '-':
                    result = operand1 - operand2
                elif operator == '*':
                    result = operand1 * operand2
                elif operator == '/':
                    if operand2 == 0:
                        result = "Error: Division by zero"
                    else:
                        result = operand1 / operand2
                else:
                    result = "Error: Unsupported operator"

                # Send the result back to the client
                clientConnection.send(str(result).encode('utf-8'))
            except ValueError:
                error_msg = "Error: Invalid format. Use 'operand operator operand'."
                print(error_msg)
                clientConnection.send(error_msg.encode('utf-8'))
            except Exception as e:
                error_msg = f"Error processing operation: {e}"
                print(error_msg)
                clientConnection.send(error_msg.encode('utf-8'))

        except Exception as e:
            print(f"Error during communication with {clientAddress}: {e}")
            break



# Close the client socket
try:
    clientConnection.close()
    print(f"Connection with {clientAddress} closed.")
except Exception as e:
    print(f"Error while closing client socket: {e}")
# Close the server socket (this will run if you stop the program manually)
try:
    Server.close()
    print("Server socket closed.")
except Exception as e:
    print(f"Error while closing the server socket: {e}")