
// javascript to apply completed class and update database
document.addEventListener("DOMContentLoaded", () => {
    const itemsList = document.getElementById("items-list");



    itemsList.addEventListener("click", (event) => {
        const target = event.target;


        if (target.classList.contains("shopping-item")) {
            target.classList.toggle("completed");
  
        
        const itemId = target.getAttribute("data-item-id");
        const Completed = target.classList.contains("completed");

        // Requst to update item status
        fetch(`/update-completed-item/${itemId}/`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": getCsrfToken(),
            },
            body: JSON.stringify({ complete: Completed }),
        })
    }
});
    // Helper Function to get CSRF token
    function getCsrfToken() {
        const cookieValue = document.cookie
            .split("; ")
            .find(row => row.startsWith("csrftoken="))
            ?.split("=")[1];
        return cookieValue;
    }
});




