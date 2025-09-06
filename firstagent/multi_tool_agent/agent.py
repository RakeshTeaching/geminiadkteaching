from google.adk.agents import Agent

# This is a simple, in-memory to-do list. In a real application, you'd use a database.
todo_list = []


def add_to_do_item(item_description: str) -> dict:
    """Adds a new item to the to-do list.

    Args:
        item_description (str): A description of the item to add.

    Returns:
        dict: A status message indicating success or failure.
    """
    if not item_description:
        return {"status": "error", "error_message": "Item description cannot be empty."}

    todo_list.append(item_description)
    return {
        "status": "success",
        "message": f"Added '{item_description}' to the to-do list.",
    }


def list_to_do_items() -> dict:
    """Lists all items currently on the to-do list.

    Returns:
        dict: A list of items or a message if the list is empty.
    """
    if not todo_list:
        return {"status": "success", "message": "The to-do list is currently empty."}

    return {"status": "success", "items": todo_list}


root_agent = Agent(
    name="todo_list_agent",
    model="gemini-2.5-flash",
    description="Agent to manage a simple to-do list.",
    instruction="You are a helpful assistant for managing a to-do list. You can add new items and list all existing items.",
    tools=[add_to_do_item, list_to_do_items],
)
