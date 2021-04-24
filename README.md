# Simple FTP Server and Client
Blue Bayani (kbayani@csu.fullerton.edu)</br>
Brian Edwards (brian_edwards@csu.fullerton.edu)</br>
Vincent Lee (lee.v3798@csu.fullerton.edu)</br>

Programming language used: Python</br>

## How to execute the program: </br>
Invoke the server using: ```python3 server.py <PORT>``` </br>
On a seperate window, invoke the client using: ```python3 client.py <SERVER MACHINE> <PORT>```</br>

**NOTE: The client and server port numbers should match.**</br>
_**EXAMPLE:**_</br>
> ```python3 server.py 12000```</br> 
> ```python3 client.py <your ip address> 12000``` </br> 
***Note: If your IP address is not working, try 127.0.0.1 instead

</br>

#### Accepted Commands:</br>
- ```ftp> get <FILE NAME>``` :  downloads <FILE NAME> from the server</br>
- ```ftp> put <FILE NAME>``` :  uploads <FILE NAME> from the client to the server</br>
- ```ftp> ls```         :  lists fils on the server</br>
- ```ftp> quit```      :  disconnects from the server and exits</br>
