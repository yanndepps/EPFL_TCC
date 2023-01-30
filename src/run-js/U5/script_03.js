// useful greeter
const mal_greet = 'Hello Sir! Welcome back !';
const fem_greet = 'Hello Madam! Welcome back !';
const nos_greet = 'Hello ! Welcome back !';

// const m_input = 'male';
// const f_input = 'female';

const gen_ins = ['male', 'Male', 'female', 'Female'];
// gen_ins.push(m_input, f_input);

const txt = ' ';

function greeter(gender) {
	for (const value of gen_ins) {
		if(gender === gen_ins[0] || gender === gen_ins[1]) {
			return mal_greet;
		} else if (gender === gen_ins[2] || gender === gen_ins[3]) {
			return fem_greet;
		} else {
			return nos_greet;
		}
	}
}

greeter(txt);
