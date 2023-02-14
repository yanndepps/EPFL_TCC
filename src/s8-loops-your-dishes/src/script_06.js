// Ex: Loop through your favorite dishes
// ---

const favDishes = ["Carrot Kinpira Onigirazu", "Cheese and Spinach Ravioli", "Fresh Pesto Pasta"];
const favOrder = ["First:", "Second:", "Third:"];
const message = "Here are my favorite dishes:";
const ask = "What are your favorite dishes ?";
const comment = "// ---";

let init = 0;
const maxVal = favDishes.length;

// ---

console.log(message);
console.log(comment);


for (init; init < maxVal; init++) {
	console.log(favOrder[init] + " " + favDishes[init]);
}

console.log(comment);
console.log(ask);

// ---
