import React from 'react';

const FileUpload = ({ label, onFileSelect, isFolder = false }) => {
  const handleFileInput = (event) => {
    const files = event.target.files;
    onFileSelect(isFolder ? Array.from(files) : files[0]);
  };

  return (
    <label className="upload-button">
      {label}
      <input 
        type="file" 
        webkitdirectory={isFolder ? "true" : undefined}
        directory={isFolder ? "true" : undefined}
        multiple={isFolder}
        onChange={handleFileInput} 
        style={{ display: 'none' }} 
      />
    </label>
  );
};

export default FileUpload;
