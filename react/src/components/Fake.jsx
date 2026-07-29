import React, { useEffect, useState } from 'react'
import Layout from './Layout'
import './Fake.css'

const Fake = () => {
    const [info,setInfo]=useState([])

    const url='https://fakestoreapi.com/products'
    const fecthdata=async () => {
        let data=await fetch(url)
        const res= await data.json()
        setInfo(res)
        
        // console.log(data)
        
    }
    useEffect(()=>{
        fecthdata()
    },[])

  return (
  <div className="container">
    {info.map((inst) => (
      <Layout key={inst.id} inst={inst} />
    ))}
  </div>
);
}

export default Fake