// mixing data types
// const aNum = 5;
// const aStr = "Hello";
// const result = aNum + aStr;

// console.log(result);

// convert input numbers inside the calculator functions
function add(a, b) {
	return a + b;
}

const result = add(3, 7).toString();
// const result = add(3, 7);
const message = "The result is " + result;
console.log(typeof result);
console.log(message);
