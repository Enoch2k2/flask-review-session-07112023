import { useEffect, useState } from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './components/static/Home';
import Signup from './components/sessions/Signup';
import UserList from './components/users/UserList';
import Navbar from './components/navigation/Navbar';
import Errors from './components/errors/Errors';


function App() {
  const [users, setUsers] = useState([])
  const [errors, setErrors] = useState(null);

  useEffect(() => {
    fetch("/api/users")
      .then(resp => resp.json())
      .then(data => setUsers(data))
  }, [])

  const addUser = user => {
    setUsers([...users, user])
  }
  
  return (
    <Router>
      <Navbar />
      <Errors errors={ errors } />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/signup" element={<Signup addUser={ addUser } setErrors={ setErrors } />} />
        <Route path="/users" element={<UserList users={ users } />} />
      </Routes>
    </Router>
  );
}

export default App;
