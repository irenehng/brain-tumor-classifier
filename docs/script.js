const form = document.getElementById('uploadForm');
const resultDiv = document.getElementById('result');
const prevImage = document.getElementById('previewImage');

form.addEventListener('submit', async (event) => {
    event.preventDefault();

    const fileInput = document.getElementById('imageUpload');
    const file = fileInput.files[0];

    if (file) {
        const formData = new FormData();
        formData.append('file', file);

        try {
            const response = await fetch('http://localhost:8000/predict', {
                method: 'POST',
                body: formData,
            });

            const data = await response.json();
            resultDiv.innerText = `Class: ${data.class}, Confidence: ${data.confidence}`;
        } catch (error) {
            console.error('Error:', error);
        }
    }
});
function displayImage(event) {
  const file = event.target.files[0];
  const reader = new FileReader();

  reader.onload = function (e) {
    prevImage.src = e.target.result;
  };
  reader.readAsDataURL(file);
}

const fileInput = document.getElementById('imageUpload');
fileInput.addEventListener('change', displayImage);