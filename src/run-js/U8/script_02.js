// Ex: favorite dishes
// ---
// 1. Create a JS array to store your 3 favorite dishes.
// 2. List each of them in the console on their own separate line.
// 3. Display the count of your favorite dishes.
// 4. Add a 4th dish to the array. -> Halloween Pumpkin Cookies
// 5. Display the count once more within a sentence: "I have x fav dishes ..."
// 6. Remove the 2nd one.
// 7. Sort them in alphabetical order.
// 8. Display them once more, as an array in the console.
// 9. Display the count again.
// ---

// --- 1.
const favDishes = ["Carrot Kinpira Onigirazu", "Cheese and Spinach Ravioli", "Fresh Pesto Pasta"];

// --- 2.
console.log(favDishes[0]);
console.log(favDishes[1]);
console.log(favDishes[2]);
console.log("// ---");

// --- 3.
const allFavDishes = favDishes.length;
console.log(allFavDishes);
console.log("// ---");

// --- 4.
const elementFour = "Halloween Pumpkin Cookies";
favDishes.push(elementFour);

// --- 5.
const message = "I have " + favDishes.length.toString() + " favorite dishes !";
console.log(message);
console.log("// ---");

// --- 6.
favDishes.splice(1, 1);

// --- 7.
favDishes.sort();

// --- 8.
console.log(favDishes);
console.log("// ---");

// --- 9.
console.log(allFavDishes);
console.log("// ---");

// ---
