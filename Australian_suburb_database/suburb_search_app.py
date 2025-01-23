import os
import pandas as pd
import tkinter as tk
from tkinter import ttk, messagebox
from fuzzywuzzy import process
import threading  # To handle long-running tasks without freezing the UI


class SuburbSearchApp:
    def __init__(self, root):
        self.root = root
        self.root.title("City/Suburb Search Tool")
        self.root.geometry("1000x600")
        self.threshold = 80  # Set the similarity threshold

        # Load the CSV file bundled with the executable
        try:
            file_path = os.path.join(os.path.dirname(__file__), "all_in_one_australian_cities.csv")
            self.csv_data = pd.read_csv(file_path)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load the CSV file: {e}")
            self.csv_data = None
            return

        # Search Entry
        self.search_label = ttk.Label(root, text="Search City or Suburb:")
        self.search_label.pack(pady=10)
        self.search_entry = ttk.Entry(root, width=50)
        self.search_entry.pack(pady=5)

        # Search Button
        self.search_button = ttk.Button(root, text="Search", command=self.start_search)
        self.search_button.pack(pady=10)

        # Loading Label
        self.loading_label = ttk.Label(root, text="", foreground="blue")
        self.loading_label.pack(pady=5)

        # Results Table
        self.results_tree = ttk.Treeview(root, show="headings", height=20)
        self.results_tree.pack(pady=10, fill="both", expand=True)

    def start_search(self):
        """Start the search in a separate thread to avoid freezing the UI."""
        if self.csv_data is None:
            messagebox.showerror("Error", "CSV data could not be loaded!")
            return

        search_term = self.search_entry.get().strip().lower()
        if not search_term:
            messagebox.showerror("Error", "Search term cannot be empty!")
            return

        # Show "Searching..." label
        self.loading_label.config(text="Searching...")

        # Start the search in a separate thread
        thread = threading.Thread(target=self.search_data, args=(search_term,))
        thread.start()

    def search_data(self, search_term):
        # Perform fuzzy matching on suburbname and cityname
        suburb_matches = process.extract(search_term, self.csv_data['suburbname'], limit=len(self.csv_data))
        city_matches = process.extract(search_term, self.csv_data['cityname'], limit=len(self.csv_data))

        # Filter results based on the similarity threshold
        suburb_filtered = [match for match in suburb_matches if match[1] >= self.threshold]
        city_filtered = [match for match in city_matches if match[1] >= self.threshold]

        # Collect the filtered row indices
        suburb_indices = [self.csv_data[self.csv_data['suburbname'] == match[0]].index[0] for match in suburb_filtered]
        city_indices = [self.csv_data[self.csv_data['cityname'] == match[0]].index[0] for match in city_filtered]

        # Combine the results, remove duplicates
        all_indices = list(set(suburb_indices + city_indices))
        results = self.csv_data.iloc[all_indices]

        # Update the Treeview in the main thread
        self.root.after(0, self.display_results, results)

    def display_results(self, results):
        """Display the search results in the Treeview."""
        # Clear existing results
        for row in self.results_tree.get_children():
            self.results_tree.delete(row)

        if results.empty:
            messagebox.showinfo("No Results", "No matches found for the given search term!")
            self.loading_label.config(text="")  # Hide "Searching..." label
            return

        # Set up TreeView columns dynamically based on CSV data
        self.results_tree["columns"] = list(results.columns)
        for col in results.columns:
            self.results_tree.heading(col, text=col)
            self.results_tree.column(col, width=100, anchor="center")

        for _, row in results.iterrows():
            self.results_tree.insert("", "end", values=list(row))

        # Hide "Searching..." label
        self.loading_label.config(text="")


if __name__ == "__main__":
    root = tk.Tk()
    app = SuburbSearchApp(root)
    root.mainloop()
