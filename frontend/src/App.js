import React from 'react'

const App = () => {
  return (<>
    <head>
      <title>나의 홈페이지</title>
    </head>
    <body>
      <nav>
        <a href="./index.html">Home</a>
        <a href="./blog_list,html">Blog</a>
        <a href="./about_me.html">About Me</a>
      </nav>
      <h1>첫번째 크기 헤드라인</h1>
      <h2>첫번째 크기 헤드라인</h2>
      <h3>첫번째 크기 헤드라인</h3>
      <h4>첫번째 크기 헤드라인</h4>
      <h5>첫번째 크기 헤드라인</h5>
      <p>문단은 p로 쓰세요. p는 아마도 paragraph의 앞글자를</p>
      <a href="https://www.google.com">Go to google</a>
      <hr/>
      <img src="./images/stay_funky.jpg" whdth="600px"></img>
    </body>
  </>)
}

export default App