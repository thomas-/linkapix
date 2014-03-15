var picking = false;
var start = [0,0];
var startblock = null;
var number = 0;
var previous = null;
var links = [];

var link_start = null;
var current_block = null;
var current_link = [];
var undo_list = [];
var touched = [];

function destroy_puzzle() {
    $(".linkapix").html("");
}

function json_to_puzzle(json_url) {
    var str = '[[{"number":3,"color":{"r":0,"g":0,"b":0}},null,{"number":3,"color":{"r":0,"g":0,"b":0}},null,null],[null,null,null,{"number":1,"color":{"r":0,"g":0,"b":0}},null],[null,null,{"number":5,"color":{"r":0,"g":0,"b":0}},{"number":2,"color":{"r":0,"g":0,"b":0}},null],[null,null,null,{"number":2,"color":{"r":0,"g":0,"b":0}},null],[{"number":5,"color":{"r":0,"g":0,"b":0}},null,null,null,null]]';
    return JSON.parse(str);
    console.log('build!' + json_url);
    var data = $.getJSON(json_url, function(data) {
        console.log(data);
        return data;
        $.each(data, function(key, val) {
            console.log(val);
            $.each(val, function(key, block) {
                console.log(key);
                console.log(block.number);
            });
        });
    });
    console.log(data);
    return data;
};


function build_puzzle(puzzle) {
    var table = $("<table></table>");
    $(".linkapix").append(table);
    $(".linkapix").append();
    $.each(puzzle, function(rid, row) {
        var tr = $("<tr/>")
        var blocks = [];
        $.each(row, function(cid, block) {
            if(block !== null) {
                number = block.number;
                blocks.push('<td class="static" data-number="'+number+'" data-x="'+cid+'" data-y="'+rid+'">' + number + "</td>");
            } else {
                number = '';
                blocks.push('<td data-number="'+number+'" data-x="'+cid+'" data-y="'+rid+'">' + number + "</td>");
            }
            //number = block !== null ? block.number : "";
            //console.log('x');
            //blocks.push('<td data-number="'+number+'" data-x="'+cid+'" data-y="'+rid+'">' + number + "</td>");
        });
        tr.append(blocks);
        table.append(tr)
    });
    //state = new State();
    register_game_events();

};

$("#launch_test").click(function() {
    destroy_puzzle();
    puzzle = json_to_puzzle('puzzles/5x5test.json');
    build_puzzle(puzzle);
});

function is_legal_move(start, end) {
    if (start.data('x') == end.data('x') || start.data('y') == end.data('y')) {
        console.log('is legal apparently');
        //console.log(start.data('x'), end.data('x'), start.data('y'), end.data('y'));
        return true;
    };
    return false;
};

function get_blocks_between(start, end) {
    return $("td").filter(function(index) {
        if (start.data('y') == end.data('y')) {
            var a = start.data('x'), b = end.data('x');
            var value = $(this).data('x');
            inline = start.data('y') == $(this).data('y');
        } else {
            var a = start.data('y'), b = end.data('y');
            var value = $(this).data('y');
            inline = start.data('x') == $(this).data('x');
        }
        return (is_between(a, b, value) && inline);
            /*var a = Math.min.apply(Math, [start.data('x'), end.data('x')]),
            max = Math.max.apply(Math, [start.data('x')]);*/
        });
};

function is_between(a, b, value) {
    var min = Math.min.apply(Math, [a,b]),
    max = Math.max.apply(Math, [a,b]);
    return value >= min && value <= max;
};

function is_same_block(a, b) {
    return (a.data('x') == b.data('x') && a.data('y') == b.data('y'));
};

function register_game_events() {
    $("td").on('click', function() {
        if (current_block != null) {
            console.log(current_block, $(this));
            if (is_same_block(current_block, $(this))) {
                $(".linkapix").trigger('endedit', [$(this)]);
            } else {
                $(".linkapix").trigger('addpoint', [$(this), get_blocks_between(
                    current_block, $(this))]);
            }
        } else {
            if ($(this).hasClass('linked') || $(this).hasClass('unfinished')) {
                $(".linkapix").trigger('removelink', [$(this)]);
            } else if ($(this).hasClass('link-end')) {
                $(".linkapix").trigger('editlink', [$(this)]);
            } else if ($(this).data('number') != '') {
                console.log('startlink')
                console.log($(this))
                $(".linkapix").trigger('startlink', [$(this)]);
            }
        }
    });
    $("td").on('mouseover', function() {
        if (current_block != null) {
            console.log('mouseovering');
            if (is_legal_move(current_block, $(this)) != false) {
                $(".linkapix").trigger('highlight', [$(this), get_blocks_between(
                    current_block, $(this))]);
            }
        }
    });
    $(".linkapix").on('startlink', function(event, block) {
        //current_link.push(block);
        block.addClass('picking');
        link_start = block;
        current_block = block;
    });
    $(".linkapix").on('highlight', function(event, block, blocks) {
        //console.log(block.number);
        if (block.data('number') != '') return;
        $("td").removeClass('picking');
        //console.log(blocks);
        blocks.addClass('picking');
        $("td").filter(function(index) {
            return $(this).data('number') == '';
        }).html('');
        console.log(current_link.length, $('td.picking').length);
        block.html(current_link.length + $('td.picking').length - 1);
    });
    $(".linkapix").on('endedit', function(event, block) {
        console.log('endedit');
        current_block = null;
        current_link = [];
        $("td").removeClass('picking');
    });
    $(".linkapix").on('addpoint', function(event, block, blocks) {
        console.log('length ', blocks.length, current_link.length);
        current_link.push.apply(current_link, blocks);
        current_link.pop();
        console.log('new length ', current_link.length)
        $(".picking").addClass('partial').removeClass('picking');
        console.log('addpoint');
        current_block = block;
    });
};


function old_register_game_events() {
    $("td").mousedown(function() {
        if ($(this).hasClass('link-end')) {
            $(".linkapix").trigger('editlink', [$(this)]);
        }
        if($(this).hasClass('linked') || $(this).hasClass('unfinished')) {
            return;
        } else {
            $(".linkapix").trigger('startlink', [$(this), $(this).data('x'), $(this).data('y')]);
        }
    });

    $("td").mouseover(function() {
        if (picking) {
            $(".linkapix").trigger('extendlink', [$(this)]);
        }
    });

    $("td").mouseup(function() {
        if (picking) {
            $('.linkapix').trigger('stoplink', [$(this)]);
        }
    });

    $('.linkapix').on('startlink', function(event, block, x, y) {
        start = [x, y];
        startblock = block;

        if (block.data('number') == '') {
            return;
        }
        else if (block.data('number') == '1') {
            block.addClass('linked');
        }
        else {
            //console.log($(this).html());
            number = block.data('number');
            picking = true;
            block.addClass('picking');
            links.push(block);
        }
    });

    $('.linkapix').on('extendlink', function(event, block) {
        if (previous !== null) previous.html('');
        if (block.hasClass('unfinished') || block.hasClass('linked') || block.hasClass('picking') || $('td.picking').length >= number || (block.hasClass('static') && block.data('number') != number)) {
            picking = false;
            if ([block.data('x'), block.data('y')] != start) {
                //console.log(block.data('x'), block.data('y'));
                //console.log(previous.data('x'), previous.data('y'));
                if(previous == null) {
                    picking = false;
                    $("td.picking").removeClass('picking');
                    links = [];
                    return
                }
                $(this).trigger('stoplink', [previous]);
            }
            $("td.picking").removeClass('picking');
            return;
        } else {
            block.addClass('picking');
            links.push(block);
            block.html($('td.picking').length);
            console.log(block != startblock);
            console.log([block.data('x'), block.data('y')] != start)
            if (block != startblock) {
                previous = block;
            }
        }
    });

$('.linkapix').on('stoplink', function(event, block) {
            //console_log($("td.picking").length);
            previous = null;
            if (block.data('number') == '') {
                len = $("td.picking").length;
                block.addClass('unfinished link-end');
                block.html(len);
                block.data('progress', $("td.picking").length);
                links.push(block);
                block.data('links', links);
                links = [];
                $("td.picking").removeClass('picking').addClass('unfinished');
            } else if (block.data('number') == number && $("td.picking").length == number) {
                $("td.picking").removeClass('picking');
                block.addClass('linked');
                $.each(links, function(key, val) {
                    val.addClass('linked');
                });
            }
            $("td.picking").css('background-color', '#fff').removeClass('picking');
            picking = false;
        });

$('.linkapix').on('editlink', function(event, block) {
    block.html('');
    block.removeClass('link-end');
    $.each(block.data('links'), function(key, val) {
        val.removeClass('unfinished');
    });
});
};

$("#launch_test").trigger('click');