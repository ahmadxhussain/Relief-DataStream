import React from 'react';
import { AppState } from '../types';

interface HeaderProps {
  currentScreen: AppState['currentScreen'];
  onNavigate: (screen: AppState['currentScreen']) => void;
}

const Header: React.FC<HeaderProps> = ({ currentScreen, onNavigate }) => {
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
              Home
            </button>
            <button
              className={`nav-link ${currentScreen === 'help' ? 'active' : ''}`}
              onClick={() => onNavigate('help')}
              style={{ background: 'none', border: 'none', cursor: 'pointer' }}
            >
              Help
            </button>
          </nav>
        </div>
      </div>
    </header>
  );
};

export default Header;