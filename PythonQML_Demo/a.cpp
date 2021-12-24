
#include <iostream>
using namespace std;

class A
{
public:
	A() { value = 2;}
	virtual void show() const { cout << value << endl;} 
	virtual void dd(){cout << value << endl;}
protected:
int value;	
};

class B : public A
{
public:
	B() { value = 4;}
	virtual void show() const { cout << value << endl;} 
private:

};
void foo(const B& b)
{
	b.show();
	b.dd();
}
int main()

{
	return 0;
}