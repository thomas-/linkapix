
/*
 * GET home page.
 */

exports.index = function(req, res){
  res.render('index', { title: 'Express' });
};

exports.show_upload = function(req, res) {
	res.render('upload');
};

exports.process_upload = function(req, res) {
	var puzzle = JSON.stringify(require('./test.json'));
	res.render('linkapix', { puzzledata: puzzle});
};