import tkinter as tk
from tkinter import ttk, messagebox, filedialog, simpledialog


class GymManagementSystem:
    def __init__(self):
        self.members = []
        self.current_member_id = 1

    def add_member(self, name, age, gender, membership_type, workout_plan, photo_path):
        member = {
            'member_id': self.current_member_id,
            'name': name,
            'age': age,
            'gender': gender,
            'membership_type': membership_type,
            'workout_plan': workout_plan,
            'photo': photo_path,
            'check_in_time': None,
            'check_out_time': None,
            'payments': [],
            'workout_logs': [],
            'attendance': []  # Track check-in and check-out times
        }
        self.members.append(member)
        self.current_member_id += 1
        return member['member_id']

    def edit_member(self, member_id, name, age, gender, membership_type, workout_plan, photo_path):
        member = next((m for m in self.members if m['member_id'] == member_id), None)
        if not member:
            return False

        if name:
            member['name'] = name
        if age:
            member['age'] = age
        if gender:
            member['gender'] = gender
        if membership_type:
            member['membership_type'] = membership_type
        if workout_plan:
            member['workout_plan'] = workout_plan
        if photo_path:
            member['photo'] = photo_path
        return True

    def remove_member(self, member_id):
        member = next((m for m in self.members if m['member_id'] == member_id), None)
        if not member:
            return False
        self.members.remove(member)
        return True

    def show_member_details(self, member_id):
        return next((m for m in self.members if m['member_id'] == member_id), None)

    def list_all_members(self):
        return self.members

    def pay_fees(self, member_id, amount):
        member = next((m for m in self.members if m['member_id'] == member_id), None)
        if not member:
            return False
        member['payments'].append({'amount': amount, 'date': 'today'})  # You can use datetime for actual dates
        return True

    def check_in(self, member_id):
        member = next((m for m in self.members if m['member_id'] == member_id), None)
        if not member:
            return False
        member['check_in_time'] = 'Checked In'
        member['attendance'].append({'action': 'check_in', 'time': 'now'})  # You can use datetime for actual times
        return True

    def check_out(self, member_id):
        member = next((m for m in self.members if m['member_id'] == member_id), None)
        if not member:
            return False
        member['check_out_time'] = 'Checked Out'
        member['attendance'].append({'action': 'check_out', 'time': 'now'})  # You can use datetime for actual times
        return True

    def add_workout_log(self, member_id, workout_log):
        member = next((m for m in self.members if m['member_id'] == member_id), None)
        if not member:
            return False
        member['workout_logs'].append(workout_log)
        return True

    def get_payment_history(self, member_id):
        member = next((m for m in self.members if m['member_id'] == member_id), None)
        if not member:
            return None
        return member['payments']

    def get_attendance_history(self, member_id):
        member = next((m for m in self.members if m['member_id'] == member_id), None)
        if not member:
            return None
        return member['attendance']


class GymManagementGUI(tk.Tk):
    def __init__(self, gym_system):
        super().__init__()
        self.gym_system = gym_system
        self.title("Gym Management System")
        self.geometry("600x400")

        self.tab_control = ttk.Notebook(self)

        self.member_tab = ttk.Frame(self.tab_control)
        self.tab_control.add(self.member_tab, text='Member Management')

        self.payment_tab = ttk.Frame(self.tab_control)
        self.tab_control.add(self.payment_tab, text='Payment Management')

        self.attendance_tab = ttk.Frame(self.tab_control)
        self.tab_control.add(self.attendance_tab, text='Attendance Management')

        self.workout_tab = ttk.Frame(self.tab_control)
        self.tab_control.add(self.workout_tab, text='Workout Management')

        self.tab_control.pack(expand=1, fill="both")

        self.create_member_tab()
        self.create_payment_tab()
        self.create_attendance_tab()
        self.create_workout_tab()

    def create_member_tab(self):
        self.name_label = tk.Label(self.member_tab, text="Name")
        self.name_entry = tk.Entry(self.member_tab)
        self.age_label = tk.Label(self.member_tab, text="Age")
        self.age_entry = tk.Entry(self.member_tab)
        self.gender_label = tk.Label(self.member_tab, text="Gender")
        self.gender_combo = ttk.Combobox(self.member_tab, values=["Male", "Female", "Other"])
        self.membership_type_label = tk.Label(self.member_tab, text="Membership Type")
        self.membership_type_combo = ttk.Combobox(self.member_tab, values=["Basic", "Premium", "VIP"])
        self.workout_plan_label = tk.Label(self.member_tab, text="Workout Plan")
        self.workout_plan_combo = ttk.Combobox(self.member_tab, values=["Plan A", "Plan B", "Plan C"])
        self.upload_photo_button = tk.Button(self.member_tab, text="Upload Photo", command=self.upload_photo)
        self.add_member_button = tk.Button(self.member_tab, text="Add Member", command=self.add_member)
        self.edit_member_button = tk.Button(self.member_tab, text="Edit Member", command=self.edit_member)
        self.remove_member_button = tk.Button(self.member_tab, text="Remove Member", command=self.remove_member)
        self.show_member_details_button = tk.Button(self.member_tab, text="Show Member Details",
                                                    command=self.show_member_details)
        self.list_all_members_button = tk.Button(self.member_tab, text="List All Members",
                                                 command=self.list_all_members)
        self.members_list_text = tk.Text(self.member_tab, height=10, width=50)

        self.name_label.grid(row=0, column=0, padx=10, pady=10)
        self.name_entry.grid(row=0, column=1, padx=10, pady=10)
        self.age_label.grid(row=1, column=0, padx=10, pady=10)
        self.age_entry.grid(row=1, column=1, padx=10, pady=10)
        self.gender_label.grid(row=2, column=0, padx=10, pady=10)
        self.gender_combo.grid(row=2, column=1, padx=10, pady=10)
        self.membership_type_label.grid(row=3, column=0, padx=10, pady=10)
        self.membership_type_combo.grid(row=3, column=1, padx=10, pady=10)
        self.workout_plan_label.grid(row=4, column=0, padx=10, pady=10)
        self.workout_plan_combo.grid(row=4, column=1, padx=10, pady=10)
        self.upload_photo_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)
        self.add_member_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10)
        self.edit_member_button.grid(row=7, column=0, columnspan=2, padx=10, pady=10)
        self.remove_member_button.grid(row=8, column=0, columnspan=2, padx=10, pady=10)
        self.show_member_details_button.grid(row=9, column=0, columnspan=2, padx=10, pady=10)
        self.list_all_members_button.grid(row=10, column=0, columnspan=2, padx=10, pady=10)
        self.members_list_text.grid(row=11, column=0, columnspan=2, padx=10, pady=10)

        self.photo_path = None

    def upload_photo(self):
        self.photo_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
        if self.photo_path:
            messagebox.showinfo("Photo Upload", "Photo uploaded successfully!")

    def add_member(self):
        name = self.name_entry.get()
        age = self.age_entry.get()
        gender = self.gender_combo.get()
        membership_type = self.membership_type_combo.get()
        workout_plan = self.workout_plan_combo.get()
        if not (name and age and gender and membership_type and workout_plan):
            messagebox.showerror("Input Error", "All fields are required.")
            return

        try:
            age = int(age)
        except ValueError:
            messagebox.showerror("Input Error", "Age must be a number.")
            return

        member_id = self.gym_system.add_member(name, age, gender, membership_type, workout_plan, self.photo_path)
        messagebox.showinfo("Member Added", f"Member added successfully with ID {member_id}")

    def edit_member(self):
        member_id = simpledialog.askinteger("Edit Member", "Enter member ID:")
        if not member_id:
            return

        name = self.name_entry.get()
        age = self.age_entry.get()
        gender = self.gender_combo.get()
        membership_type = self.membership_type_combo.get()
        workout_plan = self.workout_plan_combo.get()

        if age:
            try:
                age = int(age)
            except ValueError:
                messagebox.showerror("Input Error", "Age must be a number.")
                return

        success = self.gym_system.edit_member(member_id, name, age, gender, membership_type, workout_plan,
                                              self.photo_path)
        if success:
            messagebox.showinfo("Member Edited", f"Member ID {member_id} edited successfully")
        else:
            messagebox.showerror("Error", "Member not found")

    def remove_member(self):
        member_id = simpledialog.askinteger("Remove Member", "Enter member ID:")
        if not member_id:
            return
        success = self.gym_system.remove_member(member_id)
        if success:
            messagebox.showinfo("Member Removed", f"Member ID {member_id} removed successfully")
        else:
            messagebox.showerror("Error", "Member not found")

    def show_member_details(self):
        member_id = simpledialog.askinteger("Show Member Details", "Enter member ID:")
        if not member_id:
            return
        member = self.gym_system.show_member_details(member_id)
        if member:
            details = f"ID: {member['member_id']}\nName: {member['name']}\nAge: {member['age']}\nGender: {member['gender']}\nMembership Type: {member['membership_type']}\nWorkout Plan: {member['workout_plan']}\nPhoto: {member['photo']}\nCheck-in Time: {member['check_in_time']}\nCheck-out Time: {member['check_out_time']}"
            messagebox.showinfo("Member Details", details)
        else:
            messagebox.showerror("Error", "Member not found")

    def list_all_members(self):
        members = self.gym_system.list_all_members()
        self.members_list_text.delete(1.0, tk.END)
        for member in members:
            self.members_list_text.insert(tk.END, f"ID: {member['member_id']}, Name: {member['name']}\n")

    def create_payment_tab(self):
        self.member_id_label = tk.Label(self.payment_tab, text="Member ID")
        self.member_id_entry = tk.Entry(self.payment_tab)
        self.amount_label = tk.Label(self.payment_tab, text="Amount")
        self.amount_entry = tk.Entry(self.payment_tab)
        self.pay_fees_button = tk.Button(self.payment_tab, text="Pay Fees", command=self.pay_fees)
        self.payment_history_button = tk.Button(self.payment_tab, text="Payment History",
                                                command=self.show_payment_history)
        self.payment_list_text = tk.Text(self.payment_tab, height=10, width=50)

        self.member_id_label.grid(row=0, column=0, padx=10, pady=10)
        self.member_id_entry.grid(row=0, column=1, padx=10, pady=10)
        self.amount_label.grid(row=1, column=0, padx=10, pady=10)
        self.amount_entry.grid(row=1, column=1, padx=10, pady=10)
        self.pay_fees_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
        self.payment_history_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
        self.payment_list_text.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    def pay_fees(self):
        member_id = self.member_id_entry.get()
        amount = self.amount_entry.get()
        if not (member_id and amount):
            messagebox.showerror("Input Error", "All fields are required.")
            return

        try:
            member_id = int(member_id)
            amount = float(amount)
        except ValueError:
            messagebox.showerror("Input Error", "Member ID must be an integer and amount must be a number.")
            return

        success = self.gym_system.pay_fees(member_id, amount)
        if success:
            messagebox.showinfo("Payment Successful", f"Payment of {amount} made for member ID {member_id}")
        else:
            messagebox.showerror("Error", "Member not found")

    def show_payment_history(self):
        member_id = simpledialog.askinteger("Payment History", "Enter member ID:")
        if not member_id:
            return

        payments = self.gym_system.get_payment_history(member_id)
        if payments:
            self.payment_list_text.delete(1.0, tk.END)
            for payment in payments:
                self.payment_list_text.insert(tk.END, f"Amount: {payment['amount']}, Date: {payment['date']}\n")
        else:
            messagebox.showerror("Error", "Member not found or no payments made")

    def create_attendance_tab(self):
        self.attendance_member_id_label = tk.Label(self.attendance_tab, text="Member ID")
        self.attendance_member_id_entry = tk.Entry(self.attendance_tab)
        self.check_in_button = tk.Button(self.attendance_tab, text="Check In", command=self.check_in)
        self.check_out_button = tk.Button(self.attendance_tab, text="Check Out", command=self.check_out)
        self.attendance_history_button = tk.Button(self.attendance_tab, text="Attendance History",
                                                   command=self.show_attendance_history)
        self.attendance_list_text = tk.Text(self.attendance_tab, height=10, width=50)

        self.attendance_member_id_label.grid(row=0, column=0, padx=10, pady=10)
        self.attendance_member_id_entry.grid(row=0, column=1, padx=10, pady=10)
        self.check_in_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
        self.check_out_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
        self.attendance_history_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
        self.attendance_list_text.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    def check_in(self):
        member_id = self.attendance_member_id_entry.get()
        if not member_id:
            messagebox.showerror("Input Error", "Member ID is required.")
            return

        try:
            member_id = int(member_id)
        except ValueError:
            messagebox.showerror("Input Error", "Member ID must be an integer.")
            return

        success = self.gym_system.check_in(member_id)
        if success:
            messagebox.showinfo("Check-In Successful", f"Member ID {member_id} checked in")
        else:
            messagebox.showerror("Error", "Member not found")

    def check_out(self):
        member_id = self.attendance_member_id_entry.get()
        if not member_id:
            messagebox.showerror("Input Error", "Member ID is required.")
            return

        try:
            member_id = int(member_id)
        except ValueError:
            messagebox.showerror("Input Error", "Member ID must be an integer.")
            return

        success = self.gym_system.check_out(member_id)
        if success:
            messagebox.showinfo("Check-Out Successful", f"Member ID {member_id} checked out")
        else:
            messagebox.showerror("Error", "Member not found")

    def show_attendance_history(self):
        member_id = simpledialog.askinteger("Attendance History", "Enter member ID:")
        if not member_id:
            return

        attendance = self.gym_system.get_attendance_history(member_id)
        if attendance:
            self.attendance_list_text.delete(1.0, tk.END)
            for record in attendance:
                self.attendance_list_text.insert(tk.END, f"Action: {record['action']}, Time: {record['time']}\n")
        else:
            messagebox.showerror("Error", "Member not found or no attendance records")

    def create_workout_tab(self):
        self.workout_member_id_label = tk.Label(self.workout_tab, text="Member ID")
        self.workout_member_id_entry = tk.Entry(self.workout_tab)
        self.workout_log_label = tk.Label(self.workout_tab, text="Workout Log")
        self.workout_log_entry = tk.Entry(self.workout_tab)
        self.add_workout_log_button = tk.Button(self.workout_tab, text="Add Workout Log", command=self.add_workout_log)

        self.workout_member_id_label.grid(row=0, column=0, padx=10, pady=10)
        self.workout_member_id_entry.grid(row=0, column=1, padx=10, pady=10)
        self.workout_log_label.grid(row=1, column=0, padx=10, pady=10)
        self.workout_log_entry.grid(row=1, column=1, padx=10, pady=10)
        self.add_workout_log_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    def add_workout_log(self):
        member_id = self.workout_member_id_entry.get()
        workout_log = self.workout_log_entry.get()
        if not (member_id and workout_log):
            messagebox.showerror("Input Error", "All fields are required.")
            return

        try:
            member_id = int(member_id)
        except ValueError:
            messagebox.showerror("Input Error", "Member ID must be an integer.")
            return

        success = self.gym_system.add_workout_log(member_id, workout_log)
        if success:
            messagebox.showinfo("Workout Log Added", f"Workout log added for member ID {member_id}")
        else:
            messagebox.showerror("Error", "Member not found")

    def create_photo_tab(self):
        self.photo_member_id_label = tk.Label(self.photo_tab, text="Member ID")
        self.photo_member_id_entry = tk.Entry(self.photo_tab)
        self.browse_photo_button = tk.Button(self.photo_tab, text="Browse Photo", command=self.browse_photo)
        self.add_photo_button = tk.Button(self.photo_tab, text="Add Photo", command=self.add_photo)

        self.photo_member_id_label.grid(row=0, column=0, padx=10, pady=10)
        self.photo_member_id_entry.grid(row=0, column=1, padx=10, pady=10)
        self.browse_photo_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
        self.add_photo_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    def browse_photo(self):
        self.photo_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
        if self.photo_path:
            messagebox.showinfo("Photo Selected", f"Photo selected: {self.photo_path}")

    def add_photo(self):
        member_id = self.photo_member_id_entry.get()
        if not (member_id and self.photo_path):
            messagebox.showerror("Input Error", "Member ID and photo are required.")
            return

        try:
            member_id = int(member_id)
        except ValueError:
            messagebox.showerror("Input Error", "Member ID must be an integer.")
            return

        success = self.gym_system.add_photo(member_id, self.photo_path)
        if success:
            messagebox.showinfo("Photo Added", f"Photo added for member ID {member_id}")
        else:
            messagebox.showerror("Error", "Member not found")


if __name__ == "__main__":
    gym_system = GymManagementSystem()
    gui = GymManagementGUI(gym_system)
    gui.mainloop()