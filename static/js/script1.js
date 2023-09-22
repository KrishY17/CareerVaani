
const form = document.getElementById('sampleForm');
document.getElementById('sampleForm').addEventListener('submit', function(event) {
    event.preventDefault();

    // Loop through all questions (q1 to q105)
    for (let i = 1; i <= 105; i++) {
        const selectedOption = document.querySelector(`input[name="q${i}"]:checked`);
        if (!selectedOption) {
            alert('Attempt all the questions');
            return; // Prevent form submission if any question is unanswered
        }
    }
    const formData = new FormData(form);

    // If all questions are answered, you can submit the form or perform other actions
    fetch('/predictswot', {
        method: 'POST',
        body: formData
       
    }).then(response => {
        if (response.ok) {
            window.location.href = '/predictswot';
        }
    });
 
});
