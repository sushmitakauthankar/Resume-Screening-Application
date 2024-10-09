import React from 'react';
import './UploadSection.css';
import FileUpload from './FileUpload';
import axios from 'axios'; 
import logoImage from './Images/upload.jpg';

function UploadSection({ onJobDescriptionSelect, onResumeSelect, onProcess }) {

  const handleJobDescriptionSelect = async (file) => {
    onJobDescriptionSelect(file);

    const formData = new FormData();
    formData.append('file', file);

    try {
      const response = await axios.post('http://localhost:5000/upload-job-description', formData, {
        headers: { 'Content-Type': 'multipart/form-data' }
      });
      console.log(response.data.message);
    } catch (error) {
      console.error('Error uploading job description:', error);
    }
  };

  const handleResumeSelect = async (files) => {
    onResumeSelect(files);

    const formData = new FormData();
    files.forEach((file) => formData.append('files', file));

    try {
      const response = await axios.post('http://localhost:5000/upload-resumes', formData, {
        headers: { 'Content-Type': 'multipart/form-data' }
      });
      console.log(response.data.message);
    } catch (error) {
      console.error('Error uploading resumes:', error);
    }
  };

  return (
    <div className="upload-container">
      <div className="upload-box">
        <img src={logoImage} alt="Logo" />
        <p className="drag-drop-text">Drag and Drop</p>
        <p className="file-types">Files we can read: Pdf, Docs, Text</p>
        <div className="button-container">
          <FileUpload label="Upload Job Description File" onFileSelect={handleJobDescriptionSelect} />
          <FileUpload label="Upload Resume Folder" onFileSelect={handleResumeSelect} isFolder />
        </div>
        <button className="check-button" onClick={onProcess}>CHECK</button>
      </div>
    </div>
  );
}

export default UploadSection;
