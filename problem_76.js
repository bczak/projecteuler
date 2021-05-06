function getSum(number) {
	let sums = [0,1,1];
	for (let i = 1; i < number; i++) {
		for (let k = i; k <= number; k++) {
			sums[k] = sums[k - i] + (sums[k] || 1);
		}
	}
	return sums[number];
}

console.log(getSum(100));

//2(1) =
//3(2) = 111, 21,
//4(4) = 1111, 22, 211, 31
//5(6) = 41, 11111, 221, 2111, 311, 23
//6()  = 51(6), 42, 33, 4 + 1 +1
