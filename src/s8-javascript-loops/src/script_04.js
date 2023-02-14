// Ex: Some JS Loops
// Part 1 :
// write a for loop that displays :
// 1 step
// 2 steps
// 3 steps
// Done!
// ---
// Part 2 :
// obtain the same result using a while loop
// ---

// --- Part 1 --- //

for (let i = 0; i < 3; i++) {
	let currentStep = (i + 1).toString();
	// console.log("currentStep -> ", currentStep);
	let stepWord;
	if (currentStep === "1") {
		stepWord = " step";
	} else {
		stepWord = " steps";
	}
	console.log(currentStep + stepWord);
}
console.log("Done!");
console.log("// ---");

// --- Part 2 --- //

let x = 0;
while (x < 3) {
	let currentStep = (x + 1).toString();
	let stepWord;
	if (currentStep === "1") {
		stepWord = " step";
	} else {
		stepWord = " steps";
	}
	console.log(currentStep + stepWord);
	x++;
}

console.log("Done!");

// ---
