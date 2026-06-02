from app.services import *
from app.exceptions import StudentNotFoundError
import os


def clear_screen():
    os.system("clear")  # Linux/Ubuntu


def menu():
    while True:
        print("\n===== STUDENT SYSTEM =====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Choice: ").strip()

        # ---------------- ADD ----------------
        if choice == "1":
            try:
                name = input("Name: ")
                age = int(input("Age: "))
                grade = input("Grade: ")

                result = create_student(name, age, grade)
                print("✅ Created:", result)

            except ValueError:
                print("❌ Age must be a number")

            input("\nPress Enter to continue...")
            clear_screen()

        # ---------------- VIEW ALL ----------------
        elif choice == "2":
            print(get_all_students())

            input("\nPress Enter to continue...")
            clear_screen()

        # ---------------- SEARCH ----------------
        elif choice == "3":
            try:
                sid = int(input("ID: "))
                print(get_student(sid))

            except ValueError:
                print("❌ ID must be a number")
            except StudentNotFoundError:
                print("❌ Student not found")

            input("\nPress Enter to continue...")
            clear_screen()

        # ---------------- UPDATE ----------------
        elif choice == "4":
            try:
                sid = int(input("ID: "))
                name = input("New Name: ")
                age = int(input("New Age: "))
                grade = input("New Grade: ")

                print(update_student(sid, name, age, grade))

            except ValueError:
                print("❌ Invalid input")
            except StudentNotFoundError:
                print("❌ Student not found")

            input("\nPress Enter to continue...")
            clear_screen()

        # ---------------- DELETE ----------------
        elif choice == "5":
            try:
                sid = int(input("ID: "))
                delete_student(sid)
                print("✅ Deleted successfully")

            except ValueError:
                print("❌ ID must be number")
            except StudentNotFoundError:
                print("❌ Student not found")

            input("\nPress Enter to continue...")
            clear_screen()

        # ---------------- EXIT ----------------
        elif choice == "6":
            print("👋 Exiting system...")
            break

        else:
            print("❌ Invalid choice")
            input("\nPress Enter...")
            clear_screen()


if __name__ == "__main__":
    menu()