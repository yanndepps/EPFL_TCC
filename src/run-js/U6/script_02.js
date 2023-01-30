// Fix the errors below :

function logIn(passwordIsCorrect) {
  if (passwordIsCorrect != true) {
    console.log("Your password is not correct, you can't log in");
	} else {
		console.log("Welcome back! You are now signed in.");
	}
}

// logIn(false);

// ---

function litersToGallons(liters) {
  var result = liters * 0.264172;
  var message = liters.toString() + " liters are " + result.toString() + " gallons.";
  console.log(message);
}

// litersToGallons(2);

// ---

function isGreatherThan10(number) {
	if (number > 10) {
    return "The number is greater than 10.";
  } else if ( number < 10) {
    return "The number is smaller than 10.";
	} else {
		return "The number is equal to 10.";
	}
}

// console.log(isGreatherThan10(10));

// ---
