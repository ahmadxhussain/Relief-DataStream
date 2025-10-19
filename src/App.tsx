import React, { useState, useCallback } from 'react';
import { AppState, Country, DateRange, ReportData, ProgressStep, ErrorState } from './types';
import { countries, generateMockReportData } from './data/mockData';
import Header from './components/Header';
import HomeScreen from './components/HomeScreen';
import ReportPreview from './components/ReportPreview';
import HelpScreen from './components/HelpScreen';
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
  });

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
      
      setState(prev => ({
        ...prev,
        reportData,
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
      alert(`Downloading ${format.toUpperCase()} report... (This is a mock download)`);
    } catch (error) {
      showError('Download failed. Please try again.');
    }
  }, [showError]);

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
      default:
        return null;
    }
  };

  return (
    <div className="App">
      <Header
        currentScreen={state.currentScreen}
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