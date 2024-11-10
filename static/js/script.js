
document.addEventListener("DOMContentLoaded", () => {
    const itemsList = document.getElementById("items-list");

    itemsList.addEventListener("click", (event) => {
        const target = event.target;

        if (target.classList.contains("shopping-item")) {
            target.classList.toggle("completed");
        }}
    )
})

