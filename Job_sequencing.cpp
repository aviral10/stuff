#include<bits/stdc++.h>

using namespace std;
int maximum(vector<int> &p) //Maximum in the array
{
    int max = p[0];
    for(int i=1;i<p.size();i++)
    {
        if(p[i] > max)
            max = p[i];
    }
    return max;
}

void simult_sort(vector<int> &a, vector<int> &b) //Sorting array b according to array a(Descending)
{
    int i,j,key,temp;
    for(i=0;i<a.size();i++)
    {
        key = i;
        for(j=i+1;j<a.size();j++)
        {
            if(a[j] > a[key])
                key = j;
        }
        temp = a[i];
        a[i] = a[key];
        a[key] = temp;
        temp = b[i];
        b[i] = b[key];
        b[key] = temp;
    }

}
int main()
{
    vector<int> profits = {35,30,25,20,15,12,5};
    vector<int> deadlines = {3,4,4,2,3,1,2};
    
    simult_sort(profits, deadlines);    //So array starts with max profit

    int i, max = maximum(deadlines);
    
    vector<int> slots;                  //result array to store indices of jobs
        slots.assign(max, 0);       
    vector<bool> fill;                  //all slots available 
        fill.assign(max,false);
    
    int c = 0;
    for(i=0;i<profits.size();i++)
    {
        for(int j=deadlines[i];j>=1;j--)
        {
            if(fill[j-1] == false)      //Checking if that slot is available
            {
                slots[j-1] = i;
                fill[j-1] = true;       //making that slot unavailable
                c++;
                break;                  
            }
            if(c==max)                  //Checking if all slots are filled up
                break;
        }
        if(c==max)
            break;
    }
    int pro = 0;
    cout <<"Job sequence: " <<'\n';
    for(i=0;i<c;i++)
    {
        cout << "J" <<slots[i]+1 << " with profit of $"<<profits[slots[i]] <<'\n';
        pro += profits[slots[i]];       //Adding profit
    }
    cout<<"Final profit: " <<pro <<'\n';
    return 0;
}
