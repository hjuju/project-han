import React, { useState } from 'react'


const Home = ({children}) => (<>
    <table className="tab_lay">
        <tr><td><h1>홈</h1></td></tr>
        <tr><td><button>서버 연결 테스트</button></td></tr>
    </table>
    {children}

</>)

export default Home

export const Counter = () => {
    const [ num, setnum ] = useState(0)

    return(<>
    <h1>{num}</h1>
    <button onClick = { () => setnum(num + 1)}> + </button>
    <button onClick = { () => setnum(num - 1)}> - </button>
</>)
}

