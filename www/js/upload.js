/*
 * File reader and image analyser
 */


var puzzle = null;
var solution = null;
var imagefile = null;

function analyse_puzzle(src, callback) {

    // function that takes an image source and a calback,
    //
    // we analyse the image source by splitting it into a user determined
    // amount of blocks and then deciding what the most dominant colour is in
    // each block. this gives us an array of an arbitrary size that tells you
    // which square is which colour
    //
    // when this is done call the callback with the array as an argument to do
    // something with the data

    var imageObj = new Image();
    imageObj.src = src;

    imageObj.onload = function() {
        // create a canvas element but hide it from the user
        $('<canvas>').attr({
            id: 'myCanvas',
            width: this.width,
            height: this.height
        }).appendTo('.uploader').hide();

        var canvas = document.getElementById('myCanvas');
        var ctx = canvas.getContext('2d');

        ctx.drawImage(imageObj, 0, 0);

        console.log(parseInt($('#width').val()));

        var width = parseInt($('#width').val()); // User specified
        var height = parseInt($('#height').val()); // User specified

        var blockWidth = Math.round(canvas.width / width);
        var blockHeight = Math.round(canvas.height / height);

        var pixArray = new Array(height);
        for (var m = 0; m < pixArray.length; m++) {
            pixArray[m] = new Array(width);
        }

        for (i = 0; i < height; i++) {
            for (j = 0; j < width; j++) {
                var imgData = ctx.getImageData(j * blockWidth + blockWidth / 2, i * blockHeight + blockHeight / 2, 1, 1);
                /* divide the RGB space into 64 small cubes */
                var rBlock = Math.floor(imgData.data[0] / 64);
                var gBlock = Math.floor(imgData.data[1] / 64);
                var bBlock = Math.floor(imgData.data[2] / 64);

                // group each pixel into the corresponding 'cube'
                // use the values 0 ~ 63 to represent which cube the pixel is in
                // Use the value of vertex(centre?) of the cube as the colour of this group of pixels
                switch (rBlock) {
                    case 0:
                        switch (gBlock) {
                            case 0:
                                switch (bBlock) {
                                    case 0: pixArray[i][j] = {number: 1, color: {r: 0, g: 0, b: 0}}; break; // RGB = [31, 31, 31] (centre of the cube)
                                    case 1: pixArray[i][j] = {number: 1, color: {r: 31, g: 31, b: 95}}; break; // [31, 31, 95]
                                    case 2: pixArray[i][j] = {number: 1, color: {r: 31, g: 31, b: 159}}; break; // [31, 31, 159]
                                    case 3: pixArray[i][j] = {number: 1, color: {r: 31, g: 31, b: 223}}; break; // [31, 31, 223]
                                }
                                break;
                            case 1:
                                switch (bBlock) {
                                    case 0: pixArray[i][j] = {number: 1, color: {r: 31, g: 95, b: 31}}; break; // [31, 95, 31]
                                    case 1: pixArray[i][j] = {number: 1, color: {r: 31, g: 95, b: 95}}; break; // [31, 95, 95]
                                    case 2: pixArray[i][j] = {number: 1, color: {r: 31, g: 95, b: 159}}; break; // [31, 95, 159]
                                    case 3: pixArray[i][j] = {number: 1, color: {r: 31, g: 95, b: 223}}; break; // [31, 95, 223]
                                }
                                break;
                            case 2:
                                switch (bBlock) {
                                    case 0: pixArray[i][j] = {number: 1, color: {r: 31, g: 159, b: 31}}; break; // [31, 159, 31]
                                    case 1: pixArray[i][j] = {number: 1, color: {r: 31, g: 159, b: 95}}; break; // [31, 159, 95]
                                    case 2: pixArray[i][j] = {number: 1, color: {r: 31, g: 159, b: 159}}; break; // [31, 159, 159]
                                    case 3: pixArray[i][j] = {number: 1, color: {r: 31, g: 159, b: 223}}; break; // [31, 159, 223]
                                }
                                break;
                            case 3:
                                switch (bBlock) {
                                    case 0: pixArray[i][j] = {number: 1, color: {r: 31, g: 223, b: 31}}; break; // [31, 223, 31]
                                    case 1: pixArray[i][j] = {number: 1, color: {r: 31, g: 223, b: 95}}; break; // [31, 223, 95]
                                    case 2: pixArray[i][j] = {number: 1, color: {r: 31, g: 223, b: 159}}; break; // [31, 223, 159]
                                    case 3: pixArray[i][j] = {number: 1, color: {r: 31, g: 223, b: 223}}; break; // [31, 223, 223]
                                }
                                break;
                        }
                        break;
                    case 1:
                        switch (gBlock) {
                            case 0:
                                switch (bBlock) {
                                    case 0: pixArray[i][j] = {number: 1, color: {r: 95, g: 31, b: 31}}; break; // [95, 31, 31]
                                    case 1: pixArray[i][j] = {number: 1, color: {r: 95, g: 31, b: 95}}; break; // [95, 31, 95]
                                    case 2: pixArray[i][j] = {number: 1, color: {r: 95, g: 31, b: 159}}; break; // [95, 31, 159]
                                    case 3: pixArray[i][j] = {number: 1, color: {r: 95, g: 31, b: 223}}; break; // [95, 31, 223]
                                }
                                break;
                            case 1:
                                switch (bBlock) {
                                    case 0: pixArray[i][j] = {number: 1, color: {r: 95, g: 95, b: 31}}; break; // [95, 95, 31]
                                    case 1: pixArray[i][j] = {number: 1, color: {r: 95, g: 95, b: 95}}; break; // [95, 95, 95]
                                    case 2: pixArray[i][j] = {number: 1, color: {r: 95, g: 95, b: 159}}; break; // [95, 95, 159]
                                    case 3: pixArray[i][j] = {number: 1, color: {r: 95, g: 95, b: 223}}; break; // [95, 95, 223]
                                }
                                break;
                            case 2:
                                switch (bBlock) {
                                    case 0: pixArray[i][j] = {number: 1, color: {r: 95, g: 159, b: 31}}; break; // [95, 159, 31]
                                    case 1: pixArray[i][j] = {number: 1, color: {r: 95, g: 159, b: 95}}; break; // [95, 159, 95]
                                    case 2: pixArray[i][j] = {number: 1, color: {r: 95, g: 159, b: 159}}; break; // [95, 159, 159]
                                    case 3: pixArray[i][j] = {number: 1, color: {r: 95, g: 159, b: 223}}; break; // [95, 159, 223]
                                }
                                break;
                            case 3:
                                switch (bBlock) {
                                    case 0: pixArray[i][j] = {number: 1, color: {r: 95, g: 223, b: 31}}; break; // [95, 223, 31]
                                    case 1: pixArray[i][j] = {number: 1, color: {r: 95, g: 223, b: 95}}; break; // [95, 223, 95]
                                    case 2: pixArray[i][j] = {number: 1, color: {r: 95, g: 223, b: 159}}; break; // [95, 223, 159]
                                    case 3: pixArray[i][j] = {number: 1, color: {r: 95, g: 223, b: 223}}; break; // [95, 223, 223]
                                }
                                break;
                        }
                        break;
                    case 2:
                        switch (gBlock) {
                            case 0:
                                switch (bBlock) {
                                    case 0: pixArray[i][j] = {number: 1, color: {r: 159, g: 31, b: 31}}; break; // [159, 31, 31]
                                    case 1: pixArray[i][j] = {number: 1, color: {r: 159, g: 31, b: 95}}; break; // [159, 31, 95]
                                    case 2: pixArray[i][j] = {number: 1, color: {r: 159, g: 31, b: 159}}; break; // [159, 31, 159]
                                    case 3: pixArray[i][j] = {number: 1, color: {r: 159, g: 31, b: 223}}; break; // [159, 31, 223]
                                }
                                break;
                            case 1:
                                switch (bBlock) {
                                    case 0: pixArray[i][j] = {number: 1, color: {r: 159, g: 95, b: 31}}; break; // [159, 95, 31]
                                    case 1: pixArray[i][j] = {number: 1, color: {r: 159, g: 95, b: 95}}; break; // [159, 95, 95]
                                    case 2: pixArray[i][j] = {number: 1, color: {r: 159, g: 95, b: 159}}; break; // [159, 95, 159]
                                    case 3: pixArray[i][j] = {number: 1, color: {r: 159, g: 95, b: 223}}; break; // [159, 95, 223]
                                }
                                break;
                            case 2:
                                switch (bBlock) {
                                    case 0: pixArray[i][j] = {number: 1, color: {r: 159, g: 159, b: 31}}; break; // [159, 159, 31]
                                    case 1: pixArray[i][j] = {number: 1, color: {r: 159, g: 159, b: 95}}; break; // [159, 159, 95]
                                    case 2: pixArray[i][j] = {number: 1, color: {r: 159, g: 159, b: 159}}; break; // [159, 159, 159]
                                    case 3: pixArray[i][j] = {number: 1, color: {r: 159, g: 159, b: 223}}; break; // [159, 159, 223]
                                }
                                break;
                            case 3:
                                switch (bBlock) {
                                    case 0: pixArray[i][j] = {number: 1, color: {r: 159, g: 223, b: 31}}; break; // [159, 223, 31]
                                    case 1: pixArray[i][j] = {number: 1, color: {r: 159, g: 223, b: 95}}; break; // [159, 223, 95]
                                    case 2: pixArray[i][j] = {number: 1, color: {r: 159, g: 223, b: 159}}; break; // [159, 223, 159]
                                    case 3: pixArray[i][j] = {number: 1, color: {r: 159, g: 223, b: 223}}; break; // [159, 223, 223]
                                }
                                break;
                        }
                        break;
                    case 3:
                        switch (gBlock) {
                            case 0:
                                switch (bBlock) {
                                    case 0: pixArray[i][j] = {number: 1, color: {r: 223, g: 31, b: 31}}; break; // [223, 31, 31] 
                                    case 1: pixArray[i][j] = {number: 1, color: {r: 223, g: 31, b: 95}}; break; // [223, 31, 95]
                                    case 2: pixArray[i][j] = {number: 1, color: {r: 223, g: 31, b: 159}}; break; // [223, 31, 159]
                                    case 3: pixArray[i][j] = {number: 1, color: {r: 223, g: 31, b: 223}}; break; // [223, 31, 223]
                                }
                                break;
                            case 1:
                                switch (bBlock) {
                                    case 0: pixArray[i][j] = {number: 1, color: {r: 223, g: 95, b: 31}}; break; // [223, 95, 31]
                                    case 1: pixArray[i][j] = {number: 1, color: {r: 223, g: 95, b: 95}}; break; // [223, 95, 95]
                                    case 2: pixArray[i][j] = {number: 1, color: {r: 223, g: 95, b: 159}}; break; // [223, 95, 159]
                                    case 3: pixArray[i][j] = {number: 1, color: {r: 223, g: 95, b: 223}}; break; // [223, 95, 223]
                                }
                                break;
                            case 2:
                                switch (bBlock) {
                                    case 0: pixArray[i][j] = {number: 1, color: {r: 223, g: 159, b: 31}}; break; // [223, 159, 31]
                                    case 1: pixArray[i][j] = {number: 1, color: {r: 223, g: 159, b: 95}}; break; // [223, 159, 95]
                                    case 2: pixArray[i][j] = {number: 1, color: {r: 223, g: 159, b: 159}}; break; // [223, 159, 159]
                                    case 3: pixArray[i][j] = {number: 1, color: {r: 223, g: 159, b: 223}}; break; // [223, 159, 223]
                                }
                                break;
                            case 3:
                                switch (bBlock) {
                                    case 0: pixArray[i][j] = {number: 1, color: {r: 223, g: 223, b: 31}}; break; // [223, 223, 31]
                                    case 1: pixArray[i][j] = {number: 1, color: {r: 223, g: 223, b: 95}}; break; // [223, 223, 95]
                                    case 2: pixArray[i][j] = {number: 1, color: {r: 223, g: 223, b: 159}}; break; // [223, 223, 159]
                                    case 3: pixArray[i][j] = {number: 0, color: {r: 255, g: 255, b: 255}}; break; // [223, 223, 223]
                                }
                                break;
                        }
                        break;
                }
            }
        }

        /*for (var a  = 0; a < pixArray.length; a ++) {
            console.log(pixArray[a]);
        }*/

        console.log(pixArray);
        callback(pixArray);
    };
    return data;
};

function readFile(input) {
    // a function called when a file is selected so that we can get information
    // about it and send it to be analysed
    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            // have to hook reader.onload like this to properly get image data
            var image = new Image();
            image.src = e.target.result;
            // send data to be analysed and pass callback
            analyse_puzzle(e.target.result, function(pixArray) {
                // callback for puzzle analyser
                //
                // we want to create an object to be sent in POST to our
                // generator script
                var postdata = new Object;
                postdata.width = $('#width').val();
                postdata.height = $('#height').val();
                postdata.difficulty = $('#difficulty').val();
                postdata.data = JSON.stringify(pixArray);
                console.log(postdata);
                // this might take a while so we draw a progress bar and
                // animate it
                $('.progress').show(400);
                $('.progress-bar').animate({width: "90%"}, 20000);
                // send POST request asynchronously to generate script
                $.ajax({
                    type: "POST",
                    url: '/generate.php',
                    data: postdata,
                    success: function(result) {
                        result = JSON.parse(result);
                        // when we're done, we can remove the progress bar
                        $('.progress-bar').stop();
                        $('.progress-bar').css({width: "100%"});
                        $('.progress').hide(400);
                        // and create the puzzle from the returned data
                        destroy_puzzle();
                        puzzle = string_to_puzzle(result.puzzledata);
                        build_puzzle(puzzle);
                        solution = string_to_puzzle(result.solutiondata);
                        // hide stuff we dont need anymore
                        $('.uploader').hide(400);
                        $('.new_puzzle').show(400);
                        $('.save_puzzle').show(400);
                    }
                })
            });
        };
        reader.readAsDataURL(input.files[0]);
    };
};

$(".upld").change(function (event) {
    // monitors the user selecting an image
    readFile(this);
    imagefile = event.target.files;
});

$(".show_upload_solution").on('click', function (event) {
    // when we generate a puzzle we generate a solution,
    // which is stored globally as solution
    // we can use this to build a solved puzzle when user clicks show solution
    destroy_puzzle();
    build_puzzle(solution);
    // we want to make it pretty so loop through the table making every square
    // the proper colour but keep the numbers white
    $(".linkapix td").each(function(index) {
        if ($(this).data('number') != 0) {
            $(this).addClass('linked');
            $(this).css("background-color", $(this).css("color"));
            $(this).css("color", "white");
        } else {
            $(this).html($(this).data('partial'));
        }
    })
});

$(".btn-save").on('click', function() {
    // function to save generated puzzle to users library
    var puzzlename = prompt("Enter a name for the puzzle:");
	if (puzzlename != null && puzzlename != '' && puzzlename.length < 13 ) {
		postdata = new Object;
		postdata.puzzlename = puzzlename;
		postdata.puzzledata = JSON.stringify(puzzle);
        postdata.solution = JSON.stringify(solution)
		
		$.ajax({
			// we send the data to our save script
			type: "POST",
			url: '/save.php',
			data: postdata,
			success: function(result) {
				console.log(result);
				if (result == "OK") {
					document.getElementById('userFile').submit();
					console.log("saved");
					alert("Saved ! Go to 'Private Puzzles' to check it !");
				}
			}
		});
	}
	else {
		alert("Save failed! Name should be less than 13 characters!");
	}
});
