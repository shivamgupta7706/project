#include<bits/stdc++.h>
using namespace std;
class Board
{
private:
	char s[15][16]={
	"               ",
	" G  G     Y  Y ",
	"               ",
	"               ",
	" G  G     Y  Y ",
	"               ",
	"               ",
	"               ",
	"               ",
	"               ",
	" R  R     B  B ",
	"               ",
	"               ",
	" R  R     B  B ",
	"               "};
	char temp[15][16]={"               ",
	                   "       ++      ",
	                   
	                   "       +       ",
	                   "       +       ",
	                   "       +       ",
	                   "       +       ",
	                   " +     -       ",
	                   " +++++- -+++++ ",
	                   "       -     + ","       +       ","       +       ","       +       ","       +       ","      ++       ","               "};
public:
	Board()
	{
	}
	vector<int> dieroll()
	{
		vector<int>v;
		int l=1;
		while(l)
		{
			int k=1+rand()%6;
			v.push_back(k);
			if(k==6)l=1;
			else l=0;
		}
		return v;
	}
	void display()
	{
		for(int i=0;i<15;i++)
			cout<<s[i]<<endl;
		for(int i=0;i<15;i++)
			cout<<temp[i]<<endl;
	}
};

class goti:public Board
{   
 public:
	int home_x,home_y,start_x,start_y,curr_x,curr_y,end_x,end_y;
	bool can_attack();
	void attack();
	bool panauti_checker();
	bool is_movable();
	void move();
	bool is_openable();
	void open();


};
class Red :public goti
{	
 public:
 	
    Red()
	{start_x=13;
	start_y=6;
	end_x=8;
	end_y=7;}
	Red(int x,int y)
	{
		home_x=x;
		home_y=y;
	}
	~Red(); 
};
class Yellow :public goti
{   
 public:
 	Yellow(){
	start_x=1;
	start_y=8;
	end_x=6;
	end_y=7;}
	Yellow(int x,int y)
	{
		home_x=x;
		home_y=y;
	}
	~Yellow(); 
};
class Green :public goti
{   
 public:
 	Green(){
	start_x=6;
	start_y=1;
	end_x=7;
	end_y=6;}
	Green(int x,int y)
	{
		home_x=x;
		home_y=y;
	}
	~Green(); 
};
class Blue :public goti
{  
 public:
 	Blue(){
	start_x=8;
	start_y=13;
    end_x=7;
	end_y=8;}
	Blue(int x,int y)
	{
		home_x=x;
		home_y=y;
	}
	~Blue(); 
};
int main()
{
	Board b;
	b.display();
	Red r1(10,1),r2(13,1),r3(10,4),r4(13,4);
	Green g1(1,1),g2(1,4),g3(4,1),g4(4,4);
	Blue b1(10,10),b2(13,13),b3(10,13),b4(13,10);
	Yellow y1(1,10),y2(1,13),y3(4,10),y4(4,13);

}