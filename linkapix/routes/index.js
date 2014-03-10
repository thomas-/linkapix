
/*
 * GET home page.
 */

var fs = require('fs');
var exec = require('child_process').exec;

exports.index = function(req, res){
    res.render('index');
};

exports.show_upload = function(req, res) {
	res.render('upload');
};

exports.generate = function(req, res) {
    var puzzle;
    console.log(req.body);
    fs.writeFile('../final/puzzles/in.json', req.body.data, function(err) {
        if(err) {
            console.log(err);
        } else {
            exec('python pgen.py '+req.body.width+' '+req.body.height+' in.json', { cwd: '../final/' }, function(error, stdout, stderr) {
                console.log('stdout: '+stdout+stderr);
                puzzle = fs.readFileSync('../final/puzzles/temp.json', 'utf8');
                res.json({ puzzledata: puzzle});
        });
        }
    });
};

exports.process_upload = function(req, res) {
	//var puzzle = JSON.stringify(require('./test.json'));
    var puzzle;
    console.log(req.body);
    console.log('hi');
    //fs.unlink('../final/puzzles/temp.json');
    fs.writeFile('../final/puzzles/in.json', req.body.data, function(err) {
        if(err) {
            console.log(err);
        } else {
            exec('python pgen.py '+req.body.width+' '+req.body.height+' in.json', { cwd: '../final/' }, function(error, stdout, stderr) {
                console.log('stdout: '+stdout+stderr);
                puzzle = fs.readFileSync('../final/puzzles/temp.json', 'utf8');
                //console.log(puzzle);
                res.render('linkapix', { puzzledata: puzzle});
                /*fs.readFile('../final/puzzles/temp.json', 'utf8', function(err, data) {
                    if(err) {
                        console.log(err);
                    } else {
                        puzzle = data;
                        //console.log(data);
                    }
                });*/

        });
        }
    });
    /*fs.readFile('../final/puzzles/temp.json', function(err, data) {
        if(err) {
            console.log(err);
        } else {
            puzzle = data;
            console.log(data);
        }
    });*/
    //console.log(puzzle);

};