import React, { useState } from 'react';
import { Routes, Route, useNavigate } from 'react-router-dom';
import ResultsPage from './components/ResultsPage';
import UploadSection from './components/UploadSection';
import axios from 'axios';
import Header from './components/Header';
import Background from './components/Background';
import InfoText from './components/InfoText';
import Loader from './components/Loader';
import './App.css';

function App() {
  const [jobDescription, setJobDescription] = useState(null);
  const [resumes, setResumes] = useState([]);
  const [loading, setLoading] = useState(false);
  const [message, setMessage] = useState('');
  const navigate = useNavigate();

  const handleProcess = async () => {
    if (!jobDescription || resumes.length === 0) {
      setMessage("Please upload both job description and resumes.");
      setTimeout(() => setMessage(''), 3000);
      return;
    }

    setLoading(true);

    try {
      const formData = new FormData();
      formData.append('file', jobDescription);
      resumes.forEach((file) => formData.append('files', file));

      const response = await axios.post('http://localhost:5000/process', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });

      navigate('/results', { state: { results: response.data.results } });
    } catch (error) {
      console.error('Error processing files:', error);
      setMessage('Error processing files. Please try again.');
      setTimeout(() => setMessage(''), 3000);
    } finally {
      setLoading(false);
    }
  };

  const handleJobDescriptionSelect = (file) => {
    setJobDescription(file);
    setMessage('Job description uploaded successfully!');
    setTimeout(() => setMessage(''), 3000);
  };

  const handleResumeSelect = (files) => {
    setResumes(files);
    setMessage(`${files.length} resume(s) uploaded successfully!`);
    setTimeout(() => setMessage(''), 3000);
  };

  return (
    <div className="app-container">
      <div className="bkgrd">
      {loading && <div className="blur-background loading-active"></div>}
      {loading && <Loader />}
      <Header />
      <div className="info-text">
        <InfoText />
      </div>
      {message && <div className="upload-message">{message}</div>}
      <Routes>
        <Route 
          path="/" 
          element={
            <UploadSection 
              onJobDescriptionSelect={handleJobDescriptionSelect} 
              onResumeSelect={handleResumeSelect} 
              onProcess={handleProcess}
            />
          } 
        />
        <Route path="/results" element={<ResultsPage />} />
      </Routes> 
      </div> 
    </div>
  );
  
}

export default App;
