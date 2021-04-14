#include"functions.h"

//All Required functions
void print(vector<string> s){//Done
	for(int i=0;i<s.size();i++)
			cout<<s[i]<<" ";
	cout<<endl;
}

int binary_val(string x){//Done
	int bin=0,i;
	while(i<x.size()){
		bin=2*bin+x[i]-'0';
		i++;
	}
	return bin; 
}

vector<string> generate_Universe(int n){ //Done
	vector<string> universe;
	int mx=pow(2,n)-1,count=0;
	//cout<<mx;
	while(count<=mx){
		string x="";
		for(int j=0;j<n;j++){
			x.append(to_string((count>>j) & 1));
		}
		//cout<<x<<endl;
		reverse(x.begin(),x.end());
		universe.push_back(x);
		count++;
	}
	return universe;
}
vector<string> set_intersect(vector<string> S, vector<string> T){ //Done
	vector<string> S_int_T;
	sort(S.begin(),S.end());
	sort(T.begin(),T.end());
	for(int i=0;i<S.size();i++){
		for(int j=0;j<T.size();j++){
			if(S[i]==T[j])
					S_int_T.push_back(S[i]);
		}
	}

	return S_int_T;
}

vector<vector<string>> Intersection_F_S(vector<vector<string>> F, vector<string> S){//Done
	vector<vector<string>> F_int_S;
	for(int i=0;i<F.size();i++){
		F_int_S.push_back(set_intersect(F[i],S));
	}
	
	//Remove duplicates from F_int_S
	for(int i=0;i<F_int_S.size();i++){
		for(int j=i+1;j<F_int_S.size();j++){
			if(compare_set(F_int_S[i],F_int_S[j])){
				F_int_S.erase(F_int_S.begin()+j);
				j--;
			}
		}
	}
	return F_int_S;
}
bool compare_set(vector<string> t,vector<string> u){//Done
	if(t.size()!=u.size())
			return false;
	sort(t.begin(),t.end());
	sort(u.begin(),u.end());
	for(int i=0;i<t.size();i++){
		if(t[i]!=u[i])
			return false;
	}
	return true;
}
bool compare_family_sets(vector<vector<string>> T, vector<vector<string>> U){
	int flag=0;
	if(T.size()!=U.size())
			return false;
	for(int i=0;i<T.size();i++){
		flag=0;
		for(int j=0;j<U.size();j++){
			
			if(compare_set(T[i],T[j])){
				flag=1;
				break;
			}
		}
		if(flag==0)
			return false;
	}
	return true;
}
int count_set_bits(int a){ //Done
	int count=0;
	while(a){
		if(a&1)
			count++;
		a=a>>1;
	}
	return count;
}

vector<vector<string>> generate_subset_size_d(vector<string> a,int d){ //Done
	int j,count=0,pow_n=pow(2,a.size()),n=a.size();
	vector<vector<string>> all_subset_size_d;

	while(count<pow_n){
		if(count_set_bits(count)!=d){
			count++;
			continue;
		}
		vector<string> temp;
		for(j=0;j<n;j++){
			if(count & (1<<j))	
				temp.push_back(a[j]);
		}
		all_subset_size_d.push_back(temp);
		count++;
	}
	return all_subset_size_d;
}

vector<vector<string>> getPowerSet(vector<string> s){//Done
	vector<vector<string>> powerSet_S;
	for(int i=0;i<=s.size();i++){
			vector<vector<string>> temp;
			temp=generate_subset_size_d(s,i);
			for(int j=0;j<temp.size();j++)
				powerSet_S.push_back(temp[j]);
	}
	return powerSet_S;
}


int main(){

	int n,d,flag_shattered=0;
	vector<string> shattered_set;
	cout<<"Enter the size of the universe: "<<endl;
	cin>>n;
	vector<string> Universe=generate_Universe(n);
	//Threshold family
	/*vector<vector<string>> F={{"001","010","100","011","110","101","111"},
	{"001","010","100","011","110","101","111"},
	{"011","110","101","111"},
	{"111"}};*/

	//alt(f) <= 1 family
	vector<vector<string>> F={
		{},{"000","001","010","100","011","110","101","111"},{"111"},{"011","111"},
		{"110","111"},{"011","110","111"},{"101","111"},{"011","101","110","111"},
		{"011","101","111"},{"101","110","111"},{"001","011","101","111"},
		{"001","011","101","110","111"},{"010","011","110","111"},
		{"010","011","101","110","111"},{"100","101","110","111"},
		{"100","101","110","011","111"},{"001","010","011","110","101","111"},
		{"001","100","011","101","110","111"},{"010","100","011","101","110","111"},
		{"001","010","100","011","101","110","111"},
		////////////////// Negation of Montone////////
		{"000","001","010","100","011","101","110"},{"000","001","010","100","101","110"},
		{"000","001","010","100","011","101"},{"000","001","010","100","101"},{"000","001","010","100","011","110"},{"000","001","010","100"},
		{"000","001","010","100","110"},{"000","001","010","100","011"},{"000","010","100","110"},
		{"000","010","100"},{"000","001","100","101"},
		{"000","001","100"},{"000","001","010","011"},
		{"000","001","010"},{"000","100"},
		{"000","010"},{"000","001"},
		{"000"}
	};
	// Write to a file
	//freopen("output.txt","w",stdout);
	for(d=1;d<=Universe.size();d++){
		vector<vector<string>> set_size_d=generate_subset_size_d(Universe,d);
		for(int j=0;j<set_size_d.size();j++){
			flag_shattered=0;
			//Obtain F_int_S
			vector<string> S=set_size_d[j];
			vector<vector<string>> powerSet_S=getPowerSet(S);
			vector<vector<string>> F_int_S=Intersection_F_S(F,S);
			if(compare_family_sets(F_int_S,powerSet_S)==1){
				flag_shattered=1;
				shattered_set=S;
				/*print the shattered set
				cout<<"Shattered Set is ";
				print(shattered_set);
				cout<<endl;*/ 
				break;
			}
		}
		if(flag_shattered==0)
			break;
	}
	
	cout<<"VC-dim= "<<d-1<<endl;
	cout<<"Shattered Set is ";
	print(shattered_set);
	cout<<endl; 
	return 0;
}