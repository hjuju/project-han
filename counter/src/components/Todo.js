import React, { useState } from 'react'

const Todo = () => {
    
    const [ item, setitem ] = useState('')

    return(<>
    <h1>할 일 목록</h1>
    <h4>{item}</h4>
    
        
    <input onChange = { e => { setitem(e.target.value) } } /> <br/>
    <button onClick = { () => { setitem('')} }> 초기화</button>
    </>
        )
}

export default Todo