import React from 'react';
import { ReportData } from '../types';
import { ArrowLeft, Download, FileText, BarChart3, AlertTriangle, TrendingUp, Calendar } from 'lucide-react';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer, BarChart, Bar } from 'recharts';

interface ReportPreviewProps {
  reportData: ReportData | null;
  onDownload: (format: 'pdf' | 'docx') => void;
  onBackToHome: () => void;
}

const ReportPreview: React.FC<ReportPreviewProps> = ({
  reportData,
  onDownload,
  onBackToHome
}) => {
  if (!reportData) {
    return (
      <div className="card">
        <p>No report data available.</p>
        <button className="btn btn-primary" onClick={onBackToHome}>
          <ArrowLeft size={16} />
          Back to Home
        </button>
      </div>
    );
  }

  return (
    <div>
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '2rem' }}>
        <h1 style={{ color: '#1e293b' }}>Report Preview</h1>
        <button className="btn btn-outline" onClick={onBackToHome}>
          <ArrowLeft size={16} />
          Back to Home
        </button>
      </div>

      <div className="report-section">
        <h3>
          <FileText size={20} style={{ display: 'inline', marginRight: '0.5rem' }} />
          Executive Summary
        </h3>
        <div className="report-content">
          <p>{reportData.summary}</p>
        </div>
      </div>

      <div className="report-section">
        <h3>
          <Calendar size={20} style={{ display: 'inline', marginRight: '0.5rem' }} />
          Key Events
        </h3>
        <div className="report-content">
          <ul style={{ paddingLeft: '1.5rem' }}>
            {reportData.keyEvents.map((event, index) => (
              <li key={index} style={{ marginBottom: '0.5rem' }}>{event}</li>
            ))}
          </ul>
        </div>
      </div>

      <div className="report-section">
        <h3>
          <TrendingUp size={20} style={{ display: 'inline', marginRight: '0.5rem' }} />
          Trends
        </h3>
        <div className="report-content">
          <ul style={{ paddingLeft: '1.5rem' }}>
            {reportData.trends.map((trend, index) => (
              <li key={index} style={{ marginBottom: '0.5rem' }}>{trend}</li>
            ))}
          </ul>
        </div>
      </div>

      <div className="report-section">
        <h3>
          <AlertTriangle size={20} style={{ display: 'inline', marginRight: '0.5rem' }} />
          Risks
        </h3>
        <div className="report-content">
          <ul style={{ paddingLeft: '1.5rem' }}>
            {reportData.risks.map((risk, index) => (
              <li key={index} style={{ marginBottom: '0.5rem' }}>{risk}</li>
            ))}
          </ul>
        </div>
      </div>

      <div className="report-section">
        <h3>
          <BarChart3 size={20} style={{ display: 'inline', marginRight: '0.5rem' }} />
          Data Visualization
        </h3>
        <div className="chart-container">
          <h4 style={{ marginBottom: '1rem', color: '#374151' }}>Monthly Trends</h4>
          <ResponsiveContainer width="100%" height={300}>
            <LineChart data={reportData.chartData}>
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="name" />
              <YAxis />
              <Tooltip />
              <Line type="monotone" dataKey="value" stroke="#3b82f6" strokeWidth={2} />
            </LineChart>
          </ResponsiveContainer>
        </div>

        <div className="chart-container">
          <h4 style={{ marginBottom: '1rem', color: '#374151' }}>Monthly Comparison</h4>
          <ResponsiveContainer width="100%" height={300}>
            <BarChart data={reportData.chartData}>
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="name" />
              <YAxis />
              <Tooltip />
              <Bar dataKey="value" fill="#3b82f6" />
            </BarChart>
          </ResponsiveContainer>
        </div>
      </div>

      <div className="card">
        <h3 style={{ marginBottom: '1rem' }}>Download Report</h3>
        <p style={{ marginBottom: '1.5rem', color: '#6b7280' }}>
          Choose your preferred format to download the complete report.
        </p>
        <div className="download-buttons">
          <button
            className="btn btn-primary"
            onClick={() => onDownload('pdf')}
          >
            <Download size={16} />
            Download PDF
          </button>
          <button
            className="btn btn-secondary"
            onClick={() => onDownload('docx')}
          >
            <Download size={16} />
            Download DOCX
          </button>
        </div>
      </div>
    </div>
  );
};

export default ReportPreview;