import React from 'react';
import { ArrowLeft, HelpCircle, FileText, BarChart3, Download, RotateCcw, AlertTriangle } from 'lucide-react';

interface HelpScreenProps {
  onBackToHome: () => void;
}

const HelpScreen: React.FC<HelpScreenProps> = ({ onBackToHome }) => {
  return (
    <div>
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '2rem' }}>
        <h1 style={{ color: '#1e293b' }}>
          <HelpCircle size={24} style={{ display: 'inline', marginRight: '0.5rem' }} />
          Help & About
        </h1>
        <button className="btn btn-outline" onClick={onBackToHome}>
          <ArrowLeft size={16} />
          Back to Home
        </button>
      </div>

      <div className="card">
        <h2 style={{ marginBottom: '1rem', color: '#1e293b' }}>How to Use the App</h2>
        <p style={{ marginBottom: '1.5rem', color: '#6b7280' }}>
          The NGO Data Helpers app allows you to generate comprehensive humanitarian and development reports for any country within a specified date range.
        </p>

        <div style={{ display: 'grid', gap: '1.5rem' }}>
          <div>
            <h3 style={{ marginBottom: '0.5rem', color: '#374151' }}>
              <FileText size={18} style={{ display: 'inline', marginRight: '0.5rem' }} />
              Step 1: Select Country and Dates
            </h3>
            <p style={{ color: '#6b7280', marginLeft: '1.5rem' }}>
              Choose a country from the dropdown menu and select your desired start and end dates for the report period.
            </p>
          </div>

          <div>
            <h3 style={{ marginBottom: '0.5rem', color: '#374151' }}>
              <BarChart3 size={18} style={{ display: 'inline', marginRight: '0.5rem' }} />
              Step 2: Build Report
            </h3>
            <p style={{ color: '#6b7280', marginLeft: '1.5rem' }}>
              Click the "Build Report" button to generate your report. You'll see progress indicators as the system collects and processes data.
            </p>
          </div>

          <div>
            <h3 style={{ marginBottom: '0.5rem', color: '#374151' }}>
              <Download size={18} style={{ display: 'inline', marginRight: '0.5rem' }} />
              Step 3: Download Report
            </h3>
            <p style={{ color: '#6b7280', marginLeft: '1.5rem' }}>
              Once the report is ready, you can preview it and download it in PDF or DOCX format.
            </p>
          </div>
        </div>
      </div>

      <div className="card">
        <h2 style={{ marginBottom: '1rem', color: '#1e293b' }}>Features</h2>
        <div style={{ display: 'grid', gap: '1rem' }}>
          <div style={{ display: 'flex', alignItems: 'flex-start', gap: '0.75rem' }}>
            <FileText size={20} style={{ color: '#3b82f6', marginTop: '0.25rem' }} />
            <div>
              <h4 style={{ marginBottom: '0.25rem' }}>Comprehensive Reports</h4>
              <p style={{ color: '#6b7280', fontSize: '0.875rem' }}>
                Get detailed summaries, key events, trends, and risk assessments
              </p>
            </div>
          </div>

          <div style={{ display: 'flex', alignItems: 'flex-start', gap: '0.75rem' }}>
            <BarChart3 size={20} style={{ color: '#3b82f6', marginTop: '0.25rem' }} />
            <div>
              <h4 style={{ marginBottom: '0.25rem' }}>Data Visualization</h4>
              <p style={{ color: '#6b7280', fontSize: '0.875rem' }}>
                Interactive charts and graphs to better understand trends
              </p>
            </div>
          </div>

          <div style={{ display: 'flex', alignItems: 'flex-start', gap: '0.75rem' }}>
            <Download size={20} style={{ color: '#3b82f6', marginTop: '0.25rem' }} />
            <div>
              <h4 style={{ marginBottom: '0.25rem' }}>Multiple Formats</h4>
              <p style={{ color: '#6b7280', fontSize: '0.875rem' }}>
                Download reports in PDF or DOCX format for easy sharing
              </p>
            </div>
          </div>

          <div style={{ display: 'flex', alignItems: 'flex-start', gap: '0.75rem' }}>
            <RotateCcw size={20} style={{ color: '#3b82f6', marginTop: '0.25rem' }} />
            <div>
              <h4 style={{ marginBottom: '0.25rem' }}>Easy Reset</h4>
              <p style={{ color: '#6b7280', fontSize: '0.875rem' }}>
                Clear all inputs and start over with the reset button
              </p>
            </div>
          </div>
        </div>
      </div>

      <div className="card">
        <h2 style={{ marginBottom: '1rem', color: '#1e293b' }}>Troubleshooting</h2>
        <div style={{ display: 'grid', gap: '1rem' }}>
          <div>
            <h4 style={{ marginBottom: '0.5rem', color: '#374151' }}>
              <AlertTriangle size={16} style={{ display: 'inline', marginRight: '0.5rem', color: '#f59e0b' }} />
              "Please pick a country and valid dates"
            </h4>
            <p style={{ color: '#6b7280', fontSize: '0.875rem', marginLeft: '1.5rem' }}>
              Make sure you've selected a country from the dropdown and chosen both start and end dates.
            </p>
          </div>

          <div>
            <h4 style={{ marginBottom: '0.5rem', color: '#374151' }}>
              <AlertTriangle size={16} style={{ display: 'inline', marginRight: '0.5rem', color: '#f59e0b' }} />
              "Could not build report"
            </h4>
            <p style={{ color: '#6b7280', fontSize: '0.875rem', marginLeft: '1.5rem' }}>
              There was an error processing your request. Try again or check your internet connection.
            </p>
          </div>

          <div>
            <h4 style={{ marginBottom: '0.5rem', color: '#374151' }}>
              <AlertTriangle size={16} style={{ display: 'inline', marginRight: '0.5rem', color: '#f59e0b' }} />
              "Download failed"
            </h4>
            <p style={{ color: '#6b7280', fontSize: '0.875rem', marginLeft: '1.5rem' }}>
              The download couldn't be completed. Try again or check your browser's download settings.
            </p>
          </div>
        </div>
      </div>

      <div className="card">
        <h2 style={{ marginBottom: '1rem', color: '#1e293b' }}>About</h2>
        <p style={{ color: '#6b7280', marginBottom: '1rem' }}>
          NGO Data Helpers is designed to assist humanitarian organizations and development workers in generating comprehensive reports quickly and efficiently.
        </p>
        <p style={{ color: '#6b7280', fontSize: '0.875rem' }}>
          This is a front-end application. Backend integration will be added in future updates.
        </p>
      </div>
    </div>
  );
};

export default HelpScreen;