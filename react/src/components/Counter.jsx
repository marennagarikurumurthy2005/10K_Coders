import React, { useState } from 'react'

const Counter = () => {
    const [count,setCount]=useState(0)
    const increment=()=>{
        setCount(prev=>prev+1)
    }
    const decrement=()=>{
        setCount(prev=>prev-1)
    }
    const reset=()=>{
        setCount(0)
    }
  return (
    <div>
        <h1>{count}</h1>
        <button onClick={increment}>Increment</button> <br />
        <button onClick={decrement}>Decrement</button> <br />
        <button onClick={reset}>Reset</button> <br />
    </div>
  )
}

export default Counter