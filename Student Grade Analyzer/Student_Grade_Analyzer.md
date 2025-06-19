# Student Grade Analyzer System - C++_223005124_iranzi_claude

## Project Overview

This project implements a Student Grade Analyzer system in C++ that demonstrates advanced object-oriented programming concepts, dynamic memory management, and statistical computation. The system allows users to manage student grades dynamically and compute various statistical metrics using polymorphism and virtual functions.

## Task Description

**Assigned Task:** Create a Student Grade Analyzer system that:
- Manages student grades using dynamic memory allocation
- Implements multiple statistical metrics using polymorphism
- Provides functionality to add and remove grades dynamically
- Uses object-oriented programming principles with abstract classes
- Demonstrates proper memory management and pointer arithmetic
- Provides an interactive user interface for grade management

## Features

- **Dynamic Grade Management**: Add and remove grades at runtime with automatic memory reallocation
- **Statistical Metrics Computation**:
  - **Mean Calculation**: Computes average of all grades
  - **Range Calculation**: Computes difference between highest and lowest grades
- **Polymorphic Design**: Abstract base class with virtual functions for extensible metric system
- **Interactive Menu System**: User-friendly command-line interface
- **Memory Safety**: Proper allocation and deallocation of dynamic memory
- **Pointer Arithmetic**: Demonstrates advanced pointer usage throughout the system

## How the Task Was Completed

### 1. System Architecture

The system is built using several key components:

- **Student Structure**: Stores student information and dynamic grade array
- **Abstract GradeMetric Class**: Base class defining the metric computation interface
- **Concrete Metric Classes**: MeanMetric and RangeMetric implementations
- **Dynamic Memory Management**: Functions for adding/removing grades with reallocation
- **Interactive Menu System**: Complete user interface for all operations

### 2. Implementation Approach

1. **Data Structure Design**: Used struct with dynamic array for flexible grade storage
2. **Polymorphic Architecture**: Implemented abstract base class with pure virtual functions
3. **Strategy Pattern**: Different statistical computations as separate metric classes
4. **Dynamic Memory Management**: Custom reallocation functions for grade array manipulation
5. **Pointer Arithmetic**: Extensive use of pointer operations for memory management

### 3. Statistical Algorithms

- **Mean Algorithm**: Sum all grades and divide by count
- **Range Algorithm**: Find minimum and maximum values, return difference

## Detailed Code Explanation

### Header and Namespace
```cpp
#include <iostream>     // For input/output operations
using namespace std;    // Standard namespace
```

### Student Data Structure
```cpp
struct Student {
    char name[30];      // Fixed-size character array for student name
    float* grades;      // Dynamic array pointer for grades
    int nGrades;        // Current number of grades stored
};
```
**Purpose**: Defines the core data structure. Uses a dynamic pointer for grades to allow runtime resizing, and tracks the count of grades for proper memory management.

### Abstract Base Class for Metrics
```cpp
class GradeMetric {
public:
    // Pure virtual function - must be implemented by derived classes
    virtual float compute(const Student* s) = 0;
    // Virtual destructor ensures proper cleanup in polymorphic scenarios
    virtual ~GradeMetric() {}
};
```
**Purpose**: Establishes the interface contract for all metric computations. The pure virtual function ensures derived classes must implement their own computation logic.

### Mean Metric Implementation
```cpp
class MeanMetric : public GradeMetric {
public:
    float compute(const Student* s) override {
        // Handle empty grade list to prevent division by zero
        if (s->nGrades == 0) return 0.0f;

        float sum = 0.0f;
        // Use pointer arithmetic to iterate through grades
        for (int i = 0; i < s->nGrades; ++i) {
            sum += *(s->grades + i);  // Dereference pointer at offset i
        }
        // Return arithmetic mean
        return sum / s->nGrades;
    }
};
```
**Purpose**: Implements arithmetic mean calculation. Uses pointer arithmetic `*(s->grades + i)` instead of array notation to demonstrate pointer manipulation. Includes zero division protection.

### Range Metric Implementation
```cpp
class RangeMetric : public GradeMetric {
public:
    float compute(const Student* s) override {
        // Handle empty grade list
        if (s->nGrades == 0) return 0.0f;

        // Initialize min/max with first grade using pointer dereference
        float min = *(s->grades);
        float max = *(s->grades);

        // Iterate starting from second element
        for (int i = 1; i < s->nGrades; ++i) {
            float current = *(s->grades + i);  // Get current grade via pointer arithmetic
            if (current < min) min = current;   // Update minimum if needed
            if (current > max) max = current;   // Update maximum if needed
        }

        return max - min;  // Return the range (difference)
    }
};
```
**Purpose**: Computes the range (max - min) of grades. Efficiently finds min/max in single pass through the data using pointer arithmetic for array access.

### Add Grade Function
```cpp
void addGrade(Student& student, float grade) {
    // Allocate new array with space for one additional grade
    float* newGrades = new float[student.nGrades + 1];

    // Copy existing grades to new array using pointer arithmetic
    for (int i = 0; i < student.nGrades; ++i) {
        *(newGrades + i) = *(student.grades + i);
    }

    // Add the new grade at the end
    *(newGrades + student.nGrades) = grade;

    // Free old memory to prevent memory leaks
    delete[] student.grades;

    // Update student structure with new array and count
    student.grades = newGrades;
    student.nGrades++;
}
```
**Purpose**: Dynamically resizes the grade array to accommodate a new grade. Demonstrates proper memory reallocation pattern: allocate new memory, copy data, free old memory, update pointers.

### Remove Grade Function
```cpp
void removeGrade(Student& student, int index) {
    // Validate index bounds
    if (index < 0 || index >= student.nGrades) {
        cout << "Invalid index.\n";
        return;
    }

    // Special case: removing the last grade
    if (student.nGrades == 1) {
        delete[] student.grades;    // Free memory
        student.grades = nullptr;   // Set to null pointer
        student.nGrades = 0;        // Reset count
        return;
    }

    // Allocate new smaller array
    float* newGrades = new float[student.nGrades - 1];

    // Copy all grades except the one at specified index
    int newIndex = 0;
    for (int i = 0; i < student.nGrades; ++i) {
        if (i != index) {  // Skip the grade to be removed
            *(newGrades + newIndex) = *(student.grades + i);
            newIndex++;
        }
    }

    // Clean up old memory and update structure
    delete[] student.grades;
    student.grades = newGrades;
    student.nGrades--;
}
```
**Purpose**: Removes a grade at specified index by creating a new smaller array and copying all elements except the target. Handles edge cases like removing the last remaining grade.

### Display Grades Function
```cpp
void displayGrades(const Student& student) {
    cout << "\nGrades for " << student.name << ": ";
    
    // Check if student has any grades
    if (student.nGrades == 0) {
        cout << "No grades recorded";
    } else {
        // Display all grades using pointer arithmetic
        for (int i = 0; i < student.nGrades; ++i) {
            cout << *(student.grades + i);              // Print current grade
            if (i < student.nGrades - 1) cout << " ";   // Add space between grades
        }
    }
    cout << "\n";
}
```
**Purpose**: Displays all grades for a student in a formatted manner. Uses pointer arithmetic for array access and handles the empty grades case gracefully.

### Menu Display Function
```cpp
void showMenu() {
    cout << "\n==== Student Grade Analyzer ====\n";
    cout << "1. Add grade\n";
    cout << "2. Remove grade\n";
    cout << "3. Show all grades\n";
    cout << "4. Compute metrics (mean, range)\n";
    cout << "5. Exit\n";
    cout << "Choose: ";
}
```
**Purpose**: Provides a clean, user-friendly interface by displaying all available options in a formatted menu.

### Main Function - Initialization
```cpp
int main() {
    // Initialize student structure
    Student student;
    student.grades = nullptr;  // Start with null pointer (no grades)
    student.nGrades = 0;       // Zero grade count

    // Get student name using getline for full name support
    cout << "Enter student name: ";
    cin.getline(student.name, 30);

    // Create array of metric objects using polymorphism
    GradeMetric** metrics = new GradeMetric*[2];
    metrics[0] = new MeanMetric();    // First metric: Mean
    metrics[1] = new RangeMetric();   // Second metric: Range
```
**Purpose**: Initializes the student with empty grade list and creates polymorphic metric objects. Uses dynamic allocation for the metrics array to demonstrate pointer-to-pointer usage.

### Main Function - Menu Loop
```cpp
    int choice;
    bool running = true;

    while (running) {
        showMenu();           // Display options
        cin >> choice;        // Get user selection

        switch (choice) {
            case 1: {         // Add grade option
                float grade;
                cout << "Enter grade: ";
                cin >> grade;
                addGrade(student, grade);  // Call add function
                break;
            }
            case 2: {         // Remove grade option
                if (student.nGrades == 0) {
                    cout << "No grades to remove.\n";
                    break;
                }
                displayGrades(student);    // Show current grades
                int index;
                cout << "Enter index to remove (0-based): ";
                cin >> index;
                removeGrade(student, index);  // Call remove function
                break;
            }
            case 3:           // Display grades option
                displayGrades(student);
                break;
            case 4: {         // Compute metrics option
                displayGrades(student);
                if (student.nGrades > 0) {
                    cout << "\n--- Metrics ---\n";
                    // Use polymorphism to call appropriate compute methods
                    cout << "Mean: " << metrics[0]->compute(&student) << endl;
                    cout << "Range: " << metrics[1]->compute(&student) << endl;
                } else {
                    cout << "No grades available for computation.\n";
                }
                break;
            }
            case 5:           // Exit option
                running = false;
                break;
            default:
                cout << "Invalid option.\n";
        }
    }
```
**Purpose**: Main program loop that handles user interaction. Demonstrates polymorphic method calls where the same interface (`compute()`) behaves differently for different metric types.

### Main Function - Cleanup
```cpp
    // Clean up all dynamically allocated memory
    delete[] student.grades;  // Free grades array
    delete metrics[0];        // Free MeanMetric object
    delete metrics[1];        // Free RangeMetric object
    delete[] metrics;         // Free metrics array

    cout << "Goodbye!\n";
    return 0;
}
```
**Purpose**: Ensures all dynamically allocated memory is properly freed to prevent memory leaks. Demonstrates proper cleanup order: objects first, then arrays.

## Key Programming Concepts Demonstrated

### 1. Object-Oriented Programming
- **Inheritance**: MeanMetric and RangeMetric inherit from GradeMetric
- **Polymorphism**: Virtual functions allow runtime method selection
- **Abstraction**: Abstract base class defines interface without implementation
- **Encapsulation**: Class methods encapsulate specific computation logic

### 2. Advanced Memory Management
- **Dynamic Allocation**: Using `new` and `new[]` for runtime memory allocation
- **Memory Reallocation**: Custom functions to resize arrays dynamically
- **Proper Cleanup**: Systematic deallocation with `delete` and `delete[]`
- **Pointer Arithmetic**: Extensive use of `*(pointer + offset)` notation

### 3. Data Structures and Algorithms
- **Dynamic Arrays**: Resizable arrays using pointers
- **Statistical Algorithms**: Mean and range computation
- **Array Manipulation**: Adding and removing elements with reallocation

### 4. Advanced C++ Features
- **Pure Virtual Functions**: Abstract base class design
- **Virtual Destructors**: Proper polymorphic cleanup
- **Reference Parameters**: Pass-by-reference for efficiency
- **Const Correctness**: Proper use of const parameters

## Sample Program Outputs

### 1. Program Startup
```
Enter student name: John Smith

==== Student Grade Analyzer ====
1. Add grade
2. Remove grade
3. Show all grades
4. Compute metrics (mean, range)
5. Exit
Choose: 
```

### 2. Adding Grades
```
Choose: 1
Enter grade: 85.5

Choose: 1
Enter grade: 92.0

Choose: 1
Enter grade: 78.5
```

### 3. Displaying All Grades
```
Choose: 3

Grades for John Smith: 85.5 92 78.5
```

### 4. Computing Metrics
```
Choose: 4

Grades for John Smith: 85.5 92 78.5

--- Metrics ---
Mean: 85.3333
Range: 13.5
```

### 5. Removing a Grade
```
Choose: 2

Grades for John Smith: 85.5 92 78.5
Enter index to remove (0-based): 1

Choose: 3

Grades for John Smith: 85.5 78.5
```

### 6. Updated Metrics After Removal
```
Choose: 4

Grades for John Smith: 85.5 78.5

--- Metrics ---
Mean: 82
Range: 7
```

### 7. Attempting to Remove from Empty List
```
Choose: 2
No grades to remove.
```

### 8. Computing Metrics with No Grades
```
Choose: 4

Grades for John Smith: No grades recorded
No grades available for computation.
```

### 9. Program Exit
```
Choose: 5
Goodbye!
```

## Compilation and Execution

### To compile the program:
```bash
g++ -o grade_analyzer grade_analyzer.cpp
```

## Technical Analysis

### Memory Complexity
- **Space Complexity**: O(n) where n is the number of grades
- **Dynamic Growth**: Array grows linearly with each added grade
- **Memory Efficiency**: Only allocates memory needed for current grades

### Time Complexity
- **Add Grade**: O(n) due to array copying during reallocation
- **Remove Grade**: O(n) due to array copying and element shifting
- **Compute Mean**: O(n) single pass through all grades
- **Compute Range**: O(n) single pass to find min/max
- **Display Grades**: O(n) single pass for output

### Design Patterns Used
1. **Strategy Pattern**: Different metric computation strategies
2. **Template Method**: Abstract base class with concrete implementations
3. **RAII Principle**: Proper resource management in destructors

## Learning Outcomes

Through this project, the following advanced concepts were successfully implemented:

1. **Advanced Memory Management**: Dynamic allocation, reallocation, and proper cleanup
2. **Polymorphic Design**: Abstract classes with virtual functions
3. **Pointer Arithmetic**: Extensive use of pointer operations instead of array notation
4. **Statistical Computation**: Implementation of mathematical algorithms
5. **User Interface Design**: Interactive menu-driven application
6. **Code Organization**: Clean separation of concerns and modular design


## Advanced Features Demonstrated

### 1. Memory Management Excellence
- Custom reallocation functions that properly handle memory growth/shrinkage
- Zero memory leaks through systematic cleanup
- Efficient memory usage with dynamic sizing

### 2. Polymorphic Architecture
- Extensible design allowing easy addition of new metrics
- Runtime method resolution through virtual function calls
- Clean separation between interface and implementation

### 3. Pointer Mastery
- Consistent use of pointer arithmetic throughout the codebase
- Proper pointer lifecycle management
- Demonstration of pointer-to-pointer usage for metric arrays

---


**Key Concepts**: Dynamic Memory Management, Polymorphism, Pointer Arithmetic, Statistical Computing
