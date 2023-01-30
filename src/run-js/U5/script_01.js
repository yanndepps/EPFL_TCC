// conditional logic
function calc(a, b) {
	const mess = "what res of " + a.toString() + " + " + b.toString() + " ?";
	const promptMess = window.prompt(mess);
	const add = a + b;
	if (add == Number(promptMess)) {
		return "congrats !";
	} else {
		return "failed !";
	}
}

console.log(calc(5, 2));
