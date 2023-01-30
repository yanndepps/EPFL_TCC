// Ex : The friendly converter
function temp_conv(celsius) {
	const result = (celsius * 9 / 5) + 32
	const message = celsius.toString() + " " + "degrees Celsius are" + " " + result.toString() + " " + "degrees Farenheit !";
	return message;
}

const friendlyTemp = temp_conv(21);

console.log(friendlyTemp);
