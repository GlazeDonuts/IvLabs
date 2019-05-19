#include<iostream>
using namespace std;

main()
{
  int findmax (int[],int);
  int a[10000];
  int ch;
  int c=0;
  cout<<"Enter Elements (-1 to terminate) :"<<endl<<"---------------------------------------"<<endl;

// Loop to Take in Array
  while(1)
  {
    cout<<"Enter Element : ";
    cin>>ch;
    if(ch==-1)
      break;
    else
    {
      a[c]=ch;
      c++;
    }
  }

  if(!a[0])
  {
    cout<<"\n Not Possible to Jump Through!!!"<<endl;
    exit(0);
  }

// Checking if there exists a blockage in the Array
// Blockage is when an element is followed by equal more number of zeroes than its value
  int cnt;
  int j,k;
  for(j=0;j<c;j++)
  {
    cnt=0;
    for(k=j;k<=j+a[j];k++)
    {
      if(!a[k])
      cnt++;
    }
    if(cnt==a[j])
    {
      cout<<"Can NOT proceed beyond Position : "<<j+1<<" i.e Element : "<<a[j]<<endl;
      exit(0);
    }
  }

  int b[c];
  int i=0,l=0;
  while(i<c)
  {
    b[l]=a[i];		//Storing the elements we jumped to, in another array
    if(i==c-1)
    	break;
    i=findmax(a,i);
    l++;
  }
  cout<<"Number of Jumps : "<<l<<"("<<b[0];
  for(i=1;i<l+1;i++)
  {
    cout<<"-->"<<b[i];
  }
  cout<<")";
}


// Function to find the element (in the present jumpable distance)
// which will lead to the furthest next jump
int findmax(int x[],  int j)
{
  int k;
  int max=-1;
  int maxind=-1;
  for(k=j+1;k<=j+x[j];k++)
  {
    if((x[k]+k)>max)
    {
      max=x[k]+k;
      maxind=k;
    }
  }
  return maxind;
}
