function sortit(&$arr, $n) 
{ 
    for ($i = 0; $i < $n; $i++)  
    { 
  
        $arr[$i]=$i+1;   
    } 
} 
$arr = array(10, 7, 9, 2, 8,  
             3, 5, 4, 6, 1); 
$n = count($arr); 
sortit($arr, $n); 
for ($i = 0; $i < $n; $i++)  
    echo $arr[$i]." "; 
