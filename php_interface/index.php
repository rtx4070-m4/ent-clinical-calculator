<?php
header('Content-Type: application/json');
$input = json_decode(file_get_contents('php://input'), true);

if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($input['type'])) {
    if ($input['type'] === 'pta') {
        $left = [$input['l500'], $input['l1000'], $input['l2000']];
        $right = [$input['r500'], $input['r1000'], $input['r2000']];
        $lAvg = array_sum($left) / 3;
        $rAvg = array_sum($right) / 3;
        echo json_encode(['status' => 'success', 'left_avg' => round($lAvg, 2), 'right_avg' => round($rAvg, 2)]);
        exit;
    }
}
echo json_encode(['error' => 'Invalid request']);
?>
