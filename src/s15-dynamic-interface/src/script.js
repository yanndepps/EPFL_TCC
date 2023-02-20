// A dynamic user interface
// ---
// --- Part I
const firstBtn = document.getElementById("firstBtn");
const prg = document.getElementsByTagName('p')[0];
const txt = document.getElementById("txt");

firstBtn.addEventListener("click", () => {
  prg.innerText = txt.value;
});

// --- Part II
const secondBtn = document.getElementById("secondBtn");
const newContent = document.getElementById("newContent");
const secondTxt = document.getElementById("secondTxt");

secondBtn.addEventListener("click", () => {
  const newPrg = document.createElement("p");
  newPrg.innerText = secondTxt.value;
  newPrg.className = "myclass";
  newContent.appendChild(newPrg);
});

// --- Part III
const rmBtn = document.getElementById("rmBtn");

rmBtn.addEventListener("click", () => {
  const prgs = document.getElementsByClassName("myclass");
  const lastPrg = prgs[prgs.length - 1];
  if (prgs.length > 0) {
    newContent.removeChild(lastPrg);
  }
});
