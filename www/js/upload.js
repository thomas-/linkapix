var puzzle = null;
var imagefile = null;

function analyse_puzzle(src, callback) {
    //var canvas = document.getElementById('myCanvas');
    //var ctx = canvas.getContext('2d');
    var imageObj = new Image();
    imageObj.src = src;

    imageObj.onload = function() {
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

        var white = [255, 255, 255];
        var black = [0, 0, 0];

        for (i = 0; i < height; i++) {
            for (j = 0; j < width; j++) {
                var imgData = ctx.getImageData(j * blockWidth + blockWidth / 2, i * blockHeight + blockHeight / 2, 1, 1);

                disWhite = (white[0] - imgData.data[0]) + (white[1] - imgData.data[1]) + (white[2] - imgData.data[2]);
                disBlack = (imgData.data[0] - black[0]) + (imgData.data[1] - black[1]) + (imgData.data[2] - black[2]);
                if (disWhite < 10) {
                    pixArray[i][j] = { number: 0, color: {r: 255, g: 255, b: 255} };
                } else if (disBlack < 10) {
                    pixArray[i][j] = { number: 1, color: {r: 0, g: 0, b: 0} };
                } else {
                    pixArray[i][j] = { number: 1, color: {r: 0, g: 0, b: 0} };
                }
            }
        }
        console.log(pixArray);
        callback(pixArray);
    };
    return data;
};

function readFile(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            var image = new Image();
            image.src = e.target.result;
            analyse_puzzle(e.target.result, function(pixArray) {
                var postdata = new Object;
                postdata.width = $('#width').val();
                postdata.height = $('#height').val();
                postdata.difficulty = $('#difficulty').val();
                postdata.data = JSON.stringify(pixArray);
                console.log(postdata);
                $('.progress').show(400);
                $('.progress-bar').animate({width: "90%"}, 20000);
                $.ajax({
                    type: "POST",
                    url: '/generate.php',
                    data: postdata,
                    success: function(result) {
                        result = JSON.parse(result);
                        console.log(result.cachefilename);
                        $('.progress-bar').stop();
                        $('.progress-bar').css({width: "100%"});
                        $('.progress').hide(400);
                        destroy_puzzle();
                        console.log(result.puzzledata);
                        puzzle = string_to_puzzle(result.puzzledata);
                        build_puzzle(puzzle);
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
    readFile(this);
    imagefile = event.target.files;
});

$(".btn-save").on('click', function() {
    var valid = false;
    var puzzlename = prompt("Enter a name for the puzzle:");
    if (puzzlename != null) {
        postdata = new Object;
        postdata.puzzlename = puzzlename;
        postdata.puzzledata = JSON.stringify(puzzle);
        $.ajax({
            type: "POST",
            url: '/save.php',
            data: postdata,
            success: function(result) {
                console.log(result);
                if (result == "OK") {
                    console.log("saved");
                }
            }
        });
    }
});
