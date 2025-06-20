#include <iostream>
using namespace std;

struct Student {
    char name[30];
    float* grades;
    int nGrades;
};


class GradeMetric {
public:
    virtual float compute(const Student* s) = 0;
    virtual ~GradeMetric() {}
};

class MeanMetric : public GradeMetric {
public:
    float compute(const Student* s) override {
        if (s->nGrades == 0) return 0.0f;

        float sum = 0.0f;
        for (int i = 0; i < s->nGrades; ++i) {
            sum += *(s->grades + i);
        }
        return sum / s->nGrades;
    }
};

class RangeMetric : public GradeMetric {
public:
    float compute(const Student* s) override {
        if (s->nGrades == 0) return 0.0f;

        float min = *(s->grades);
        float max = *(s->grades);

        for (int i = 1; i < s->nGrades; ++i) {
            float current = *(s->grades + i);
            if (current < min) min = current;
            if (current > max) max = current;
        }

        return max - min;
    }
};

void addGrade(Student& student, float grade) {

    float* newGrades = new float[student.nGrades + 1];


    for (int i = 0; i < student.nGrades; ++i) {
        *(newGrades + i) = *(student.grades + i);
    }


    *(newGrades + student.nGrades) = grade;


    delete[] student.grades;


    student.grades = newGrades;
    student.nGrades++;
}

void removeGrade(Student& student, int index) {
    if (index < 0 || index >= student.nGrades) {
        cout << "Invalid index.\n";
        return;
    }

    if (student.nGrades == 1) {

        delete[] student.grades;
        student.grades = nullptr;
        student.nGrades = 0;
        return;
    }


    float* newGrades = new float[student.nGrades - 1];


    int newIndex = 0;
    for (int i = 0; i < student.nGrades; ++i) {
        if (i != index) {
            *(newGrades + newIndex) = *(student.grades + i);
            newIndex++;
        }
    }

    delete[] student.grades;


    student.grades = newGrades;
    student.nGrades--;
}


void displayGrades(const Student& student) {
    cout << "\nGrades for " << student.name << ": ";
    if (student.nGrades == 0) {
        cout << "No grades recorded";
    } else {

        for (int i = 0; i < student.nGrades; ++i) {
            cout << *(student.grades + i);
            if (i < student.nGrades - 1) cout << " ";
        }
    }
    cout << "\n";
}

// ======= Menu System =======
void showMenu() {
    cout << "\n==== Student Grade Analyzer ====\n";
    cout << "1. Add grade\n";
    cout << "2. Remove grade\n";
    cout << "3. Show all grades\n";
    cout << "4. Compute metrics (mean, range)\n";
    cout << "5. Exit\n";
    cout << "Choose: ";
}


int main() {

    Student student;
    student.grades = nullptr;
    student.nGrades = 0;

    cout << "Enter student name: ";
    cin.getline(student.name, 30);


    GradeMetric** metrics = new GradeMetric*[2];
    metrics[0] = new MeanMetric();
    metrics[1] = new RangeMetric();

    int choice;
    bool running = true;

    while (running) {
        showMenu();
        cin >> choice;

        switch (choice) {
            case 1: {
                float grade;
                cout << "Enter grade: ";
                cin >> grade;
                addGrade(student, grade);
                break;
            }
            case 2: {
                if (student.nGrades == 0) {
                    cout << "No grades to remove.\n";
                    break;
                }
                displayGrades(student);
                int index;
                cout << "Enter index to remove (0-based): ";
                cin >> index;
                removeGrade(student, index);
                break;
            }
            case 3:
                displayGrades(student);
                break;
            case 4: {
                displayGrades(student);
                if (student.nGrades > 0) {
                    cout << "\n--- Metrics ---\n";

                    cout << "Mean: " << metrics[0]->compute(&student) << endl;
                    cout << "Range: " << metrics[1]->compute(&student) << endl;
                } else {
                    cout << "No grades available for computation.\n";
                }
                break;
            }
            case 5:
                running = false;
                break;
            default:
                cout << "Invalid option.\n";
        }
    }

    delete[] student.grades;
    delete metrics[0];
    delete metrics[1];
    delete[] metrics;

    cout << "Goodbye!\n";
    return 0;
}
