function kthlargest($arr, $n, $k) 
{ 
 sort($arr); 
   return $arr[$k - 1]; 
} 
$arr = array(12, 3, 5, 7, 19); 
    $n =count($arr); 
    $k = 2; 
    echo "K'th largest element is "
       , kthSmallest($arr, $n, $k); 
