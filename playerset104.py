function minimalSteps($s,$n) 
{ 
for ($i = 0; $i < $n; $i++) 
        $dp[$i] = PHP_INT_MAX; 
        $s1 = ""; 
    $s2 = ""; 
    $dp[0] = 1; 
  
    $s1=$s1.$s[0]; 
  
    for ($i = 1; $i < $n; $i++)  
    { 
        $s1 = $s1.$s[$i]; 
        $s2 = substr($s, $i + 1, $i + 1); 
        $dp[$i] = min($dp[$i],  
                  $dp[$i - 1] + 1); 
                  if ($s1 == $s2) 
            $dp[$i * 2 + 1] = min($dp[$i] + 1, 
                              $dp[$i * 2 + 1]); 
    } 
      return $dp[$n - 1]; 
} 
  $s = "aaaaaaaa"; 
    $n = strlen($s);
    echo minimalSteps($s, $n);
