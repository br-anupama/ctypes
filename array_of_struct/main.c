#include <unistd.h>
#include <stdio.h>
#include <sys/socket.h>
#include <stdlib.h>
#include <netinet/in.h>
#include <string.h>
#include "dummy.h"

#define PORT 8080


void display(struct Classes cl){
     printf("paper_weight = %f \n", cl.paper_weight);


     printf("Printing Example struct Data : \n");
     for(int i = 0; i < 5; i++){
	printf("===================== \n");
	printf("length %d \n", cl.EX[i].length);
	printf("names \n");
	for(int j = 0; j < 3; j++){
		printf("%s \n", cl.EX[i].names[j]);
	}

	printf("sizes \n");
	for(int k = 0; k < 4; k++){
		printf("%d \n", cl.EX[i].sizes[k]);
	}	
     }
     printf("num = %d \n", cl.num);
}

int main(int argc, char const *argv[])
{
    int server_fd, new_socket, valread;
    struct sockaddr_in address;
    int opt = 1;
    int addrlen = sizeof(address);
    char buffer[1024] = {0};
    struct Classes class;
  
    printf("server started listening ... \n");
    
    // Creating socket file descriptor
    if ((server_fd = socket(AF_INET, SOCK_STREAM, 0)) == 0)
    {
        perror("socket failed");
        exit(EXIT_FAILURE);
    }
      
    // Forcefully attaching socket to the port 8080
    if (setsockopt(server_fd, SOL_SOCKET, SO_REUSEADDR | SO_REUSEPORT,
                                                  &opt, sizeof(opt)))
    {
        perror("setsockopt");
        exit(EXIT_FAILURE);
    }
    address.sin_family = AF_INET;
    address.sin_addr.s_addr = INADDR_ANY;
    address.sin_port = htons( PORT );
      
    // Forcefully attaching socket to the port 8080
    if (bind(server_fd, (struct sockaddr *)&address, 
                                 sizeof(address))<0)
    {
        perror("bind failed");
        exit(EXIT_FAILURE);
    }
    if (listen(server_fd, 3) < 0)
    {
        perror("listen");
        exit(EXIT_FAILURE);
    }
   
    while(1){
    	if ((new_socket = accept(server_fd, (struct sockaddr *)&address, 
                       (socklen_t*)&addrlen))<0)
    	{
        	perror("accept");
        	exit(EXIT_FAILURE);
   	 }
    	valread = read( new_socket , (struct Example *)&class, 1024);
        display(class);
	printf("------------------------");
    }
    return 0;
}
