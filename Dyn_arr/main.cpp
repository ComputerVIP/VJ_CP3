// VJ Dynamic Array
// g++ main.cpp -o app `fltk-config --cxxflags --ldflags`

#include <iostream>
#include <vector>
#include <memory>
#include <string>
#include <FL/Fl.H>
#include <FL/Fl_Window.H>
#include <FL/Fl_Input.H>
#include <FL/Fl_Button.H>
#include <FL/Fl_Output.H>
#include <FL/Fl_Multiline_Output.H>
#include <FL/Fl_Scroll.H>

struct Widgets {
    Fl_Input* input;
    Fl_Output* output;
    Fl_Multiline_Output* outputFull;
    std::vector<std::unique_ptr<std::string>>* spaceArray;
};

void button_cb(Fl_Widget* w, void* data) {
    Widgets* widgets = (Widgets*)data;
    // Add input to array with 5 spaces in front
    std::string newStr = widgets->input->value();
    widgets->spaceArray->push_back(std::make_unique<std::string>(newStr));
    std::cout << newStr << std::endl;

    // Show last entry in output box
    widgets->output->value(widgets->input->value());

    // Concatenate all strings for full output, each on its own line
    std::string all;
    for (const auto& s : *widgets->spaceArray) {
        all += *s + "\n";
    }
    widgets->outputFull->value(all.c_str());
}

int main(int argc, char** argv) {
    // Vector of smart pointers to strings
    std::vector<std::unique_ptr<std::string>> spaceArray;
    // Add names WITHOUT spaces (or add spaces if you want them indented)
    spaceArray.push_back(std::make_unique<std::string>("Alice"));
    spaceArray.push_back(std::make_unique<std::string>("Bob"));
    spaceArray.push_back(std::make_unique<std::string>("Carol"));
    spaceArray.push_back(std::make_unique<std::string>("Dave"));
    spaceArray.push_back(std::make_unique<std::string>("Eve"));

    // Print initial names
    for (size_t i = 0; i < spaceArray.size(); ++i) {
        std::cout << *spaceArray[i] << std::endl;
    }

    Fl_Window* win = new Fl_Window(400, 800, "Dynamic Array");

    Fl_Input* input = new Fl_Input(100, 40, 200, 30, "Enter text:");
    Fl_Output* output = new Fl_Output(100, 90, 200, 30, "You typed:");
    Fl_Button* button = new Fl_Button(100, 450, 100, 30, "Submit");
    
    // Create a scroll area for the multiline output
    Fl_Scroll* scroll = new Fl_Scroll(100, 130, 200, 300); // x, y, width, height
    Fl_Multiline_Output* outputFull = new Fl_Multiline_Output(0, 0, 300, 400, "Full Output:");
    scroll->add(outputFull);

    

    Widgets* widgets = new Widgets{input, output, outputFull, &spaceArray};
    button->callback(button_cb, widgets);

    win->resizable(*scroll);
    win->end();
    win->show(argc, argv);

    return Fl::run();
}