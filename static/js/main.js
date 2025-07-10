document.getElementById("uploadForm").addEventListener("submit", async function (e) {
  e.preventDefault();

  const fileInput = document.getElementById("imageUpload");
  const file = fileInput.files[0];
  if (!file) {
    alert("Please select an image.");
    return;
  }

  // Show image preview
  const preview = document.getElementById("preview");
  preview.src = URL.createObjectURL(file);
  preview.style.display = "block";

  // Show loading text
  const resultDiv = document.getElementById("result");
  resultDiv.innerText = "⏳ Predicting...";

  const formData = new FormData();
  formData.append("file", file);

  try {
    const response = await fetch("/predict", {
      method: "POST",
      body: formData
    });

    const data = await response.json();
    resultDiv.innerText = `🧾 Result: ${data.prediction}`;
  } catch (error) {
    console.error(error);
    resultDiv.innerText = "❌ Error predicting result. Try again.";
  }
});
