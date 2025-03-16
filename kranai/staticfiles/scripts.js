document.addEventListener('DOMContentLoaded', () => {
    // Lentelės eilučių paspaudimo logika
    const rows = document.querySelectorAll('.document-row');
    rows.forEach(row => {
        row.addEventListener('click', () => {
            const url = row.getAttribute('data-url');
            if (url) {
                window.location.href = url;
            }
        });
    });

    // Tamsos režimo perjungimas
    const themeToggleButton = document.querySelector('.btn-light');
    if (themeToggleButton) {
        themeToggleButton.addEventListener('click', toggleTheme);
    }
});

function toggleTheme() {
    document.body.classList.toggle('dark-mode');
    document.body.classList.toggle('light-mode');
}


document.addEventListener("DOMContentLoaded", function() {
    const vehicleSelect = document.getElementById("vehicle-select");
    const modelField = document.getElementById("vehicle-model");

    if (vehicleSelect && modelField) {
        vehicleSelect.addEventListener("change", function() {
            const regNumber = this.value;
            if (regNumber) {
                fetch(`/get_vehicle_model/?registration_number=${regNumber}`)
                    .then(response => response.json())
                    .then(data => {
                        modelField.value = data.model;  // Automatiškai užpildo modelį
                    })
                    .catch(error => console.error("Klaida gaunant modelį:", error));
            } else {
                modelField.value = "";
            }
        });
    }
});
