import React from 'react';
import { Pie } from 'react-chartjs-2';
import { Chart as ChartJS, ArcElement, Tooltip, Legend } from 'chart.js';
import './PieeChart.css';

ChartJS.register(ArcElement, Tooltip, Legend);

const PieChart = ({ data }) => {
  const chartData = {
    labels: data.map(category => category.name),
    datasets: [
      {
        label: '# of Resumes',
        data: data.map(category => category.count),
        backgroundColor: [
            '#FF6384', '#36A2EB', '#FFCE56', '#4BC0C0', '#9966FF', '#FF9F40',
            '#FF6F61', '#6B5B95', '#88B04B', '#F7CAC9', '#92A8D1', '#FF0000',
            '#FF6347', '#0082B1', '#FFD700', '#32CD32', '#FF4500', '#6A5ACD',
            '#20B2AA', '#FF1493', '#00CED1', '#FF69B4', '#ADFF2F', '#8A2BE2',
            '#B0E0E6', '#C71585', '#FFC0CB', '#8B4513', '#7FFF00', '#D2691E'
        ],
        hoverBackgroundColor: [
            '#FF6384', '#36A2EB', '#FFCE56', '#4BC0C0', '#9966FF', '#FF9F40',
            '#FF6F61', '#6B5B95', '#88B04B', '#F7CAC9', '#92A8D1', '#FF0000',
            '#FF6347', '#0082B1', '#FFD700', '#32CD32', '#FF4500', '#6A5ACD',
            '#20B2AA', '#FF1493', '#00CED1', '#FF69B4', '#ADFF2F', '#8A2BE2',
            '#B0E0E6', '#C71585', '#FFC0CB', '#8B4513', '#7FFF00', '#D2691E'
        ],
      },
    ],
  };

  return (
    <div className="pie-chart-container">
      <Pie data={chartData} />
    </div>
  );
};

export default PieChart;
