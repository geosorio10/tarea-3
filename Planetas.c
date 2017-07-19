#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>

int main(void){
  FILE *file;
  file=fopen("coordinates.csv","r");

  int len=250;
  char line_buffer[len];
  char *split_buffer;
  const char *delimiter;
  delimiter = ",";
  int i=0,j=0;
  while(fgets(line_buffer,len,file))
    {
      printf("LINE IS: %s", line_buffer);
      split_buffer=strtok(line_buffer, delimiter);

      while(split_buffer!=NULL)
	{
	  
	  printf("ITEM IN LINE: %s\n",split_buffer);
	  split_buffer=strtok(NULL,delimiter);
	  j+=1;	  
	}
      i+=1;
      
    }

  return 0;
}
