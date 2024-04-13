#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <string>
#include <sstream>
#include <limits>
#include <iomanip>

using namespace std;

class Task {
private:
    int _id;
    string name;
    bool isComplete;

public:
    Task(int id, string name, bool isComplete) : _id(id), name(name), isComplete(isComplete) {}

    string getTaskName() const {
        return name;
    }

    int getId() const {
        return _id;
    }

    bool getIsComplete() const {
        return isComplete;
    }

    void setTaskName(const string& taskName) {
        name = taskName;
    }

    void setIsComplete(bool complete) {
        isComplete = complete;
    }

    friend ostream& operator<<(ostream& os, const Task& task);
};

ostream& operator<<(ostream& os, const Task& task) {
    os << task._id << " " << task.name << " " << (task.isComplete ? "Task is completed" : "Task is pending");
    return os;
}

class SortById {
public:
    bool operator()(const Task& t1, const Task& t2) {
        return t1.getId() < t2.getId();
    }
};

vector<Task> loadTasksFromFile(const string& fileName) {
    vector<Task> tasks;
    ifstream file(fileName);
    string line;

    while (getline(file, line)) {
        istringstream iss(line);
        vector<string> data;
        string token;

        while (getline(iss, token, ',')) {
            data.push_back(token);
        }

        if (data.size() == 3) {
            tasks.emplace_back(stoi(data[0]), data[1], data[2] == "true");
        }
    }

    file.close();
    return tasks;
}

void saveTasksToFile(const vector<Task>& tasks, const string& fileName) {
    ofstream file(fileName);

    for (const auto& task : tasks) {
        file << task.getId() << "," << task.getTaskName() << "," << (task.getIsComplete() ? "true" : "false") << endl;
    }

    file.close();
}

void logTaskAction(const string& action, const Task& task) {
    ofstream file("task_history.txt", ios::app);
    file << action << ": " << task << endl;
    file.close();
}

void displayTasks(const vector<Task>& tasks) {
    cout << left << setw(10) << "Task ID" << setw(30) << "Task Name" << setw(20) << "Status" << endl;
    cout << string(60, '-') << endl;

    for (const auto& task : tasks) {
        cout << left << setw(10) << task.getId()
             << setw(30) << task.getTaskName()
             << setw(20) << (task.getIsComplete() ? "Completed" : "Pending") << endl;
    }
}
void deleteTask(vector<Task>& tasks, int id) {
    auto it = find_if(tasks.begin(), tasks.end(), [id](const Task& task) { return task.getId() == id; });
    if (it != tasks.end()) {
        logTaskAction("Deleted", *it);
        tasks.erase(it);
        cout << "Task deleted successfully.\n";
    } else {
        cout << "Task not found.\n";
    }
}
int main() {
    vector tasks = loadTasksFromFile("tasks.csv");
    int _id = tasks.empty() ? 1 : tasks.back().getId() + 1;

while (true) {
    cout << "1. Add new Task\n";
    cout << "2. Edit Task\n";
    cout << "3. Complete Task\n";
    cout << "4. Show All Tasks\n";
    cout << "5. Delete Task\n";
    cout << "6. Save Changes\n";
    cout << "7. Exit\n";
    cout << "Enter your choice: ";
    int choice;
    cin >> choice;
    cin.ignore(numeric_limits<streamsize>::max(), '\n'); // Consume newline

    switch (choice) {
        case 1: {
            cout << "Enter name of Task: ";
            string name;
            getline(cin, name);
            Task newTask(_id++, name, false);
            tasks.push_back(newTask);
            logTaskAction("Added", newTask);
            cout << "Added task successfully\n";
            break;
        }
        case 2: {
            cout << "Enter task ID: ";
            int id;
            cin >> id;
            cin.ignore();

            auto it = find_if(tasks.begin(), tasks.end(), [id](const Task& task) { return task.getId() == id; });
            if (it != tasks.end() && !it->getIsComplete()) {
                cout << "Enter modified task name: ";
                string newTaskName;
                getline(cin, newTaskName);
                it->setTaskName(newTaskName);
                logTaskAction("Updated", *it);
                cout << "Task updated successfully\n";
            } else if (it != tasks.end() && it->getIsComplete()) {
                cout << "Task is completed and cannot be edited. It can only be deleted.\n";
            } else {
                cout << "Task not found.\n";
            }
            break;
        }
        case 3: {
            cout << "Enter task ID: ";
            int id;
            cin >> id;

            auto it = find_if(tasks.begin(), tasks.end(), [id](const Task& task) { return task.getId() == id; });
            if (it != tasks.end() && !it->getIsComplete()) {
                it->setIsComplete(true);
                logTaskAction("Completed", *it);
                cout << "Task is completed\n";
            } else if (it != tasks.end() && it->getIsComplete()) {
                cout << "Task is already completed.\n";
            } else {
                cout << "Task not found.\n";
            }
            break;
        }
        case 4: {
            sort(tasks.begin(), tasks.end(), SortById());
            displayTasks(tasks);
            break;
        }
        case 5: {
            cout << "Enter task ID to delete: ";
            int id;
            cin >> id;
            deleteTask(tasks, id);
            break;
        }
        case 6: {
            saveTasksToFile(tasks, "tasks.csv");
            cout << "Changes saved successfully.\n";
            break;
        }
        case 7: {
            saveTasksToFile(tasks, "tasks.csv");
            cout << "Exiting...\n";
            return 0;
        }
        default:
            cout << "Invalid choice. Please try again.\n";
    }
}

}