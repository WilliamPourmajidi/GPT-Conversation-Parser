import json

def find_and_save_entry_by_title(input_file, desired_title):
  """
  Finds the entry with the specified title in a JSON file and saves it as a separate file.

  Args:
      input_file (str): Path to the input JSON file.
      desired_title (str): The title of the entry you're looking for.
  """

  with open(input_file, 'r') as f:
    data = json.load(f)

  # Find the entry with the desired title
  desired_entry = next((entry for entry in data if entry.get("title") == desired_title), None)

  if desired_entry:
    # Create the filename based on the title
    filename = f"{desired_title}.json"

    # Save the entry as a JSON file with indentation
    with open(filename, 'w') as f:
      json.dump(desired_entry, f, indent=4)

    print(f"Entry with title '{desired_title}' saved to '{filename}'.")
  else:
    print(f"Entry with title '{desired_title}' not found in the provided data.")

# Example usage
# By Defauly the ChatGPT exported file that contains all the converrsations is called "conversations.json".
input_file = "conversations.json"
desired_title = "The exact name of the conversation you want to export as a JSON file"

find_and_save_entry_by_title(input_file, desired_title)

