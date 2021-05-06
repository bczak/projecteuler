const fs = require('fs')

let names = "[" + fs.readFileSync('./p022_names.txt', {encoding: 'utf-8'}) + "]"

let unsorted = JSON.parse(names);
unsorted.sort()
let result = unsorted.map((i, id) => {
	return [...i].map(i => i.charCodeAt(0) - 64).reduce((sum, tmp) => sum + tmp, 0) * (id + 1)
}).reduce((sum, tmp) => sum + tmp, 0)



console.log(result);