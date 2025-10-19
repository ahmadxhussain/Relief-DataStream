import React from 'react';
import { AppState } from '../types';
import { getTranslation } from '../data/translations';

interface HeaderProps {
  currentScreen: AppState['currentScreen'];
  currentLanguage: string;
  onNavigate: (screen: AppState['currentScreen']) => void;
}

const Header: React.FC<HeaderProps> = ({ currentScreen, currentLanguage, onNavigate }) => {
  const t = (key: string) => getTranslation(currentLanguage, key as any);
  
  return (
    <header className="header">
      <div className="container">
        <div className="header-content">
          <div className="logo" onClick={() => onNavigate('home')} style={{ cursor: 'pointer' }}>
            NGO Data Helpers
          </div>
          <nav className="nav">
            <button
              className={`nav-link ${currentScreen === 'home' ? 'active' : ''}`}
              onClick={() => onNavigate('home')}
              style={{ background: 'none', border: 'none', cursor: 'pointer' }}
            >
              {t('home')}
            </button>
            <button
              className={`nav-link ${currentScreen === 'history' ? 'active' : ''}`}
              onClick={() => onNavigate('history')}
              style={{ background: 'none', border: 'none', cursor: 'pointer' }}
            >
              {t('history')}
            </button>
            <button
              className={`nav-link ${currentScreen === 'settings' ? 'active' : ''}`}
              onClick={() => onNavigate('settings')}
              style={{ background: 'none', border: 'none', cursor: 'pointer' }}
            >
              {t('settings')}
            </button>
            <button
              className={`nav-link ${currentScreen === 'help' ? 'active' : ''}`}
              onClick={() => onNavigate('help')}
              style={{ background: 'none', border: 'none', cursor: 'pointer' }}
            >
              {t('help')}
            </button>
          </nav>
        </div>
      </div>
    </header>
  );
};

export default Header;