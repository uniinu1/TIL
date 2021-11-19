
# *DB에서 자료를 추출하면 가공하는 과정이 필요하다.(JSON)*
DB에서 추출한 자료 중 JSON STRING으로 저장되어 있는 자료형이 존재했다. <br>
이 자료는 가공하는 과정을 거쳐야 다른 사람이 이해하기 쉬운 자료가 된다.

내가 DB로 부터 추출한 JSON 자료형은 이스케이프 문자(\\)가 들어가 있어서 json_decode()함수로 바로 Decode가 되지 않아서 이스케이프 문자를 없애는 작업이 한 번 더 필요했다.

$list에는 내가 쿼리를 통해 추출한 다른 컬럼 자료들도 있기에 foreach문을 돌려서 배열을 한 번 나열해주고 그 중 내가 가공하길 원하는 JSON이 들어있는 staff 컬럼을 추출하였다.

<code>

    <?php
        foreach ($list as $list) {
            $staff_JSON = $list->staff;
            $test = str_replace("\\", "", $staff_JSON);  
            $test_de = json_decode($test, true);
               
            foreach($test_de as $person){
                echo $person["Name"].",";
                echo $person["Tel"].",";
                echo $person["Phone"].",";
                echo $person["Email"].",";
            }
            echo '<br>';
        } ?>
      

</code>

<br>
[참고자료] <br>
https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=cokolavel&logNo=221516817104 <br>
https://www.delftstack.com/ko/howto/php/php-replace-string/ <br>
https://midwin.tistory.com/11


