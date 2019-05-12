#include<iostream>
using namespace std;

static int cnt=0;


// Structure to encapsulate segment length and price together
struct lenpr
{
    int len;
    int pr;
};


// Search function to search for the price of a given segment length in array of lengths and prices
// If 2 prices are provided for the same segment then the higher price is used
int searchpr(int a,lenpr x[])
{
    int flag=0;
    int i;
    int price =0;
    for(i=0;i<cnt;i++)
    {
        if((a==x[i].len)&&(x[i].pr>price))
        {
            flag=1;
            price=x[i].pr;
        }
    }
	return price;
}


// A utility function to calculate price of given partition
int findval(int p[], int n,lenpr x[])
{
    int i;
    int val=0;
    for (int i = 0; i < n; i++)
    {
        val+=searchpr(p[i],x);
    }
    return val;
}


//Function to find partition with max value and to return the max value
int maxval(int n,lenpr x[])
{
    int p[n]; 		// An array to store a partition
    int k = 0;	 	// Index of last element in a partition
    p[k] = n;  		// Initialize first partition as number itself
    int max=0;		//To store the max revenue
    
    
    // This loop first calculates the value of current partition, compares it with current max value, then generates next partition
    // The loop stops when the last partition (all 1s) is reached
    while (true)
    {
        // Find value of current partition and compare with max
        if(max<=(findval(p, k+1,x)))
        max=findval(p,k+1,x);

        // Generate next partition

        /*Find the rightmost non-one value in p[]. Also, update the rem_val so that we know how much value can be accommodated*/
        int rem_val = 0;
        while (k >= 0 && p[k] == 1)
        {
            rem_val += p[k];
            k--;
        }

        // if k < 0, all the values are 1 so there are no more partitions
        if (k < 0)  break;

        // Decrease the p[k] found above and adjust the rem_val
        p[k]--;
        rem_val++;


        // If rem_val is more, then the sorted order is violated.  Divide
        // rem_val in different values of size p[k] and copy these values at different positions after p[k]
        while (rem_val > p[k])
        {
            p[k+1] = p[k];
            rem_val = rem_val - p[k];
            k++;
        }

        // Copy rem_val to next position and increment position
        p[k+1] = rem_val;
        k++;
    }
    return max;
}





main()
{
	int n,c,j=0;
	cout<<"\nEnter Length of Rod : ";
	cin>>n;
    lenpr x[100*n];
    cout<<"\nEnter Segment Lengths and Prices(enter -1 to terminate)"<<endl<<"---------------------------------------------------";
    while(1)
    {
    	len : cout<<"\nEnter Length : ";  // Labelling the line
        cin>>c;
        if(c==-1)
        break;
        else if (c>n)
        {
        	cout<<"\nINVALID LENGTH (ignored)";
        	goto len;
		}
        else
        {
            cnt++;
            x[j].len=c;
            cout<<"Enter Price : ";
            cin>>c;
            x[j].pr=c;
            cout<<endl;
            j++;
        }
    }

	int maxval(int,lenpr[]);
	int ans = maxval(n,x);
    cout<<"\nMaximum Possible value is : "<<ans;
}
