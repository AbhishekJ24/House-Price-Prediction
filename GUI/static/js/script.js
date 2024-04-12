document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('predictionForm');
    form.addEventListener('submit', async (e) => {
      e.preventDefault();
      const formData = new FormData(form);
      const response = await fetch('/predict', {
        method: 'POST',
        body: formData
      });
      const data = await response.json();
      const resultDiv = document.getElementById('result');
      resultDiv.innerText = `Predicted Price: $${data.price}`;
    });
  });
  