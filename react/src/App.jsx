import React from 'react'
import Profile from './components/Profile'

const users = [
  {
    id: 1,
    name: "Kurumurthy",
    role: "Python Full Stack Developer",
    email: "kurumurthy@gmail.com",
    age: 22,
    isOnline: true,
    skills: ["Python", "Django", "React", "SQL"],
    address: {
      city: "Hyderabad",
      state: "Telangana",
      country: "India"
    }
  },
  {
    id: 2,
    name: "",
    role: "Frontend Developer",
    email: "@gmail.com",
    age: 21,
    isOnline: false,
    skills: ["React", "JavaScript", "Tailwind"],
    address: {
      city: "Bangalore",
      state: "Karnataka",
      country: "India"
    }
  },
  {
    id: 3,
    name: "Jagadish",
    role: "Backend Developer",
    email: "jagadish@gmail.com",
    age: 23,
    isOnline: true,
    skills: ["Python", "FastAPI", "PostgreSQL"],
    address: {
      city: "Chennai",
      state: "Tamil Nadu",
      country: "India"
    }
  }
];

const App = () => {
  return (
    <div>
      <Profile users={users}/>
    </div>
  )
}

export default App