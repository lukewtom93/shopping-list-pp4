describe("Shopping item click behavior", () => {
    beforeEach(() => {
        // Mock DOM
        document.body.innerHTML = `
            <ul id="items-list">
                <li class="shopping-item" data-item-id="42">Milk</li>
            </ul>
        `;

        // Set mock CSRF cookie
        Object.defineProperty(document, 'cookie', {
            writable: true,
            value: "csrftoken=testcsrftoken"
        });

        // Mock fetch
        global.fetch = jest.fn(() => Promise.resolve({
            ok: true,
            json: () => Promise.resolve({})
        }));

        // Load script logic (simulate DOMContentLoaded)
        require('../script');
        document.dispatchEvent(new Event('DOMContentLoaded'));
    });

    afterEach(() => {
        jest.resetModules();
        fetch.mockClear();
    });

    it("toggles 'completed' class and sends fetch request with correct data", async () => {
        const item = document.querySelector(".shopping-item");
        
        // Initial state: not completed
        expect(item.classList.contains("completed")).toBe(false);

        // Simulate click
        item.click();

        // Check class toggled
        expect(item.classList.contains("completed")).toBe(true);

        // Check fetch called correctly
        expect(fetch).toHaveBeenCalledWith("/update-completed-item/42/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": "testcsrftoken"
            },
            body: JSON.stringify({ complete: true })
        });
    });
});