// Multiconverter
// ---

// --- Main function --- //
function multiConvert() {
  let run = true;
  while (run) {
    let value;
    const userInput = window.prompt("Do you want to convert a value? (yes/no)");
    if (userInput === "yes") {
      const whichConv = window.prompt("Which conversion ? (inches/celsius/liters)");
      if (whichConv === "celsius") {
        value = window.prompt("Which value do you want to convert ?");
        isNum(value, tempConvert(value));
      } else if (whichConv === "inches") {
        value = window.prompt("Which value do you want to convert ?");
        isNum(value, cmToInches(value));
      } else if (whichConv === "liters") {
        value = window.prompt("Which value do you want to convert ?");
        isNum(value, usgToLtr(value));
      } else {
        value = window.prompt("Which value do you want to convert ?");
        console.log("Nope!");
        return;
      }
    } else if (userInput === "no") {
      console.log("You don't want to convert things !");
      return;
    } else {
      console.log("Can't convert !");
    }
  }
}
multiConvert();

// --- Utils functions --- //
// --- check that inputs are numbers only
function isNum(val, fn) {
  const isNumeric = val.match(/^\d+$/);
  if (!isNumeric) {
    console.log("Please enter numbers only !");
  } else {
    console.log(fn);
  }
}

// --- cm to inches
function cmToInches(num) {
  // formula
  let result = (num / 2.54).toFixed(2);
  // account for negative values
  if (num < 0) { console.log("beware : negative values !"); }

  // account for singular or plural
  // remember that we make plural any quantity over one
  let msg;
  const words = ["centimeter", "centimeters", "inch", "inches"];
  const singular = "is";
  const plural = "are";
  if (result > 0 && result < 1) {
    msg = words[0] + " " + singular + " " + result + " " + words[2];
  } else {
    msg = words[1] + " " + plural + " " + result + " " + words[3];
  }

  // return result
  return num + " " + msg;
}

// --- celsius to fahrenheit
function tempConvert(num) {
  // formula
  let result = ((num * 9 / 5) + 32).toFixed(1);

  // account for singular or plural ( -1 ... 1 degree )
  let msg;
  const words = ["degree", "degrees", "fahrenheit", "fahrenheits"];
  const singular = "celsius is";
  const plural = "celsius are";

  if (num === 0 || num === 1 || num === -1) {
    msg = words[0] + " " + singular + " " + result + " " + words[2];
  } else {
    msg = words[1] + " " + plural + " " + result + " " + words[3];
  }

  // return result
  return num + " " + msg;
}

// --- US gallons to liters
function usgToLtr(num) {
  // formula
  let result = (num / 0.26417).toFixed(2);

  // account for plural and singular
  let msg;
  const wordList = {
    ugl: "US gallon",
    ugls: "US gallons",
    ltr: "liter",
    ltrs: "liters",
    sgn: "is",
    plr: "are",
  };

  if (result > 0 && result < 1) {
    msg = wordList.ugl + " " + wordList.sgn + " " + result + " " + wordList.ltr;
  } else {
    msg = wordList.ugls + " " + wordList.plr + " " + result + " " + wordList.ltrs;
  }

  // return result
  return num + " " + msg;
}
// --- END --- //
