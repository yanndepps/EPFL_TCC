// The Number Game - JS Version
// ---
const rnd = Math.round(Math.random() * 101);
const showNum = true;
const debugNum = "the secret number is : " + rnd.toString();
if (showNum) {
  console.log(debugNum);
}

function guessNumGame() {
  // --- vars
  let playGame = true;
  let attempts = 0;
  let guess = window.prompt("Pick a number between 1 and 100 : ");
  let displayAttempts;
  let words = {
    congrats: "Nailed it ! in ",
    nan: "This is not a valid number !",
    numMajor: "Try a bigger number : ",
    numMinor: "Try a lower number : ",
    count: "attempt !",
    counts: "attempts !"
  };

  // --- logic
  while (playGame) {
    // check for number only
    if (isNaN(guess)) {
      console.log(words.nan);
      playGame = false;
    }

    // inc game turns
    attempts += 1;

    // how many attempt(s) -> plural or singular
    if (attempts === 1) {
      displayAttempts = words.count;
    } else {
      displayAttempts = words.counts;
    }

    // bigger, smaller or correct guess
    if (guess == rnd) {
      guess = window.prompt(words.congrats + attempts.toString() + " " + displayAttempts)
      playGame = false;
    } else if (guess > rnd) {
      guess = window.prompt(words.numMinor);
    } else if (guess < rnd) {
      guess = window.prompt(words.numMajor);
    }
  }
}

guessNumGame();
