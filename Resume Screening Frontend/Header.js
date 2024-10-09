import React from 'react';
import './Header.css';
import logoImage from './Images/s2.png';


function Header() {
  return (
    <header>
      <div className="heading-box">
      <img src={logoImage} alt="Logo" />
      <div>
        <h1>HireStream</h1>
        <p>Smart Resume Screening</p>
        </div>
      </div>
    </header>
  );
}

export default Header;
