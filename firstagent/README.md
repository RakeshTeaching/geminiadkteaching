# Gemini ADK Teaching - Multi-Tool Agent Example

This directory contains an example of a multi-tool agent built using the Google Gemini Agent Development Kit (ADK). This agent demonstrates how to create a simple to-do list manager with two tools: one for adding items and one for listing items.

## Project Structure

- `multi_tool_agent/agent.py`: Contains the core logic for the Gemini agent, including the `add_to_do_item` and `list_to_do_items` functions, and the agent definition.
- `multi_tool_agent/__init__.py`: An empty file indicating that `multi_tool_agent` is a Python package.
- `multi_tool_agent/.env`: (Optional) Environment variables for the agent.
- `requirements.txt`: Lists the Python dependencies required for this project.
- `.gitignore`: Specifies intentionally untracked files to ignore.

## Agent Functionality

The `todo_list_agent` is designed to help users manage a simple in-memory to-do list. It exposes the following functionalities:

### `add_to_do_item(item_description: str)`
Adds a new item to the to-do list.
- **Parameters:**
    - `item_description` (str): A description of the item to add.
- **Returns:**
    - `dict`: A status message indicating success or failure.

### `list_to_do_items()`
Lists all items currently on the to-do list.
- **Returns:**
    - `dict`: A list of items or a message if the list is empty.

## How to Use (Conceptual)

To interact with this agent, you would typically:

1.  **Set up your environment:** Ensure you have the Google ADK installed and configured with access to the Gemini model.
2.  **Instantiate the agent:** Load the `root_agent` from `agent.py`.
3.  **Interact with the agent:** Use the ADK's interaction mechanisms to call the `add_to_do_item` and `list_to_do_items` tools.

**Example Interaction (pseudo-code):**

```python
# Assuming you have the ADK set up and the agent loaded
# from firstagent.multi_tool_agent.agent import root_agent

# Add an item
response_add = root_agent.run("Add 'Buy groceries' to my to-do list.")
print(response_add)

# List items
response_list = root_agent.run("What's on my to-do list?")
print(response_list)
```

This README provides a high-level overview. For detailed implementation, refer to the `agent.py` file.
