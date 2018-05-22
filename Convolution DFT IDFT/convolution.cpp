#include<bits/stdc++.h>
using namespace std;
int main() {
	int xn, hn;
	cout<<"Enter the no. of values of x[n]: ";
	cin>>xn;
	int x_n[xn], pos_x_n[xn];
	cout<<"Enter the values of x[n]\n";
	for(int i=0;i<xn;i++)
		cin>>x_n[i];
	cout<<"Enter the n of x[n]\n";
	for(int i=0;i<xn;i++)
		cin>>pos_x_n[i];

	cout<<"Enter the no. of values of h[n]: ";
	cin>>hn;
	int h_n[hn], pos_h_n[hn];
	cout<<"Enter the values of h[n]\n";
	for(int i=0;i<hn;i++)
		cin>>h_n[i];
	cout<<"Enter the n of h[n]\n";
	for(int i=0;i<hn;i++)
		cin>>pos_h_n[i];
	

	vector<int> y_n;
	vector<int> pos_y_n;

	for(int i=0;i<xn;i++) {
		for(int j=0;j<hn;j++) {
			y_n.push_back(x_n[i] * h_n[j]);
			pos_y_n.push_back(pos_x_n[i] + pos_h_n[j]);
		}
	}

	cout<<endl;

	map<int, int> final;

	for(int i=0;i<pos_y_n.size();i++) {
		final[pos_y_n[i]] += y_n[i];
	}

	cout<<"Values of y[n] :\n";
	for (map<int, int>::iterator i = final.begin(); i != final.end(); ++i) {
		cout<<i->second<<" ";		
	}

	cout<<"\nPosition of y[n]"<<endl;
	for (map<int, int>::iterator i = final.begin(); i != final.end(); ++i) {
		cout<<i->first<<" ";		
	}
	cout<<"\n";
}