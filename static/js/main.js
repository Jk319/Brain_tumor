document.getElementById("uploadForm").addEventListener("submit", async function (e) {
  e.preventDefault();

  const fileInput = document.getElementById("imageUpload");
  const file = fileInput.files[0];
  if (!file) {
    alert("Please select an image.");
    return;
  }

  const preview = document.getElementById("preview");
  preview.src = URL.createObjectURL(file);
  preview.style.display = "block";

  const resultDiv = document.getElementById("result");
  resultDiv.innerText = "⏳ Predicting...";

  const formData = new FormData();
  formData.append("file", file);

  try {
    const response = await fetch("/predict", {
      method: "POST",
      body: formData,
    });

    const data = await response.json();
    resultDiv.innerText = `🧾 Result: ${data.prediction}`;
  } catch (error) {
    resultDiv.innerText = "❌ Error in prediction.";
    console.error("Prediction error:", error);
  }
});
