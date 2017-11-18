#include<conio.h>
#include<stdlib.h>
#include<iomanip>
#include<iostream>

using namespace std;

struct CubicSpline
{
	double *x;	//Mang toa do x
	double *y;	//Mang toa do y
	double *e;
	double *f;
	double *g;
	double *r;
	double *w;
} cs;

void entry(struct CubicSpline cs , int &n )  // Ham nhap du lieu
{
	cout<<"Nhap toa do (x,y) cho cac vi tri: \n";
	for(int i=0;i<=n;i++)
	{
		cout<<"x"<<i<<" = ";
		cin>>cs.x[i];
		cout<<"y"<<i<<" = ";
		cin>>cs.y[i];
	}
}

void processing(struct CubicSpline cs , int &n)
{
	for(int k=1;k<n;k++)
	{
		cs.f[k] = 2*(cs.x[k+1]-cs.x[k-1]);
		cs.r[k] = 6*((cs.y[k+1] - cs.y[k])/(cs.x[k+1] - cs.x[k]) + (cs.y[k-1] - cs.y[k])/((cs.x[k] - cs.x[k-1])) );
		if(k>=1)
		{
			cs.e[k+1] = cs.x[k+1] - cs.x[k] ;
			cout<<"\n"<<cs.e[k];
		}
		if(k<n-1)
		{
			cs.g[k] = cs.x[k+1] - cs.x[k] ;
		}
	}
}

void print1(struct CubicSpline cs , int &n)
{
	cout<<"\nHam sau khi xu li cac gia tri trung gian : \n";
	cout<<"k"<<setw(5)<<"x"<<setw(5)<<"y"<<setw(10)<<"ek"<<setw(10)<<"fk"<<setw(10)<<"gk"<<setw(10)<<"rk";
	for(int k=0;k<=n;k++)
	{
		cout<<"\n";
		cout<<k<<setw(5)<<cs.x[k]<<setw(5)<<cs.y[k];
		if(k>1&&k<n)
		{
			cout<<setw(10)<<cs.e[k];
		}
		else
		{
			cout<<setw(10)<<"";
		}
		if(k>=1&&k<n)
		{
			cout<<setw(10)<<cs.f[k];
		}
		else
		{
			cout<<setw(10);
		}
		if(k>=1&&k<n-1)
		{
			cout<<setw(10)<<cs.g[k];
		}
		else
		{
			cout<<setw(10)<<"";
		}
		if(k>=1&&k<n)
		{
			cout<<setw(10)<<cs.r[k];
		}
		else
		{
			cout<<setw(10);
		}
	}
}

void findW(struct CubicSpline cs , int &n)
{
	
}

int main(){
	int n;
	struct CubicSpline cs;
	cout<<"Chuong trinh tim duong cong xap xi qua n diem su dung Cubic spline.";
	cout<<"\nSo diem duong cong di qua : ";
	cin>>n ;
	cs.x = (double *)malloc(n*sizeof(double));
	cs.y = (double *)malloc(n*sizeof(double));
	cs.e = (double *)malloc(n*sizeof(double)); 
	cs.f = (double *)malloc(n*sizeof(double));
	cs.g = (double *)malloc(n*sizeof(double));
	cs.r = (double *)malloc(n*sizeof(double));
	cs.w = (double *)malloc(n*sizeof(double));
	n=n-1;
	entry(cs,n);
	processing(cs,n);
	print1(cs,n);
	return 0;
}
