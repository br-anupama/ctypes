#include<stdio.h>

struct Example{
	int length;
	char names[3][10];
	int sizes[4];
};

struct Classes{
	float paper_weight;
	struct Example EX [5];
	int num;
};

