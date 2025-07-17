document.getElementById('uploadForm').addEventListener('submit', async function (e) {
  e.preventDefault();

  const fileInput = document.getElementById('imageFile');
  const file = fileInput.files[0];

  if (!file) {
    alert("📸 Please select an image file from gallery or camera!");
    return;
  }

  // ✅ DEBUG: Log selected file info
  console.log("✅ Selected file:", file);
  console.log("📂 File name:", file.name);
  console.log("📏 File size:", file.size);
  console.log("📄 File type:", file.type);

  // ✅ Show preview
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

    if (!res.ok) {
      const errText = await res.text();
      console.error("❌ Server error:", errText);
      document.getElementById('result').innerText = `❌ Server returned ${res.status}`;
      return;
    }

    const data = await res.json();

    if (data.prediction) {
      document.getElementById('result').innerText = "🧾 Result: " + data.prediction;
    } else if (data.error) {
      document.getElementById('result').innerText = "❌ Error: " + data.error;
    } else {
      document.getElementById('result').innerText = "❌ Unexpected response from server.";
    }

  } catch (err) {
    console.error("❌ JS Fetch error:", err);
    document.getElementById('result').innerText = "❌ Error during prediction.";
  }
});



// document.getElementById('uploadForm').addEventListener('submit', async function (e) {
//   e.preventDefault();

//   const fileInput = document.getElementById('imageFile');
//   const file = fileInput.files[0];

//   if (!file) {
//     alert("Please select an image file!");
//     return;
//   }

//   // Show preview
//   const preview = document.getElementById('preview');
//   preview.src = URL.createObjectURL(file);

//   const formData = new FormData();
//   formData.append('file', file);

//   document.getElementById('result').innerText = "⏳ Processing...";

//   try {
//     const res = await fetch('/predict', {
//       method: 'POST',
//       body: formData
//     });

//     const data = await res.json();

//     // ✅ FIX: Check if 'prediction' key is present
//     if (data.prediction) {
//       document.getElementById('result').innerText = "🧾 Result: " + data.prediction;
//     } else if (data.error) {
//       document.getElementById('result').innerText = "❌ Error: " + data.error;
//     } else {
//       document.getElementById('result').innerText = "❌ Unexpected response from server.";
//     }

//   } catch (err) {
//     document.getElementById('result').innerText = "❌ Error during prediction.";
//   }
// });
