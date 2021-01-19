const input = document.getElementById('input');
const output = document.getElementById('output');

document.querySelector("form").addEventListener("submit", function (e) {
    e.preventDefault();    //stop form from submitting

    fetch('/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(input.value)
    }).then(response => {return response.json() })
    .then(data => { printMatrix(data) })
    .catch(err => { console.log(err) })
});


function printMatrix(data) {
    // Clear output
    output.innerHTML = ""

    for(i = 0; i < data.length; i++) {

        // Create rows
        output.innerHTML += `<tr id="row${i}">`

        // Add characters to rows
        for(j = 0; j < data.length; j++) {

            // Set unique IDs for each row
            row = document.getElementById(`row${i}`)
            data[i][j] = data[i][j].replace('123456789', ' ')
            row.innerHTML += `<td>${data[i][j]}</td>`

        }
        output.innerHTML += `</tr>`
    }
}

// Sudoku to solve
printMatrix([['123456789','123456789','3','7','1','8','4','5','123456789'],
            ['4','5','123456789','123456789','123456789','123456789','7','8','1'],
            ['1','8','7','4','123456789','123456789','2','123456789','9'],
            ['123456789','123456789','123456789','1','123456789','123456789','123456789','6','7'],
            ['7','123456789','8','2','123456789','123456789','123456789','123456789','4'],
            ['5','123456789','123456789','6','8','123456789','123456789','2','123456789'],
            ['6','123456789','2','8','123456789','123456789','3','9','5'],
            ['123456789','7','123456789','123456789','2','123456789','123456789','4','8'],
            ['123456789','123456789','123456789','5','6','3','123456789','123456789','123456789']])