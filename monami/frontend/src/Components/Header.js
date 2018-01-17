import React, { Component } from 'react';
import { Link } from 'react-router-dom';
import LogButton from './LogButton';


// The Header creates links that can be used to navigate
// between routes.
class Header extends React.Component {
  constructor(props){
    super(props)

  }



  render(){

    return(
  <header className="headerstyle">
    <h2><span><Link to='/'>Mon Ami</Link></span> - providing assistance for the elderly</h2>

    <nav className="navbar">
      <ul>
        <li> <button><Link to='/'>Home</Link></button>
        </li>
        <li> <button><Link to='/BecomeAssistant'>Become an Assistant</Link></button>
        </li>
        <li> <button><Link to='/Dashboard'>Dashboard</Link></button>
        </li>
        <li><button><Link to='/Assistants'>Find Assistant</Link></button>
        </li>
        <li> <button><Link to='/Signup'>Sign Up</Link></button>
        </li>
        <li> <LogButton onLogin={this.props.onLogin} getToken={this.props.getToken}/>
        </li>
      </ul>
    </nav>
  </header>
  )
  }
}

export default Header;
