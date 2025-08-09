import mysql.connector as sqltor
import tkinter as tk
from tkinter import ttk, messagebox

class ProgrammingLanguageDB:
    def __init__(self, root):
        self.root = root
        self.root.title("Programming Language Database")
        self.root.geometry("800x600")
        
        # Database connection parameters
        self.db_config = {
            'host': 'localhost',
            'user': 'root',
            'password': 'root',
            'database': 'programming_language'
        }
        
        self.create_widgets()
    
    def create_widgets(self):
        # Create notebook (tabs)
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill='both', expand=True)
        
        # Create frames for each tab
        self.add_tab = ttk.Frame(self.notebook)
        self.delete_tab = ttk.Frame(self.notebook)
        self.update_tab = ttk.Frame(self.notebook)
        self.search_tab = ttk.Frame(self.notebook)
        self.view_tab = ttk.Frame(self.notebook)
        
        self.notebook.add(self.add_tab, text="Add Record")
        self.notebook.add(self.delete_tab, text="Delete Record")
        self.notebook.add(self.update_tab, text="Update Rating")
        self.notebook.add(self.search_tab, text="Search by ID")
        self.notebook.add(self.view_tab, text="View All Records")
        
        # Add Record Tab
        self.create_add_tab()
        
        # Delete Record Tab
        self.create_delete_tab()
        
        # Update Rating Tab
        self.create_update_tab()
        
        # Search Tab
        self.create_search_tab()
        
        # View All Tab
        self.create_view_tab()
    
    def create_add_tab(self):
        # Labels
        ttk.Label(self.add_tab, text="Language ID:").grid(row=0, column=0, padx=10, pady=5, sticky='e')
        ttk.Label(self.add_tab, text="Language Name:").grid(row=1, column=0, padx=10, pady=5, sticky='e')
        ttk.Label(self.add_tab, text="Creator Name:").grid(row=2, column=0, padx=10, pady=5, sticky='e')
        ttk.Label(self.add_tab, text="Release Date:").grid(row=3, column=0, padx=10, pady=5, sticky='e')
        ttk.Label(self.add_tab, text="Version:").grid(row=4, column=0, padx=10, pady=5, sticky='e')
        ttk.Label(self.add_tab, text="Rating:").grid(row=5, column=0, padx=10, pady=5, sticky='e')
        
        # Entry widgets
        self.lid_entry = ttk.Entry(self.add_tab)
        self.name_entry = ttk.Entry(self.add_tab)
        self.cname_entry = ttk.Entry(self.add_tab)
        self.rdate_entry = ttk.Entry(self.add_tab)
        self.version_entry = ttk.Entry(self.add_tab)
        self.rating_entry = ttk.Entry(self.add_tab)
        
        self.lid_entry.grid(row=0, column=1, padx=10, pady=5)
        self.name_entry.grid(row=1, column=1, padx=10, pady=5)
        self.cname_entry.grid(row=2, column=1, padx=10, pady=5)
        self.rdate_entry.grid(row=3, column=1, padx=10, pady=5)
        self.version_entry.grid(row=4, column=1, padx=10, pady=5)
        self.rating_entry.grid(row=5, column=1, padx=10, pady=5)
        
        # Submit button
        ttk.Button(self.add_tab, text="Add Record", command=self.insert_record).grid(row=6, column=0, columnspan=2, pady=10)
    
    def create_delete_tab(self):
        ttk.Label(self.delete_tab, text="Language ID to Delete:").grid(row=0, column=0, padx=10, pady=10, sticky='e')
        
        self.delete_id_entry = ttk.Entry(self.delete_tab)
        self.delete_id_entry.grid(row=0, column=1, padx=10, pady=10)
        
        ttk.Button(self.delete_tab, text="Delete Record", command=self.delete_record).grid(row=1, column=0, columnspan=2, pady=10)
    
    def create_update_tab(self):
        ttk.Label(self.update_tab, text="Language ID:").grid(row=0, column=0, padx=10, pady=5, sticky='e')
        ttk.Label(self.update_tab, text="Rating Change (+/-):").grid(row=1, column=0, padx=10, pady=5, sticky='e')
        
        self.update_id_entry = ttk.Entry(self.update_tab)
        self.rating_change_entry = ttk.Entry(self.update_tab)
        
        self.update_id_entry.grid(row=0, column=1, padx=10, pady=5)
        self.rating_change_entry.grid(row=1, column=1, padx=10, pady=5)
        
        ttk.Button(self.update_tab, text="Update Rating", command=self.update_rating).grid(row=2, column=0, columnspan=2, pady=10)
    
    def create_search_tab(self):
        ttk.Label(self.search_tab, text="Language ID to Search:").grid(row=0, column=0, padx=10, pady=10, sticky='e')
        
        self.search_id_entry = ttk.Entry(self.search_tab)
        self.search_id_entry.grid(row=0, column=1, padx=10, pady=10)
        
        ttk.Button(self.search_tab, text="Search", command=self.search_record).grid(row=1, column=0, columnspan=2, pady=10)
        
        # Result display
        self.search_result = tk.Text(self.search_tab, height=10, width=60, state='disabled')
        self.search_result.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
    
    def create_view_tab(self):
        # Treeview to display records
        columns = ("ID", "Name", "Creator", "Release Date", "Version", "Rating")
        self.records_tree = ttk.Treeview(self.view_tab, columns=columns, show='headings')
        
        for col in columns:
            self.records_tree.heading(col, text=col)
            self.records_tree.column(col, width=100, anchor='center')
        
        self.records_tree.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Refresh button
        ttk.Button(self.view_tab, text="Refresh Records", command=self.show_all_records).pack(pady=10)
    
    def db_connect(self):
        try:
            return sqltor.connect(**self.db_config)
        except sqltor.Error as err:
            messagebox.showerror("Database Error", f"Error connecting to database: {err}")
            return None
    
    def insert_record(self):
        try:
            lid = int(self.lid_entry.get())
            name = self.name_entry.get()
            cname = self.cname_entry.get()
            rdate = self.rdate_entry.get()
            version = int(self.version_entry.get())
            rating = int(self.rating_entry.get())
            
            mycon = self.db_connect()
            if mycon is None:
                return
                
            qry = "INSERT INTO program VALUES (%s, %s, %s, %s, %s, %s)"
            cur = mycon.cursor()
            cur.execute(qry, (lid, name, cname, rdate, version, rating))
            mycon.commit()
            mycon.close()
            
            messagebox.showinfo("Success", "Record added successfully!")
            
            # Clear fields
            self.lid_entry.delete(0, 'end')
            self.name_entry.delete(0, 'end')
            self.cname_entry.delete(0, 'end')
            self.rdate_entry.delete(0, 'end')
            self.version_entry.delete(0, 'end')
            self.rating_entry.delete(0, 'end')
            
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numbers for ID, Version, and Rating")
        except sqltor.Error as err:
            messagebox.showerror("Database Error", f"Error inserting record: {err}")
    
    def delete_record(self):
        try:
            lid = int(self.delete_id_entry.get())
            
            mycon = self.db_connect()
            if mycon is None:
                return
                
            cur = mycon.cursor()
            qry = "DELETE FROM program WHERE lid = %s"
            cur.execute(qry, (lid,))
            
            if cur.rowcount == 0:
                messagebox.showinfo("Info", "No record found with that ID")
            else:
                mycon.commit()
                messagebox.showinfo("Success", "Record deleted successfully!")
            
            mycon.close()
            self.delete_id_entry.delete(0, 'end')
            
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid ID number")
        except sqltor.Error as err:
            messagebox.showerror("Database Error", f"Error deleting record: {err}")
    
    def update_rating(self):
        try:
            rating_change = int(self.rating_change_entry.get())
            lid = int(self.update_id_entry.get())
            
            mycon = self.db_connect()
            if mycon is None:
                return
                
            cur = mycon.cursor()
            qry = "UPDATE program SET rating = rating + %s WHERE lid = %s"
            cur.execute(qry, (rating_change, lid))
            
            if cur.rowcount == 0:
                messagebox.showinfo("Info", "No record found with that ID")
            else:
                mycon.commit()
                messagebox.showinfo("Success", "Rating updated successfully!")
            
            mycon.close()
            self.update_id_entry.delete(0, 'end')
            self.rating_change_entry.delete(0, 'end')
            
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numbers for ID and Rating Change")
        except sqltor.Error as err:
            messagebox.showerror("Database Error", f"Error updating rating: {err}")
    
    def search_record(self):
        try:
            lid = int(self.search_id_entry.get())
            
            mycon = self.db_connect()
            if mycon is None:
                return
                
            cur = mycon.cursor()
            qry = "SELECT * FROM program WHERE lid = %s"
            cur.execute(qry, (lid,))
            data = cur.fetchall()
            mycon.close()
            
            self.search_result.config(state='normal')
            self.search_result.delete(1.0, 'end')
            
            if not data:
                self.search_result.insert('end', "No record found with that ID")
            else:
                for rec in data:
                    self.search_result.insert('end', f"ID: {rec[0]}\n")
                    self.search_result.insert('end', f"Name: {rec[1]}\n")
                    self.search_result.insert('end', f"Creator: {rec[2]}\n")
                    self.search_result.insert('end', f"Release Date: {rec[3]}\n")
                    self.search_result.insert('end', f"Version: {rec[4]}\n")
                    self.search_result.insert('end', f"Rating: {rec[5]}\n")
                    self.search_result.insert('end', "\n")
            
            self.search_result.config(state='disabled')
            self.search_id_entry.delete(0, 'end')
            
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid ID number")
        except sqltor.Error as err:
            messagebox.showerror("Database Error", f"Error searching record: {err}")
    
    def show_all_records(self):
        try:
            mycon = self.db_connect()
            if mycon is None:
                return
                
            cur = mycon.cursor()
            qry = "SELECT * FROM program"
            cur.execute(qry)
            data = cur.fetchall()
            mycon.close()
            
            # Clear existing data in treeview
            for item in self.records_tree.get_children():
                self.records_tree.delete(item)
            
            # Insert new data
            for rec in data:
                self.records_tree.insert('', 'end', values=rec)
                
        except sqltor.Error as err:
            messagebox.showerror("Database Error", f"Error fetching records: {err}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ProgrammingLanguageDB(root)
    root.mainloop()
