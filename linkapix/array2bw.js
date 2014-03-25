var fs = require('fs');

process.argv.slice(2).forEach(function (fileName) {
    var puzzle = Array();
    data = require('./'+fileName);
    for (var i in data) {
        var row = Array();
        for (var j in data) {
            row.push({number: data[i][j], color: {r: 0, b: 0, g: 0}});
        }
        puzzle.push(row);
    }
    fs.writeFileSync('result.json', JSON.stringify(puzzle), 'utf8');
});