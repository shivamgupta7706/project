#define pi 3.141592653589793238462643383279
#include<bits/stdc++.h>
using namespace std;
int main() {
	int n;
	cout<<"Enter the value of N: ";
	cin>>n;

	vector<complex<float> > x;

	cout<<"Enter the value of x[n] in form 'a + ib' as 'a b' \n";
	float a, b;
	for(int i=0;i<n;i++) {
		cin>>a>>b;
		complex<float> temp(a,b);
		x.push_back(temp);
	}

	cout<<"Signal is as folows: \n";
	for(int i=0;i<x.size();i++) {
		cout<<"x["<<i<<"] = "<<real(x[i])<<" + "<<imag(x[i])<<"j\n";
	}

	complex<float> W(cos(2*pi/n),-sin(2*pi/n));

	vector<vector<complex<float> > > matrix;

	for(int i=0;i<n;i++) {
		vector<complex<float> > temp;
		for(int j=0;j<n;j++) {
			temp.push_back(pow(W, i*j));
		}
		matrix.push_back(temp);
	}

	vector<complex<float> > DFT;

	for(int i=0;i<n;i++) {
		complex<float> temp_sum(0,0);
		for(int j=0;j<n;j++) {
			temp_sum += matrix[i][j] * x[j];
		} 
		DFT.push_back(temp_sum);
	}

	cout<<"DFT of the following signal is as follows:\n";
	for(int i=0;i<n;i++){
		cout<<"X["<<i<<"] = "<<real(DFT[i])<<" + "<<imag(DFT[i])<<"j"<<endl;
	}



}