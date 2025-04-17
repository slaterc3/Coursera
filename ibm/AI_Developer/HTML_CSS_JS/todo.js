// Function to add a task
function addTask() {
  // 1. Get the input element and its current text value
  const input = document.getElementById("taskInput"); // Find the HTML element with the ID "taskInput" (your text box)
  const taskText = input.value.trim(); // Get the text typed into the input box (.value)
  // and remove extra spaces from the beginning/end (.trim())

  // 2. Check if the user actually typed something (after trimming spaces)
  if (taskText !== "") {
    // If the taskText is NOT an empty string... proceed to add the task

    // 3. Get the unordered list (<ul>) element where tasks will be added
    const ul = document.getElementById("todoList"); // Find the HTML element with ID "todoList" (your <ul> tag)

    // --- Create the necessary HTML elements for the new task ---
    // These elements are created in JavaScript's memory first, they aren't on the page yet.

    // 4. Create a new list item element (<li>)
    const li = document.createElement("li"); // Creates an empty <li></li> element

    // 5. Create a span element (<span>) to hold the task text
    const span = document.createElement("span"); // Creates an empty <span></span> element
    span.textContent = taskText; // Set the text inside the span to be the task text the user entered
    // Now it's conceptually: <span>User's Task Text</span>

    // 6. Create the "Edit" button element (<button>)
    const editButton = document.createElement("button"); // Creates an empty <button></button>
    editButton.textContent = "Edit"; // Set the text visible on the button
    // Now it's: <button>Edit</button>
    // Set up what happens when THIS new Edit button is clicked:
    editButton.onclick = () => editTask(span);
    // () => ... : This defines an action (an arrow function) to run on click.
    // editTask(span) : It calls another function named 'editTask' (defined elsewhere, maybe Exercise 3).
    // It passes the 'span' element (containing the task text) to 'editTask',
    // so the 'editTask' function knows WHICH task's text needs editing.

    // 7. Create the "Delete" button element (<button>)
    const removeButton = document.createElement("button"); // Creates another empty <button></button>
    removeButton.textContent = "Delete"; // Set the button's text: <button>Delete</button>
    // Set up what happens when THIS new Delete button is clicked:
    removeButton.onclick = () => removeTask(li);
    // () => ... : Defines the click action.
    // removeTask(li) : It calls another function named 'removeTask' (defined elsewhere, maybe Exercise 4).
    // It passes the entire list item 'li' element to 'removeTask',
    // so the 'removeTask' function knows WHICH list item to remove from the page.

    // --- Assemble the new list item ---
    // Now, put the pieces (span, buttons) inside the list item (li).

    // 8. Append the text span and buttons as children of the list item (li)
    li.appendChild(span); // Makes the li look like: <li><span>User's Task Text</span></li>
    li.appendChild(editButton); // Appends the Edit button: <li><span>...</span><button>Edit</button></li>
    li.appendChild(removeButton); // Appends the Delete button: <li><span>...</span><button>Edit</button><button>Delete</button></li>

    // --- Add the completed list item to the page ---
    // Now, take the fully formed 'li' and add it to the visible list on the webpage.

    // 9. Append the new list item (li) to the main unordered list (ul)
    ul.appendChild(li); // This makes the new task appear on the screen within the <ul> identified by "todoList".

    // --- Clean up ---

    // 10. Clear the input field for the next task
    input.value = ""; // Set the text in the input box back to empty.
  } else {
    // This 'else' corresponds to the 'if (taskText !== "")' check earlier
    // 11. If the input was empty, show an alert message
    alert("Please enter a valid task."); // Display a pop-up warning the user.
  }
} // End of the addTask function

// Function to edit an existing task
function editTask(span) {
  // 'span' here is the specific <span> element passed from the onclick event

  // 1. Ask the user for the new task description using a prompt dialog
  const newTask = prompt("Edit your task:", span.textContent);
  // prompt(): This built-in browser function displays a small pop-up window with:
  //    - A message ("Edit your task:")
  //    - An input field
  //    - An "OK" button and a "Cancel" button.
  // span.textContent: This gets the CURRENT text content of the specific span element
  //                   that was passed into the function. This current text is put into
  //                   the prompt's input field as the default value, making it easy
  //                   for the user to see what they are editing.

  // What 'prompt' returns (stored in 'newTask'):
  // - If user types text and clicks OK -> returns the typed text (string).
  // - If user clicks OK without typing -> returns an empty string ("").
  // - If user clicks Cancel or closes the prompt -> returns null.

  // 2. Check if the user provided valid input (didn't cancel and didn't leave it empty)
  if (newTask !== null && newTask.trim() !== "") {
    // newTask !== null: Checks if the user clicked "OK" (didn't cancel).
    // &&: Logical AND - both conditions must be true.
    // newTask.trim() !== "": Checks if the text entered, after removing leading/trailing
    //                       whitespace, is not an empty string. This handles cases
    //                       where the user clicks OK but leaves the field blank or just types spaces.

    // 3. If the input is valid, update the original span's text content
    span.textContent = newTask.trim(); // Directly change the text inside the original span element
    // to the new, trimmed text provided by the user.
    // Because 'span' is a direct reference to the element
    // on the page (in the DOM), changing its textContent
    // immediately updates what the user sees in the browser.
  }
  // If the user clicked Cancel (newTask is null) or entered empty text,
  // the code inside the 'if' block is skipped, and nothing changes.
}
// Function to remove a task from the to-do list
function removeTask(task) {
  const ul = document.getElementById("todoList"); // Get the list container
  ul.removeChild(task); // Remove the specified task element
}
