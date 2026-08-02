import { Routes, Route, BrowserRouter } from 'react-router-dom';
import LogIn from './pages/Log-In';
import SignIn from './pages/Sign-In';
import Dashboard from './pages/Dashboard';

function App(){
  return(
    <BrowserRouter>
      <Routes>
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/login" element={<LogIn />} />
        <Route path="/signin" element={<SignIn />} />
      </Routes>
    </BrowserRouter>
  )

}

export default App;