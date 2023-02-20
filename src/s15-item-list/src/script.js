// Persistent Item List
// ---

// --- globals
const addBtn = document.getElementById("addBtn");
const rmvBtn = document.getElementById("rmvBtn");
const clrBtn = document.getElementById("clrBtn");
const input = document.getElementById("input");
const content = document.getElementById("content");

let count;
let prgs;

// --- display local storage if any 
count = localStorage.length;
// console.log(`local items -> ${count}`);

if (localStorage.length > 0) {
  for (let i = 0; i < localStorage.length; i++) {
    prgs = document.createElement("p");
    prgs.innerText = localStorage.getItem(`item ${i + 1}`);
    prgs.className = "inputTxt";
    content.appendChild(prgs);
  }
}

// --- add elements
addBtn.addEventListener("click", () => {
  count++;
  prgs = document.createElement("p");
  const txtValue = input.value;
  localStorage.setItem(`item ${count}`, `${txtValue}`);
  prgs.innerText = localStorage.getItem(`item ${count}`);
  prgs.className = "inputTxt";
  content.appendChild(prgs);
  input.value = "";
});

// --- remove last element
rmvBtn.addEventListener("click", () => {
  const selectPrgs = document.getElementsByClassName("inputTxt");
  const lastPrg = selectPrgs[selectPrgs.length - 1];
  if (selectPrgs.length > 0) {
    content.removeChild(lastPrg);
    localStorage.removeItem(`item ${count}`);
  }
  count--;
});

// --- remove all elements 
clrBtn.addEventListener("click", () => {
  const element = document.getElementById("content");
  while (element.firstChild) {
    element.removeChild(element.firstChild);
  }
  localStorage.clear();
  count = 0;
});

// --- typewritter effect on page start
let typo = 0;
let placeholder = "";
const plhTxt = "Enter an item ...";
const speed = 120;

function type() {
  placeholder += plhTxt.charAt(typo);
  document.getElementById("input").setAttribute("placeholder", placeholder);
  typo++;
  setTimeout(type, speed);
}
type();
