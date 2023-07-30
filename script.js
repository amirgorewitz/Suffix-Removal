document.getElementById('uploadForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const formData = new FormData();
    const wordDoc = document.getElementById('wordDoc').files[0];

    formData.append('wordDoc', wordDoc);

    fetch('/process_document', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        // Display the result in the 'result' div
        const resultDiv = document.getElementById('result');
        resultDiv.innerHTML = '<h2>List of Words:</h2><ul>' + data.words.join('<li>') + '</ul>';
    })
    .catch(error => {
        console.error('Error:', error);
    });
});
