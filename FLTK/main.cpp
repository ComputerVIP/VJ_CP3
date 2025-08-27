#include <FL/Fl.H>
#include <FL/Fl_Window.H>
#include <FL/Fl_Box.H>

int main() {
    Fl_Window window(340, 180, "Hello, FLTK!");
    Fl_Box box(20, 40, 300, 100, "Hello World");
    window.end();
    window.show();
    return Fl::run();
}