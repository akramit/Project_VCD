#include <bits/stdc++.h>
using namespace std;

int main(){
	int d,n,i,j;
	n=15; d=2;
	vector<int> a={1,2,3,4,5,6,7,8,9,10,11,12,13,14,15};
	vector<vector<int> > subset;
	//cout<<"Enter subset size and n";
	//cin>>d>>n;
	int counter=0,pow_set=pow(2,n);
	while(counter<pow_set){
		//find set bits and insert
		vector<int> temp;
		for(j=0;j<n;j++){
			if(counter&(1<<j)){
				temp.push_back(a[j]);
			}
		}
		subset.push_back(temp);
		counter++;
	}

	cout<<"All subsets of S of size "<<endl;
	for(i=0;i<subset.size();i++){
		
		if(subset[i].size()>=0){
			cout<<"[ ";
			for(j=0;j<subset[i].size();j++){
				cout<<subset[i][j]<<" ";
			}
			cout<<"]";
			cout<<endl;
		}
	}


	return 0;
}
