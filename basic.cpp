// VJ test thingy
#include <iostream>

class Hello {
public:
    void sayHello() {
        std::cout << "Hello, World!" << std::endl;
    }
};

int main() {
    Hello hello;
    hello.sayHello();
    return 0;
}