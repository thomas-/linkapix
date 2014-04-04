<?php

ini_set('max_execution_time', 300000);

//error_log('generator');

$width = intval($_POST['width']);
$height = intval($_POST['height']);
$difficulty = intval($_POST['difficulty']);
$data = $_POST['data'];
$md5 = md5($data);
$cachefilename = $width."x".$height."-".$md5.".json";
$cachepath = "/home/thomas/gp13-jaa/final/puzzles/$cachefilename";

file_put_contents($cachepath, $data);

$result = exec("cd /home/thomas/gp13-jaa/final/; /usr/bin/python pgen.py $width $height $cachefilename $difficulty");
//error_log("cd /home/thomas/gp13-jaa/final/; /usr/bin/python pgen.py $width $height $cachefilename  $difficulty");

copy("/home/thomas/gp13-jaa/final/puzzles/".$cachefilename, "cache/puzzles/".$cachefilename);

$puzzledata = file_get_contents("cache/puzzles/".$cachefilename);

$result = Array(
    "cachefilename" => $cachefilename,
    "puzzledata" => $puzzledata
);

echo json_encode($result);
