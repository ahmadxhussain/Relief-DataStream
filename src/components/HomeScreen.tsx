import React from 'react';
import { Country, DateRange, ProgressStep } from '../types';
import { Calendar, MapPin, Play, RotateCcw } from 'lucide-react';

interface HomeScreenProps {
  countries: Country[];
  selectedCountry: Country | null;
  dateRange: DateRange | null;
  progressSteps: ProgressStep[];
  currentStep: number;
  isLoading: boolean;
  onCountryChange: (country: Country | null) => void;
  onDateRangeChange: (dateRange: DateRange | null) => void;
  onBuildReport: () => void;
  onReset: () => void;
}

const HomeScreen: React.FC<HomeScreenProps> = ({
  countries,
  selectedCountry,
  dateRange,
  progressSteps,
  currentStep,
  isLoading,
  onCountryChange,
  onDateRangeChange,
  onBuildReport,
  onReset
}) => {
  const handleCountryChange = (e: React.ChangeEvent<HTMLSelectElement>) => {
    const countryCode = e.target.value;
    const country = countryCode ? countries.find(c => c.code === countryCode) || null : null;
    onCountryChange(country);
  };

  const handleStartDateChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const startDate = e.target.value;
    onDateRangeChange({
      startDate,
      endDate: dateRange?.endDate || ''
    });
  };

  const handleEndDateChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const endDate = e.target.value;
    onDateRangeChange({
      startDate: dateRange?.startDate || '',
      endDate
    });
  };

  const canBuild = selectedCountry && dateRange?.startDate && dateRange?.endDate && !isLoading;

  return (
    <div>
      <div className="card">
        <h1 style={{ marginBottom: '1.5rem', color: '#1e293b' }}>
          Generate NGO Report
        </h1>
        <p style={{ marginBottom: '2rem', color: '#6b7280' }}>
          Select a country and date range to generate a comprehensive humanitarian and development report.
        </p>

        <div className="form-group">
          <label className="form-label">
            <MapPin size={16} style={{ display: 'inline', marginRight: '0.5rem' }} />
            Country
          </label>
          <select
            className="form-select"
            value={selectedCountry?.code || ''}
            onChange={handleCountryChange}
            disabled={isLoading}
          >
            <option value="">Select a country...</option>
            {countries.map(country => (
              <option key={country.code} value={country.code}>
                {country.name}
              </option>
            ))}
          </select>
        </div>

        <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '1rem' }}>
          <div className="form-group">
            <label className="form-label">
              <Calendar size={16} style={{ display: 'inline', marginRight: '0.5rem' }} />
              Start Date
            </label>
            <input
              type="date"
              className="form-input"
              value={dateRange?.startDate || ''}
              onChange={handleStartDateChange}
              disabled={isLoading}
            />
          </div>

          <div className="form-group">
            <label className="form-label">
              <Calendar size={16} style={{ display: 'inline', marginRight: '0.5rem' }} />
              End Date
            </label>
            <input
              type="date"
              className="form-input"
              value={dateRange?.endDate || ''}
              onChange={handleEndDateChange}
              disabled={isLoading}
            />
          </div>
        </div>

        <div style={{ display: 'flex', gap: '1rem', marginTop: '2rem' }}>
          <button
            className="btn btn-primary"
            onClick={onBuildReport}
            disabled={!canBuild}
          >
            <Play size={16} />
            {isLoading ? 'Building...' : 'Build Report'}
          </button>
          
          <button
            className="btn btn-outline"
            onClick={onReset}
            disabled={isLoading}
          >
            <RotateCcw size={16} />
            Reset
          </button>
        </div>
      </div>

      {isLoading && (
        <div className="card">
          <h3 style={{ marginBottom: '1rem' }}>Building Report</h3>
          <div className="progress-bar">
            <div 
              className="progress-fill" 
              style={{ width: `${(currentStep / progressSteps.length) * 100}%` }}
            />
          </div>
          <div className="progress-steps">
            {progressSteps.map((step, index) => (
              <div
                key={step.id}
                className={`progress-step ${step.completed ? 'completed' : ''} ${step.active ? 'active' : ''}`}
              >
                <div className="step-circle">
                  {step.completed ? '✓' : index + 1}
                </div>
                <div className="step-label">{step.label}</div>
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  );
};

export default HomeScreen;