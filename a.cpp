#include<bits/stdc++.h>

using namespace std;
int maximum(vector<int> &p)
{
    int max = p[0];
    for(int i=1;i<p.size();i++)
    {
        if(p[i] > max)
            max = p[i];
    }
    return max;
}

int main()
{
    vector<int> profits = {35,30,25,20,15,12,5};
    vector<int> deadlines = {3,4,4,2,3,1,2};
    int i;
    int max = maximum(deadlines);
    vector<int> slots;
    slots.assign(max, 0);
    vector<bool> fill;
    fill.assign(max,false);
    int c = 0;
    for(i=0;i<profits.size();i++)
    {
        for(int j=deadlines[i];j>=1;j--)
        {
            if(fill[j-1] == false)
            {
                slots[j-1] = i;
                fill[j-1] = true;
                c++;
                break;
            }
            if(c==max)
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
        pro += profits[slots[i]];
    }
    cout<<"Final profit: " <<pro <<'\n';
    return 0;
}