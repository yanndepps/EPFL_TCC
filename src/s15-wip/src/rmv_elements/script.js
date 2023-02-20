// Add elements
const addBtn = document.getElementById("addBtn");
const txt = document.getElementById("txt");
const content = document.getElementById("content");
const title = document.getElementById("title");
const main = document.getElementById("main");
const rmvBtn = document.getElementById("rmvBtn");


addBtn.addEventListener("click", () => {
	const newPrg = document.createElement("p");
	newPrg.innerText = txt.value;
	newPrg.className = "myclass";
	content.appendChild(newPrg);
});

rmvBtn.addEventListener("click", () => {
	const paragraphs = document.getElementsByClassName("myclass");
	if (paragraphs.length > 0) {
		content.removeChild(paragraphs[0]);
	}
});
