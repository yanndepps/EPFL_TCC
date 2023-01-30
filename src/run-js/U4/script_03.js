// temp converter from Python to JS
function temp_convert(celsius) {
	const result = (celsius * 9 / 5) + 32;
	return result;
}

const tempA = temp_convert(21.5);
const tempB = temp_convert(-7);
const tempC = temp_convert(11);
const tempD = temp_convert(0);

console.log(tempA);
console.log(tempB);
console.log(tempC);
console.log(tempD);
