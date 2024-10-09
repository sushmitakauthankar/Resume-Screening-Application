import React from 'react';
import './InfoText.css';
import logoImage1 from './Images/resume-Folder-img.webp';
import logoImage2 from './Images/jd-img.png';
import logoImage3 from './Images/results-icon-img.png';

function InfoText() {
  return (
    <info>
      <div className="info-text">
        <div class="tagline">
          <h2>Streamline your hiring process by matching the best candidates to your job descriptions</h2>
          </div>
        <h1>How It Works</h1>
        <div className="jd-text">
          <div className="left-text">
            <img src={logoImage1} alt="Logo 1" />
            <h1>Upload Resume Folder</h1>
            <p>Easily submit Your Resume Folder For Thorough Analysis</p>
          </div>
          <div className="centre-text">
            <img src={logoImage2} alt="Logo 2" />
            <h1>Upload Job Description File</h1>
            <p>Add File Containing Job Details</p>
          </div>
          <div className="right-text">
            <img src={logoImage3} alt="Logo 3" />
            <h1>Get Predicted category and Ranking </h1>
            <p>categorizes the resume and ranks it based on job description</p>
          </div>
        </div>    
      </div>
    </info>
  );
}


export default InfoText;
