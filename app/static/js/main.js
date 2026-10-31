const toggle = document.getElementById("themeToggle");
const savedTheme = localStorage.getItem("leticias-theme") || "warm";
document.body.dataset.theme = savedTheme;
function updateToggle(){
  toggle.querySelector("span").textContent = document.body.dataset.theme === "warm" ? "Classic theme" : "Warm theme";
}
updateToggle();
toggle.addEventListener("click", () => {
  const next = document.body.dataset.theme === "warm" ? "classic" : "warm";
  document.body.dataset.theme = next;
  localStorage.setItem("leticias-theme", next);
  updateToggle();
});
document.getElementById("year").textContent = new Date().getFullYear();
