import './Header.css'
import logo from "../../assets/logo.svg"
import { NavLink } from 'react-router-dom'

const Header = () => {
  return (
    <div className="header-wrapper">
        <img className="logo" src={logo} alt="" />

        <div className="navigation">
            <NavLink to="/">Home</NavLink>
            <NavLink to="/batch-analyze">Batch analyze</NavLink>
        </div>
    </div>
  )
}

export default Header