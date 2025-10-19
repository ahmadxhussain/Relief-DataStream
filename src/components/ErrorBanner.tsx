import React from 'react';
import { X } from 'lucide-react';

interface ErrorBannerProps {
  message: string;
  onClose: () => void;
}

const ErrorBanner: React.FC<ErrorBannerProps> = ({ message, onClose }) => {
  return (
    <div className="error-banner">
      <X size={20} />
      <span>{message}</span>
      <button
        onClick={onClose}
        style={{
          marginLeft: 'auto',
          background: 'none',
          border: 'none',
          cursor: 'pointer',
          color: 'inherit'
        }}
        aria-label="Close error"
      >
        <X size={16} />
      </button>
    </div>
  );
};

export default ErrorBanner;