let input = document.querySelector("input");
let button = document.querySelector(".addingButton");

button.addEventListener("click", addTask);

function addTask(event) {
    let container = document.querySelector(".container");
    
    let newTask = document.createElement("p");
    let checkButton = document.createElement("data"); // ???
    let deleteButton = document.createElement("data");

    checkButton.innerHTML = "<input type=\"checkbox\" class=\"checkerBox\">";
    deleteButton.innerHTML = "<i class=\"fa fa-trash\"></i>";

    checkButton.classList.add("checkerBox");
    deleteButton.classList.add("deleteBox");
    newTask.classList.add("taskText");

    if(input.value !== "") {
        newTask.innerText = input.value;
        input.value = "";
        container.appendChild(checkButton);
        container.appendChild(newTask);
        container.appendChild(deleteButton);
    }

    checkButton.addEventListener("click", function() {
        if( newTask.style.textDecoration == "line-through" ) {
            newTask.style.textDecoration = "none"; 
        } else {
            newTask.style.textDecoration = "line-through";
        }
    } ); 

    deleteButton.addEventListener("click", function() {
        container.removeChild(checkButton);
        container.removeChild(newTask);
        container.removeChild(deleteButton);
    } );
}