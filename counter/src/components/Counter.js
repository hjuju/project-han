import React, { useState } from 'react'

const Counter = () => {

    const [ num, setnum ] = useState(0)

    return(<>
    <h1>{num}</h1>
    <button onClick = { () => setnum(num + 1)}> + </button>
    <button onClick = { () => setnum(num - 1)}> - </button>
    </>)
    
}

export default Counter