import React, { useState } from 'react';
import { ArrowLeft, Settings, Save, Check } from 'lucide-react';
import { supportedLanguages } from '../data/translations';
import { getTranslation } from '../data/translations';

interface SettingsScreenProps {
  currentLanguage: string;
  onLanguageChange: (language: string) => void;
  onBackToHome: () => void;
}

const SettingsScreen: React.FC<SettingsScreenProps> = ({
  currentLanguage,
  onLanguageChange,
  onBackToHome
}) => {
  const [selectedLanguage, setSelectedLanguage] = useState(currentLanguage);
  const [showSuccess, setShowSuccess] = useState(false);

  const handleLanguageChange = (e: React.ChangeEvent<HTMLSelectElement>) => {
    setSelectedLanguage(e.target.value);
  };

  const handleSaveSettings = () => {
    onLanguageChange(selectedLanguage);
    setShowSuccess(true);
    setTimeout(() => setShowSuccess(false), 3000);
  };

  const t = (key: string) => getTranslation(currentLanguage, key as any);

  return (
    <div>
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '2rem' }}>
        <h1 style={{ color: '#1e293b' }}>
          <Settings size={24} style={{ display: 'inline', marginRight: '0.5rem' }} />
          {t('settings')}
        </h1>
        <button className="btn btn-outline" onClick={onBackToHome}>
          <ArrowLeft size={16} />
          {t('back')}
        </button>
      </div>

      <div className="card">
        <h2 style={{ marginBottom: '1.5rem', color: '#1e293b' }}>{t('settingsTitle')}</h2>
        
        {showSuccess && (
          <div className="success-banner" style={{ marginBottom: '1.5rem' }}>
            <Check size={20} />
            <span>{t('settingsSaved')}</span>
          </div>
        )}

        <div className="form-group">
          <label className="form-label">
            🌐 {t('language')}
          </label>
          <select
            className="form-select"
            value={selectedLanguage}
            onChange={handleLanguageChange}
          >
            {supportedLanguages.map(lang => (
              <option key={lang.code} value={lang.code}>
                {lang.flag} {lang.name}
              </option>
            ))}
          </select>
          <p style={{ marginTop: '0.5rem', color: '#6b7280', fontSize: '0.875rem' }}>
            {t('selectLanguage')}
          </p>
        </div>

        <div style={{ display: 'flex', gap: '1rem', marginTop: '2rem' }}>
          <button
            className="btn btn-primary"
            onClick={handleSaveSettings}
          >
            <Save size={16} />
            {t('saveSettings')}
          </button>
        </div>
      </div>

      <div className="card">
        <h3 style={{ marginBottom: '1rem', color: '#1e293b' }}>Language Information</h3>
        <div style={{ display: 'grid', gap: '1rem' }}>
          <div>
            <h4 style={{ marginBottom: '0.5rem', color: '#374151' }}>🇺🇸 English</h4>
            <p style={{ color: '#6b7280', fontSize: '0.875rem' }}>
              Default language with full feature support
            </p>
          </div>
          <div>
            <h4 style={{ marginBottom: '0.5rem', color: '#374151' }}>🇪🇸 Español</h4>
            <p style={{ color: '#6b7280', fontSize: '0.875rem' }}>
              Complete Spanish translation for all interface elements
            </p>
          </div>
          <div>
            <h4 style={{ marginBottom: '0.5rem', color: '#374151' }}>🇫🇷 Français</h4>
            <p style={{ color: '#6b7280', fontSize: '0.875rem' }}>
              Full French translation with proper localization
            </p>
          </div>
          <div>
            <h4 style={{ marginBottom: '0.5rem', color: '#374151' }}>🇸🇦 العربية</h4>
            <p style={{ color: '#6b7280', fontSize: '0.875rem' }}>
              Arabic translation with RTL support (coming soon)
            </p>
          </div>
        </div>
      </div>

      <div className="card">
        <h3 style={{ marginBottom: '1rem', color: '#1e293b' }}>Settings Persistence</h3>
        <p style={{ color: '#6b7280', marginBottom: '1rem' }}>
          Your language preference is automatically saved and will be remembered the next time you visit the application.
        </p>
        <div style={{ display: 'flex', gap: '0.5rem', flexWrap: 'wrap' }}>
          <span style={{ 
            background: '#f0f9ff', 
            color: '#0369a1', 
            padding: '0.25rem 0.75rem', 
            borderRadius: '1rem', 
            fontSize: '0.875rem',
            border: '1px solid #bae6fd'
          }}>
            ✓ Auto-save enabled
          </span>
          <span style={{ 
            background: '#f0fdf4', 
            color: '#166534', 
            padding: '0.25rem 0.75rem', 
            borderRadius: '1rem', 
            fontSize: '0.875rem',
            border: '1px solid #bbf7d0'
          }}>
            ✓ Local storage
          </span>
          <span style={{ 
            background: '#fef3c7', 
            color: '#92400e', 
            padding: '0.25rem 0.75rem', 
            borderRadius: '1rem', 
            fontSize: '0.875rem',
            border: '1px solid #fde68a'
          }}>
            ⚠ No server sync
          </span>
        </div>
      </div>
    </div>
  );
};

export default SettingsScreen;