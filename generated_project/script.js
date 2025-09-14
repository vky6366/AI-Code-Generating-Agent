// Initialize the task list
let taskList = [];

// Function to save tasks to local storage
function saveTasksToLocalStorage() {
    localStorage.setItem('taskList', JSON.stringify(taskList));
}

// Function to load tasks from local storage
function loadTasksFromLocalStorage() {
    const storedTasks = localStorage.getItem('taskList');
    if (storedTasks) {
        taskList = JSON.parse(storedTasks);
        renderTasks(); // Render loaded tasks
    }
}

// Function to add a task to the task list
function addTask(taskInput) {
    if (taskInput) {
        taskList.push({ text: taskInput, completed: false }); // Add the task to the list
        updateUI(taskInput); // Update the UI to reflect the new task
        saveTasksToLocalStorage(); // Save to local storage
    }
}

// Function to delete a task from the task list
function deleteTask(index) {
    if (index > -1 && index < taskList.length) {
        taskList.splice(index, 1); // Remove the task from the list
        renderTasks(); // Re-render the tasks
        saveTasksToLocalStorage(); // Save to local storage
    }
}

// Function to mark a task as complete
function markTaskComplete(index) {
    if (index > -1 && index < taskList.length) {
        taskList[index].completed = !taskList[index].completed; // Toggle the completed status
        renderTasks(); // Re-render the tasks to reflect changes
        saveTasksToLocalStorage(); // Save to local storage
    }
}

// Function to re-render the tasks
function renderTasks() {
    const taskListElement = document.querySelector('ul');
    taskListElement.innerHTML = ''; // Clear existing tasks
    taskList.forEach((task, index) => {
        const newTaskElement = document.createElement('li');
        newTaskElement.textContent = task.completed ? '[✔] ' + task.text : task.text;
        const completeButton = document.createElement('button');
        completeButton.textContent = task.completed ? 'Undo' : 'Complete';
        completeButton.onclick = function() { markTaskComplete(index); }; // Set the complete function
        newTaskElement.appendChild(completeButton);
        const deleteButton = document.createElement('button');
        deleteButton.textContent = 'Delete';
        deleteButton.onclick = function() { deleteTask(index); }; // Set the delete function
        newTaskElement.appendChild(deleteButton);
        taskListElement.appendChild(newTaskElement);
    });
}

// Filter Tasks Functionality
function filterTasks(status) {
    const filteredTasks = taskList.filter(task => {
        if (status === 'all') return true;
        if (status === 'completed') return task.completed;
        if (status === 'active') return !task.completed;
    });
    renderFilteredTasks(filteredTasks);
}

// Function to render filtered tasks
function renderFilteredTasks(filteredTasks) {
    const taskListElement = document.querySelector('ul');
    taskListElement.innerHTML = ''; // Clear existing tasks
    filteredTasks.forEach((task, index) => {
        const newTaskElement = document.createElement('li');
        newTaskElement.textContent = task.completed ? '[✔] ' + task.text : task.text;
        const completeButton = document.createElement('button');
        completeButton.textContent = task.completed ? 'Undo' : 'Complete';
        completeButton.onclick = function() { markTaskComplete(index); }; // Set the complete function
        newTaskElement.appendChild(completeButton);
        const deleteButton = document.createElement('button');
        deleteButton.textContent = 'Delete';
        deleteButton.onclick = function() { deleteTask(index); }; // Set the delete function
        newTaskElement.appendChild(deleteButton);
        taskListElement.appendChild(newTaskElement);
    });
}

// Function to update the UI
function updateUI(task) {
    const taskListElement = document.querySelector('ul');
    const newTaskElement = document.createElement('li');
    newTaskElement.textContent = task;
    taskListElement.appendChild(newTaskElement);
}

// Load tasks from local storage on initialization
loadTasksFromLocalStorage();

// Event listener for the submit button
const submitButton = document.querySelector('#submit');
submitButton.addEventListener('click', function() {
    const taskInput = document.querySelector('#taskInput').value;
    addTask(taskInput);
    document.querySelector('#taskInput').value = ''; // Clear input field
});
