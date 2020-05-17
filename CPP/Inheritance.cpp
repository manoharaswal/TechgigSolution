#include <iostream>

using namespace std;

class Rectangle{
    protected:
        int width;
        int height;
    public:
        void display(){
            cout << width << " " << height;
        }
};

class RectangleArea : public Rectangle{
    public:
        void read_input(){
            cin >> width >> height;
        }

        void display(){
            Rectangle::display();
            cout << endl << (width * height);
        }
};

int main()
{
	RectangleArea Rect;
	Rect.read_input();
	Rect.display();
}
