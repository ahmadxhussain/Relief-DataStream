export interface Country {
  code: string;
  name: string;
}

export interface DateRange {
  startDate: string;
  endDate: string;
}

export interface ReportData {
  summary: string;
  keyEvents: string[];
  trends: string[];
  risks: string[];
  chartData: ChartDataPoint[];
}

export interface ChartDataPoint {
  name: string;
  value: number;
  date?: string;
}

export interface ProgressStep {
  id: string;
  label: string;
  completed: boolean;
  active: boolean;
}

export interface ErrorState {
  message: string;
  show: boolean;
}

export interface AppState {
  currentScreen: 'home' | 'preview' | 'help' | 'history' | 'settings';
  selectedCountry: Country | null;
  dateRange: DateRange | null;
  reportData: ReportData | null;
  progressSteps: ProgressStep[];
  currentStep: number;
  error: ErrorState;
  isLoading: boolean;
}