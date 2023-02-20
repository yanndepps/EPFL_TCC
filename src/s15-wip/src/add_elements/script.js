// Add elements
const btn = document.getElementById("btn");
const txt = document.getElementById("txt");
const content = document.getElementById("content");


btn.addEventListener("click", () => {
	const newPrg = document.createElement("p");
	newPrg.innerText = txt.value;
	newPrg.className = "nofun";
	content.appendChild(newPrg);
});
