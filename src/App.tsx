import React, { useState, useCallback, useEffect } from 'react';
import { AppState, Country, DateRange, ProgressStep, SavedReport } from './types';
import { countries, generateMockReportData } from './data/mockData';
import { getTranslation } from './data/translations';
import Header from './components/Header';
import HomeScreen from './components/HomeScreen';
import ReportPreview from './components/ReportPreview';
import HelpScreen from './components/HelpScreen';
import SettingsScreen from './components/SettingsScreen';
import HistoryScreen from './components/HistoryScreen';
import ErrorBanner from './components/ErrorBanner';

const initialProgressSteps: ProgressStep[] = [
  { id: 'collecting', label: 'Collecting Data', completed: false, active: false },
  { id: 'processing', label: 'Processing', completed: false, active: false },
  { id: 'summarizing', label: 'Summarizing', completed: false, active: false },
  { id: 'ready', label: 'Ready', completed: false, active: false },
];

const App: React.FC = () => {
  const [state, setState] = useState<AppState>({
    currentScreen: 'home',
    selectedCountry: null,
    dateRange: null,
    reportData: null,
    progressSteps: initialProgressSteps,
    currentStep: 0,
    error: { message: '', show: false },
    isLoading: false,
    currentLanguage: 'en',
    savedReports: [],
  });

  // Load saved settings and reports on app start
  useEffect(() => {
    const savedLanguage = localStorage.getItem('ngo-app-language') || 'en';
    const savedReports = localStorage.getItem('ngo-reports-history');
    
    setState(prev => ({
      ...prev,
      currentLanguage: savedLanguage,
      savedReports: savedReports ? JSON.parse(savedReports) : []
    }));
  }, []);

  const showError = useCallback((message: string) => {
    setState(prev => ({
      ...prev,
      error: { message, show: true }
    }));
  }, []);

  const hideError = useCallback(() => {
    setState(prev => ({
      ...prev,
      error: { message: '', show: false }
    }));
  }, []);

  const setScreen = useCallback((screen: AppState['currentScreen']) => {
    setState(prev => ({
      ...prev,
      currentScreen: screen,
      error: { message: '', show: false }
    }));
  }, []);

  const setLanguage = useCallback((language: string) => {
    setState(prev => ({
      ...prev,
      currentLanguage: language
    }));
    localStorage.setItem('ngo-app-language', language);
  }, []);

  const setCountry = useCallback((country: Country | null) => {
    setState(prev => ({
      ...prev,
      selectedCountry: country,
      error: { message: '', show: false }
    }));
  }, []);

  const setDateRange = useCallback((dateRange: DateRange | null) => {
    setState(prev => ({
      ...prev,
      dateRange,
      error: { message: '', show: false }
    }));
  }, []);

  const resetForm = useCallback(() => {
    setState(prev => ({
      ...prev,
      selectedCountry: null,
      dateRange: null,
      reportData: null,
      progressSteps: initialProgressSteps,
      currentStep: 0,
      isLoading: false,
      error: { message: '', show: false }
    }));
  }, []);

  const buildReport = useCallback(async () => {
    if (!state.selectedCountry || !state.dateRange) {
      showError('Please pick a country and valid dates.');
      return;
    }

    setState(prev => ({
      ...prev,
      isLoading: true,
      currentStep: 0,
      progressSteps: initialProgressSteps.map((step, index) => ({
        ...step,
        active: index === 0
      }))
    }));

    try {
      // Simulate progress steps
      for (let i = 0; i < initialProgressSteps.length; i++) {
        await new Promise(resolve => setTimeout(resolve, 1000));
        
        setState(prev => ({
          ...prev,
          currentStep: i + 1,
          progressSteps: prev.progressSteps.map((step, index) => ({
            ...step,
            completed: index <= i,
            active: index === i + 1
          }))
        }));
      }

      // Generate mock report data
      const reportData = generateMockReportData(state.selectedCountry, state.dateRange);
      
      // Save report to history
      const newReport: SavedReport = {
        id: Date.now().toString(),
        country: state.selectedCountry!,
        dateRange: state.dateRange!,
        reportData,
        createdAt: new Date().toISOString(),
        title: `${state.selectedCountry!.name} Report - ${state.dateRange!.startDate} to ${state.dateRange!.endDate}`
      };
      
      const updatedReports = [...state.savedReports, newReport];
      localStorage.setItem('ngo-reports-history', JSON.stringify(updatedReports));
      
      setState(prev => ({
        ...prev,
        reportData,
        savedReports: updatedReports,
        isLoading: false,
        currentScreen: 'preview'
      }));

    } catch (error) {
      showError('Could not build report. Please try again.');
      setState(prev => ({
        ...prev,
        isLoading: false,
        currentStep: 0,
        progressSteps: initialProgressSteps
      }));
    }
  }, [state.selectedCountry, state.dateRange, showError]);

  const downloadReport = useCallback(async (format: 'pdf' | 'docx') => {
    try {
      // Mock download - in real app, this would call the backend
      await new Promise(resolve => setTimeout(resolve, 1000));
      const t = (key: string) => getTranslation(state.currentLanguage, key as any);
      alert(`${t('downloading')} ${format.toUpperCase()} ${t('report')}... (${t('mockDownload')})`);
    } catch (error) {
      const t = (key: string) => getTranslation(state.currentLanguage, key as any);
      showError(t('errorDownload'));
    }
  }, [showError, state.currentLanguage]);

  const openReport = useCallback((report: SavedReport) => {
    setState(prev => ({
      ...prev,
      reportData: report.reportData,
      selectedCountry: report.country,
      dateRange: report.dateRange,
      currentScreen: 'preview'
    }));
  }, []);

  const renderCurrentScreen = () => {
    
    switch (state.currentScreen) {
      case 'home':
        return (
          <HomeScreen
            countries={countries}
            selectedCountry={state.selectedCountry}
            dateRange={state.dateRange}
            progressSteps={state.progressSteps}
            currentStep={state.currentStep}
            isLoading={state.isLoading}
            currentLanguage={state.currentLanguage}
            onCountryChange={setCountry}
            onDateRangeChange={setDateRange}
            onBuildReport={buildReport}
            onReset={resetForm}
          />
        );
      case 'preview':
        return (
          <ReportPreview
            reportData={state.reportData}
            currentLanguage={state.currentLanguage}
            onDownload={downloadReport}
            onBackToHome={() => setScreen('home')}
          />
        );
      case 'help':
        return (
          <HelpScreen
            onBackToHome={() => setScreen('home')}
          />
        );
      case 'settings':
        return (
          <SettingsScreen
            currentLanguage={state.currentLanguage}
            onLanguageChange={setLanguage}
            onBackToHome={() => setScreen('home')}
          />
        );
      case 'history':
        return (
          <HistoryScreen
            currentLanguage={state.currentLanguage}
            onOpenReport={openReport}
            onBackToHome={() => setScreen('home')}
          />
        );
      default:
        return null;
    }
  };

  return (
    <div className="App">
      <Header
        currentScreen={state.currentScreen}
        currentLanguage={state.currentLanguage}
        onNavigate={setScreen}
      />
      <div className="container">
        {state.error.show && (
          <ErrorBanner
            message={state.error.message}
            onClose={hideError}
          />
        )}
        {renderCurrentScreen()}
      </div>
    </div>
  );
};

export default App;