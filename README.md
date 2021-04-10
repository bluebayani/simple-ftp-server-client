# Simple FTP Server and Client

## Usage:</br>
Invoke the server using: ```python3 server.py <PORT>``` </br>

Invoke the client using: ```python3 client.py <SERVER MACHINE> <PORT>```</br>
EXAMPLE:</br>
```python3 client.py <your ip address> 12000``` </br> 
```python3 server.py 12000```</br> 
**NOTE: The client and server port numbers should match.**</br>

#### Client Commands:</br>
- ```ftp> get <FILE NAME>``` :  downloads <FILE NAME> from the server</br>
- ```ftp> put <FILE NAME>``` :  uploads <FILE NAME> from the client to the server</br>
- ```ftp> ls```         :  lists fils on the server</br>
- ```ftp> quit```      :  disconnects from the server and exits</br>
