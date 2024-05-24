import json

def find_entry_by_title(input_file, desired_title):
  """
  Finds and returns the entry with the specified title from a JSON file.

  Args:
      input_file (str): Path to the input JSON file.
      desired_title (str): The title of the entry you're looking for.

  Returns:
      dict: The entry with the matching title, or None if not found.
  """

  with open(input_file, 'r') as f:
    data = json.load(f)

  # Find the entry with the desired title
  desired_entry = next((entry for entry in data if entry.get("title") == desired_title), None)

  return desired_entry

# Example usage
input_file = "conversations.json"
desired_title = "CNA-Governance-Paper"

entry = find_entry_by_title(input_file, desired_title)

if entry:
  print(json.dumps(entry, indent=4))  # Print the desired entry with indentation
else:
  print(f"Entry with title '{desired_title}' not found in the provided data.")
