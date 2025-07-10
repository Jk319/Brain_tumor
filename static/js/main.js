document.getElementById('uploadForm').addEventListener('submit', async function (e) {
  e.preventDefault();

  const fileInput = document.getElementById('imageFile');
  const file = fileInput.files[0];

  if (!file) {
    alert("Please select an image file!");
    return;
  }

  // Show image preview
  const preview = document.getElementById('preview');
  preview.src = URL.createObjectURL(file);

  const formData = new FormData();
  formData.append('file', file);

  document.getElementById('result').innerText = "⏳ Processing...";

  try {
    const res = await fetch('/predict', {
      method: 'POST',
      body: formData
    });

    const data = await res.json();
    document.getElementById('result').innerText = "🧾 Result: " + data.prediction;
  } catch (err) {
    document.getElementById('result').innerText = "❌ Error during prediction.";
  }
});
