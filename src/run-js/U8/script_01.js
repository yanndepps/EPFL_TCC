// Arrays
const fruits = ["oranges", "apples", "bananas"];
// console.log("fruits -> ", fruits);

// accessing values
let message;
message = "The second value contains apples : " + fruits[1];
// console.log(message);

// update a value
fruits[1] = "kiwis";
message = "The second value now contains kiwis : " + fruits[1];
// console.log(message);

// add and remove values
fruits.push("tomatoes");
// console.log(fruits);

// fruits.splice(2, 2);
// console.log(fruits);

// sorting
// fruits.sort();
// fruits.reverse();
// console.log(fruits);

// array length
const fruitsCount = fruits.length;
console.log(fruitsCount);
