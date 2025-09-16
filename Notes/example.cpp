#include <iostream>
#include <vector>
#include <memory>
#include <string>

int main() {
    // Vector of smart pointers to strings
    std::vector<std::unique_ptr<std::string>> spaceArray;
    spaceArray.push_back(std::make_unique<std::string>("a"));
    spaceArray.push_back(std::make_unique<std::string>("b"));
    spaceArray.push_back(std::make_unique<std::string>("c"));

    // Add spaces based on index and print
    for (size_t i = 0; i < spaceArray.size(); ++i) { // For each string
        *spaceArray[i] = std::string(i, ' ') + *spaceArray[i]; // Add leading spaces
        std::cout << *spaceArray[i] << std::endl;
    }

    return 0;
} 