#include<bits/stdc++.h>
using namespace std;

int main(){
    int n,x;
    cin >> n >> x;
    int y = (x-1) / n ;
    cout << char('A'+y) << endl;
}