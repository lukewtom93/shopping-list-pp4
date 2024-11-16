
document.addEventListener("DOMContentLoaded", () => {
    const itemsList = document.getElementById("items-list");
    

    itemsList.addEventListener("click", (event) => {
        const target = event.target;


        if (target.classList.contains("shopping-item")) {
            target.classList.toggle("completed");
  
        
        const itemId = target.getAttribute("data-item-id");
        const Completed = target.classList.contains("completed");

        fetch(`/update-completed-item/${itemId}/`, {
            method: "POST",
            headers: {
                "Content-Type": "aplication/json",
                "X-CSRFToken": getCsrfToken(),
            },
            body: JSON.stringify({ complete: Completed }),
        })
    }
});

    function getCsrfToken() {
        const cookieValue = document.cookie
            .split("; ")
            .find(row => row.startsWith("csrftoken="))
            ?.split("=")[1];
        return cookieValue;
    }
});



