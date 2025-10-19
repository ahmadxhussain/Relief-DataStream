import React, { useState, useEffect } from 'react';
import { ArrowLeft, History, Search, Trash2, FileText, Calendar, MapPin, Eye } from 'lucide-react';
import { ReportData, Country } from '../types';
import { getTranslation } from '../data/translations';

interface SavedReport {
  id: string;
  country: Country;
  dateRange: { startDate: string; endDate: string };
  reportData: ReportData;
  createdAt: string;
  title: string;
}

interface HistoryScreenProps {
  currentLanguage: string;
  onOpenReport: (report: SavedReport) => void;
  onBackToHome: () => void;
}

const HistoryScreen: React.FC<HistoryScreenProps> = ({
  currentLanguage,
  onOpenReport,
  onBackToHome
}) => {
  const [savedReports, setSavedReports] = useState<SavedReport[]>([]);
  const [searchTerm, setSearchTerm] = useState('');
  const [filteredReports, setFilteredReports] = useState<SavedReport[]>([]);

  const t = (key: string) => getTranslation(currentLanguage, key as any);

  // Load saved reports from localStorage
  useEffect(() => {
    const saved = localStorage.getItem('ngo-reports-history');
    if (saved) {
      try {
        const reports = JSON.parse(saved);
        setSavedReports(reports);
        setFilteredReports(reports);
      } catch (error) {
        console.error('Error loading saved reports:', error);
      }
    }
  }, []);

  // Filter reports based on search term
  useEffect(() => {
    if (!searchTerm.trim()) {
      setFilteredReports(savedReports);
    } else {
      const filtered = savedReports.filter(report =>
        report.country.name.toLowerCase().includes(searchTerm.toLowerCase()) ||
        report.title.toLowerCase().includes(searchTerm.toLowerCase()) ||
        report.dateRange.startDate.includes(searchTerm) ||
        report.dateRange.endDate.includes(searchTerm)
      );
      setFilteredReports(filtered);
    }
  }, [searchTerm, savedReports]);

  const handleDeleteReport = (reportId: string) => {
    if (window.confirm(t('confirm') + ' ' + t('delete') + '?')) {
      const updatedReports = savedReports.filter(report => report.id !== reportId);
      setSavedReports(updatedReports);
      setFilteredReports(updatedReports);
      localStorage.setItem('ngo-reports-history', JSON.stringify(updatedReports));
    }
  };

  const handleClearHistory = () => {
    if (window.confirm(t('confirm') + ' ' + t('clearHistory') + '?')) {
      setSavedReports([]);
      setFilteredReports([]);
      localStorage.removeItem('ngo-reports-history');
    }
  };

  const formatDate = (dateString: string) => {
    return new Date(dateString).toLocaleDateString(currentLanguage === 'ar' ? 'ar-SA' : currentLanguage, {
      year: 'numeric',
      month: 'short',
      day: 'numeric',
      hour: '2-digit',
      minute: '2-digit'
    });
  };

  return (
    <div>
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '2rem' }}>
        <h1 style={{ color: '#1e293b' }}>
          <History size={24} style={{ display: 'inline', marginRight: '0.5rem' }} />
          {t('reportHistory')}
        </h1>
        <button className="btn btn-outline" onClick={onBackToHome}>
          <ArrowLeft size={16} />
          {t('back')}
        </button>
      </div>

      {savedReports.length > 0 && (
        <div className="card">
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '1rem' }}>
            <h3 style={{ color: '#1e293b' }}>{t('searchReports')}</h3>
            <button
              className="btn btn-outline"
              onClick={handleClearHistory}
              style={{ color: '#dc2626', borderColor: '#dc2626' }}
            >
              <Trash2 size={16} />
              {t('clearHistory')}
            </button>
          </div>
          
          <div className="form-group">
            <div style={{ position: 'relative' }}>
              <Search 
                size={20} 
                style={{ 
                  position: 'absolute', 
                  left: '0.75rem', 
                  top: '50%', 
                  transform: 'translateY(-50%)', 
                  color: '#6b7280' 
                }} 
              />
              <input
                type="text"
                className="form-input"
                placeholder={t('searchPlaceholder')}
                value={searchTerm}
                onChange={(e) => setSearchTerm(e.target.value)}
                style={{ paddingLeft: '2.5rem' }}
              />
            </div>
          </div>
        </div>
      )}

      {filteredReports.length === 0 ? (
        <div className="card">
          <div style={{ textAlign: 'center', padding: '3rem 1rem' }}>
            <FileText size={64} style={{ color: '#d1d5db', marginBottom: '1rem' }} />
            <h3 style={{ marginBottom: '1rem', color: '#6b7280' }}>
              {savedReports.length === 0 ? t('noHistory') : 'No matching reports found'}
            </h3>
            <p style={{ color: '#9ca3af', marginBottom: '2rem' }}>
              {savedReports.length === 0 ? t('noHistoryDescription') : 'Try adjusting your search terms'}
            </p>
            <button className="btn btn-primary" onClick={onBackToHome}>
              {t('back')} {t('home')}
            </button>
          </div>
        </div>
      ) : (
        <div style={{ display: 'grid', gap: '1rem' }}>
          {filteredReports.map((report) => (
            <div key={report.id} className="card">
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', marginBottom: '1rem' }}>
                <div style={{ flex: 1 }}>
                  <h3 style={{ marginBottom: '0.5rem', color: '#1e293b' }}>
                    {report.title}
                  </h3>
                  <div style={{ display: 'flex', gap: '1rem', marginBottom: '0.5rem', flexWrap: 'wrap' }}>
                    <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', color: '#6b7280' }}>
                      <MapPin size={16} />
                      <span>{report.country.name}</span>
                    </div>
                    <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', color: '#6b7280' }}>
                      <Calendar size={16} />
                      <span>{report.dateRange.startDate} - {report.dateRange.endDate}</span>
                    </div>
                  </div>
                  <p style={{ color: '#9ca3af', fontSize: '0.875rem' }}>
                    {t('reportDate')}: {formatDate(report.createdAt)}
                  </p>
                </div>
                <div style={{ display: 'flex', gap: '0.5rem' }}>
                  <button
                    className="btn btn-primary"
                    onClick={() => onOpenReport(report)}
                    style={{ padding: '0.5rem 1rem' }}
                  >
                    <Eye size={16} />
                    {t('openReport')}
                  </button>
                  <button
                    className="btn btn-outline"
                    onClick={() => handleDeleteReport(report.id)}
                    style={{ padding: '0.5rem', color: '#dc2626', borderColor: '#dc2626' }}
                  >
                    <Trash2 size={16} />
                  </button>
                </div>
              </div>
              
              <div style={{ 
                background: '#f8fafc', 
                padding: '1rem', 
                borderRadius: '0.5rem',
                border: '1px solid #e2e8f0'
              }}>
                <h4 style={{ marginBottom: '0.5rem', color: '#374151', fontSize: '0.875rem' }}>
                  Report Preview
                </h4>
                <p style={{ color: '#6b7280', fontSize: '0.875rem', lineHeight: '1.5' }}>
                  {report.reportData.summary.substring(0, 150)}...
                </p>
              </div>
            </div>
          ))}
        </div>
      )}

      {savedReports.length > 0 && (
        <div className="card">
          <h3 style={{ marginBottom: '1rem', color: '#1e293b' }}>History Statistics</h3>
          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))', gap: '1rem' }}>
            <div style={{ textAlign: 'center', padding: '1rem', background: '#f0f9ff', borderRadius: '0.5rem' }}>
              <div style={{ fontSize: '2rem', fontWeight: 'bold', color: '#0369a1' }}>
                {savedReports.length}
              </div>
              <div style={{ color: '#6b7280', fontSize: '0.875rem' }}>
                Total Reports
              </div>
            </div>
            <div style={{ textAlign: 'center', padding: '1rem', background: '#f0fdf4', borderRadius: '0.5rem' }}>
              <div style={{ fontSize: '2rem', fontWeight: 'bold', color: '#166534' }}>
                {new Set(savedReports.map(r => r.country.code)).size}
              </div>
              <div style={{ color: '#6b7280', fontSize: '0.875rem' }}>
                Countries Covered
              </div>
            </div>
            <div style={{ textAlign: 'center', padding: '1rem', background: '#fef3c7', borderRadius: '0.5rem' }}>
              <div style={{ fontSize: '2rem', fontWeight: 'bold', color: '#92400e' }}>
                {Math.round(savedReports.reduce((acc, r) => acc + r.reportData.chartData.length, 0) / savedReports.length) || 0}
              </div>
              <div style={{ color: '#6b7280', fontSize: '0.875rem' }}>
                Avg Data Points
              </div>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

export default HistoryScreen;