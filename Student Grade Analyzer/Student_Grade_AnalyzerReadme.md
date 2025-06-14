# C++ STUDENT FINAL PROJECT/223005124/IRANZICLAUDE/HUYE-CAMPUS 


## Assignment 29: Student Grade Analyzer

## Assignment Overview

This project implements project 29: Student Grade Analyzer, demonstrating proficiency in advanced C++ programming concepts including inheritance, polymorphism, dynamic memory management, and pointer arithmetic.

## Assignment Requirements Implementation

### 1. Student Structure Definition ✓
```cpp
struct Student {
    char name[30];     // Fixed-size character array for student name
    float* grades;     // Pointer to dynamically allocated grade array
    int nGrades;       // Counter for number of grades stored
};
```
**Implementation Notes:**
- `grades` is dynamically allocated using `new float[]`
- Memory is managed manually throughout the program lifecycle
- Structure initialized with `grades = nullptr` and `nGrades = 0`

### 2. Abstract Base Class with Pure Virtual Function ✓
```cpp
class GradeMetric {
public:
    virtual float compute(const Student*) = 0;  // Pure virtual function
    virtual ~GradeMetric() {}                   // Virtual destructor
};
```
**Design Rationale:**
- Pure virtual function enforces implementation in derived classes
- Virtual destructor ensures proper cleanup in polymorphic scenarios
- Const parameter prevents modification of student data during computation

### 3. Inheritance and Polymorphism Implementation ✓

#### MeanMetric Class
```cpp
class MeanMetric : public GradeMetric {
public:
    float compute(const Student* s) override {
        // Implementation using pointer arithmetic exclusively
    }
};
```

#### RangeMetric Class  
```cpp
class RangeMetric : public GradeMetric {
public:
    float compute(const Student* s) override {
        // Implementation using pointer arithmetic exclusively
    }
};
```

**Polymorphism Demonstration:**
- Both classes inherit from `GradeMetric`
- Override the pure virtual `compute()` function
- Enable runtime polymorphism through base class pointers

### 4. Dynamic Polymorphic Dispatch ✓
```cpp
GradeMetric** metrics = new GradeMetric*[2];
metrics[0] = new MeanMetric();
metrics[1] = new RangeMetric();

// Polymorphic dispatch - correct virtual function called at runtime
float mean = metrics[0]->compute(&student);
float range = metrics[1]->compute(&student);
```

**Technical Implementation:**
- Dynamic array of base class pointers allocated on heap
- Derived class objects stored through base class pointers
- Runtime dispatch achieved through virtual function table (vtable)

### 5. Mandatory Pointer Arithmetic Usage ✓

All array operations use pointer arithmetic instead of array subscripting:

```cpp
// Mean calculation example
for (int i = 0; i < s->nGrades; ++i) {
    sum += *(s->grades + i);        // Pointer arithmetic
    // NOT: sum += s->grades[i];    // Array subscripting forbidden
}

// Grade copying in addGrade()
for (int i = 0; i < student.nGrades; ++i) {
    *(newGrades + i) = *(student.grades + i);  // Pointer arithmetic
}
```

**Rationale for Pointer Arithmetic:**
- Demonstrates understanding of memory addressing
- Shows relationship between arrays and pointers
- Required by assignment specifications

### 6. Dynamic Array Management Functions ✓

#### addGrade(Student&, float) Implementation
```cpp
void addGrade(Student& student, float grade) {
    // 1. Allocate new array with increased size
    float* newGrades = new float[student.nGrades + 1];
    
    // 2. Copy existing grades using pointer arithmetic
    for (int i = 0; i < student.nGrades; ++i) {
        *(newGrades + i) = *(student.grades + i);
    }
    
    // 3. Add new grade
    *(newGrades + student.nGrades) = grade;
    
    // 4. Clean up old array and update structure
    delete[] student.grades;
    student.grades = newGrades;
    student.nGrades++;
}
```

#### removeGrade(Student&, int) Implementation
```cpp
void removeGrade(Student& student, int index) {
    // Input validation
    if (index < 0 || index >= student.nGrades) return;
    
    // Handle edge case: removing last grade
    if (student.nGrades == 1) {
        delete[] student.grades;
        student.grades = nullptr;
        student.nGrades = 0;
        return;
    }
    
    // 1. Allocate smaller array
    float* newGrades = new float[student.nGrades - 1];
    
    // 2. Copy grades excluding target index
    int newIndex = 0;
    for (int i = 0; i < student.nGrades; ++i) {
        if (i != index) {
            *(newGrades + newIndex) = *(student.grades + i);
            newIndex++;
        }
    }
    
    // 3. Update structure
    delete[] student.grades;
    student.grades = newGrades;
    student.nGrades--;
}
```

## Key C++ Concepts Demonstrated

### 1. Object-Oriented Programming
- **Inheritance:** Derived classes extend base class functionality
- **Polymorphism:** Runtime method dispatch through virtual functions
- **Abstraction:** Pure virtual functions define interface contracts

### 2. Memory Management
- **Dynamic Allocation:** Using `new` and `delete` operators
- **Memory Leaks Prevention:** Proper cleanup in destructors and main()
- **Resource Management:** Manual array resizing and reallocation

### 3. Advanced Pointer Operations
- **Pointer Arithmetic:** Direct memory address manipulation
- **Double Pointers:** Array of pointers for polymorphic storage
- **Const Correctness:** Protecting data integrity in function parameters

### 4. Software Design Principles
- **Single Responsibility:** Each class has one clear purpose
- **Open/Closed Principle:** Extensible through inheritance
- **Interface Segregation:** Clean abstract base class design

## Program Functionality

The application provides an interactive menu system for:
1. Adding grades to student record
2. Removing grades by index position
3. Displaying all current grades
4. Computing statistical metrics (mean and range)
5. Proper program termination with memory cleanup

## Technical Specifications

- **Language:** C++11 or later
- **Compilation:** Standard C++ compiler (g++, clang++)
- **Memory Model:** Manual memory management (no STL containers)
- **Design Pattern:** Abstract Factory pattern for metrics

## Memory Safety and Error Handling

- Input validation for grade removal operations
- Null pointer checks before array operations
- Proper cleanup of all dynamically allocated memory
- Exception-safe resource management

## Compilation and Execution

```bash
# Compile
g++ -std=c++11 -Wall -o grade_analyzer main.cpp

# Run
./grade_analyzer
```

## Code Quality Assurance

- **No Memory Leaks:** All `new` operations paired with corresponding `delete`
- **Const Correctness:** Appropriate use of const parameters and methods
- **Error Handling:** Graceful handling of edge cases and invalid input
- **Clean Architecture:** Separation of concerns and modular design

---

**Assignment Completion Status:** All requirements implemented and tested  
**Submission:** Ready for academic review
