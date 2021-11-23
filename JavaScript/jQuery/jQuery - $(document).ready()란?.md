## - 사용법
<code>

    <script>
        $(document).ready(function(){

        });
    </script>

</code>

 .ready()는 DOM(Document Object Model)이 완전히 불러와지면 실행되는 Event입니다. 일반적으로 브라우저가 HTML을 보여주기 위해서는 먼저 문서 구조를 만들고 만들어진 문서 구조 위에 디자인을 입히는 형식을 취합니다. 이 과정에서 디자인이 입혀지지 않은 상태로 문서 구조가 만들어진 시점에 실행되는 Event가 바로. ready()입니다.

대부분의 브라우저에서는 DOMContentLoaded라는 .ready()와 비슷한 Event를 사용할 수 있습니다. 다만 여기에는 다른 점이 있습니다. 첫 번째. ready() Evnet는 DOMContentLoaded보다 먼저 실행됩니다. 두 번째 DOMContentLoaded는 Event가 한 번만 발생하며. ready() Evnet는 계속 발생합니다.

## - $(documet).ready() 대신 $()를 사용하자

<code>

    $(function(){ 
        // 실행할 기능을 정의해주세요. 
    });

</code>

<br>
출처: https://7942yongdae.tistory.com/77 [프로그래머 YD]
