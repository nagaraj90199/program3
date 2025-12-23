def Employee_details(empid, empname, salary):
    result = (
        f"Employee Name: {empname}\n"
        f"Employee ID: {empid}\n"
        f"Salary: {salary}\n"
    )
    return result

if __name__ == "__main__":
    empid = "S109"
    empname = "Harsha"
    salary = 70000
    print(Employee_details(empid, empname, salary))
