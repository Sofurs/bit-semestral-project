#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

int main(int argc, char** argv);

char secret_flag[17];

void create_flag() {
  strcpy(secret_flag, "SecretFlagForBIT");
}

void unreachable() {
  printf("This is from an unreachable function!\n");
}

void vulnerable_function() {
  char name[128];
  char surname[128];

  read(0, name, 1000);
  printf(name);
  read(0, surname, 1000);
  printf(surname);
}

int main(int argc, char** argv) {
  create_flag();
  vulnerable_function();
  return 0;
}
