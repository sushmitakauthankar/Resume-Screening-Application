import React from 'react';
import { useLocation, useNavigate } from 'react-router-dom';
import PieChart from './PieChart';
import './ResultPage.css';

const ResultsPage = () => {
  const location = useLocation();
  const navigate = useNavigate();
  const results = location.state?.results || [];

  const categoryCounts = results.reduce((acc, result) => {
    const { predicted_categories } = result;
    predicted_categories.forEach(category => {
      if (category) {
        acc[category] = (acc[category] || 0) + 1;
      }
    });
    return acc;
  }, {});

  const data = Object.keys(categoryCounts).map(category => ({
    name: category,
    count: categoryCounts[category],
  }));

  const handleBackClick = () => {
    navigate('/'); 
  };

  return (
    <div className="results-container">
      <button className="back-button" onClick={handleBackClick}>Back</button>
      <h1>Results</h1>
      <table className="table">
        <thead>
          <tr>
            <th>Rank</th>
            <th>Resume File Name</th>
            <th>Predicted Categories</th>
            <th>Category Probabilities</th>
            <th>Similarity Score</th>
          </tr>
        </thead>
        <tbody>
          {results.map((result, index) => (
            <tr key={index}>
              <td>{result.rank}</td>
              <td>{result.resume_file}</td>
              <td>{result.predicted_categories.join(', ')}</td>
              <td>{result.probabilities.join(', ')}</td>
              <td>{result.similarity_score}</td>
            </tr>
          ))}
        </tbody>
      </table>
      <h4>Resumes In Each Category</h4>
      <PieChart data={data} /> {}

    </div>
    
  );
};

export default ResultsPage;
