async function askQuestion() {
  const question = document.getElementById("question").value;
  const response = await fetch(`/ask?question=${encodeURIComponent(question)}`);
  const data = await response.json();
  document.getElementById("answer").innerText = data.answer || data.error;
}
