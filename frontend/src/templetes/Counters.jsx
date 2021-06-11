import React from 'react'
import './table.style.css'
import { Counter } from 'counter'

const Counter = ({children}) => (<>
    <h1>Counter</h1>
    {children}
</>)

export default Counter