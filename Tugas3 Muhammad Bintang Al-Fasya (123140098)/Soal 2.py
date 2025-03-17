
class Employee:
    def __init__(self, name, role, hours_worked, task_completed):
        self.name = name                 
        self.role = role                 
        self.hours_worked = hours_worked  
        self.task_completed = task_completed  

    # Metode abstrak yang akan diimplementasikan oleh kelas turunan
    def work(self):
        pass

    # Metode untuk menghitung rasio kinerja (jumlah tugas selesai per jam kerja)
    def evaluate_performance(self):
        return self.task_completed / self.hours_worked


# Kelas turunan SoftwareEngineer dari kelas Employee
class SoftwareEngineer(Employee):
    def work(self):
        performance_ratio = self.evaluate_performance()

        if performance_ratio > 1.5:
            performance = "High Performance"
        elif performance_ratio > 1:
            performance = "Medium Performance"
        else:
            performance = "Low Performance"

        return f"{self.name} (Software Engineer) is coding. \nPerformance Rating: {performance}"


# Kelas turunan DataScientist dari kelas Employee
class DataScientist(Employee):
    def work(self):
        performance_ratio = self.evaluate_performance()

        if performance_ratio > 2:
            performance = "High Performance"
        elif performance_ratio > 1:
            performance = "Medium Performance"
        else:
            performance = "Low Performance"


        return f"{self.name} (Data Scientist) is analyzing data. \nPerformance Rating: {performance}"


# Kelas turunan ProductManager dari kelas Employee
class ProductManager(Employee):
    def work(self):
        performance_ratio = self.evaluate_performance()

        if performance_ratio > 3:
            performance = "High Performance"
        elif performance_ratio > 1.5:
            performance = "Medium Performance"
        else:
            performance = "Low Performance"

        return f"{self.name} (Product Manager) is managing the product roadmap. \nPerformance Rating: {performance}"

employees = [
    SoftwareEngineer("Alice", "Software Engineer", 45, 80),    
    DataScientist("Bob", "Data Scientist", 60, 100),            
    ProductManager("Charlie", "Product Manager", 50, 120),      
    SoftwareEngineer("David", "Software Engineer", 45, 40),     
]

for employee in employees:
    print(employee.work())
